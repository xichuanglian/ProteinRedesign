import random
import math
import time
from dataset import Dataset
from mpi4py import MPI

def temperature(t):
    return 0.8 * t

def generate_solution(core_num,rotamer_num):
    data.load_library()
    s = []
    for i in range(core_num):
        l = [random.randrange(x) for x in rotamer_num]
        v = data.calc_energy(l)
        s.append((l,v))
    return s

def split(n_and_b):
    best = ([],0)
    l = []
    for s,b in n_and_b:
        l.append(s)
        if b[1] < best[1]:
            best = b
    return (l,best)

def accept(new_v,old_v,t):
    if new_v > 0:
        return False
    if new_v <= old_v:
        return True
    else:
        d = new_v - old_v
        return math.exp(t*d/new_v) < random.random()

def average(s):
    sum_v = 0.0
    for l,v in s:
        sum_v += v
    return sum_v / len(s)

def sub_annealing(data,s,T):
    sub_best = ([],0.0)
    t = T
    min_t = T * 0.1
    while t > min_t:
        for i in range(data.rotamer_sum/10):
            old_node,old_v = s
            new_node = old_node[:]
            ri = random.randrange(data.residue_num)
            new_node[ri] = random.randrange(data.rotamer_num[ri])
            new_v = data.calc_energy(new_node)
            if accept(new_v,old_v,t):
                s = (new_node,new_v)
            if new_v < sub_best[1]:
                sub_best = (new_node,new_v)
        t *= 0.999
    return (s,sub_best)

def sim_annealing(comm,data,core_num):
    n = data.residue_num
    rot_n = data.rotamer_num
    solution = generate_solution(core_num,data.rotamer_num)
    avg_s = average(solution)
    best = ([],10.0)
    T = 100.0
    stable_count = 0
    while T > 0.001 and stable_count < 10:
        T = comm.bcast(T,root=0)
        s = comm.scatter(solution,root=0)
        s = sub_annealing(data,s,T)
        new_s_and_best = comm.gather(s,root=0)
        new_s,b = split(new_s_and_best)
        new_avg = average(new_s)
        if accept(new_avg,avg_s,T):
            solution = new_s
            avg_s = new_avg
        if b[1] < best[1]:
            best = b
            stable_count = 0
        stable_count += 1
        T = T * 0.6
    T = -1
    T = comm.bcast(T,root=0)
    return best

def sim_annealing_worker(comm,data):
    T = None
    T = comm.bcast(T,root=0)
    while T > 0:
        s = None
        s = comm.scatter(s,root=0)
        s = sub_annealing(data,s,T)
        s = comm.gather(s,root=0)
        T = comm.bcast(T,root=0)

if __name__ == '__main__':
    data = Dataset("rotamerLibrary", "energyTable")
    data.load_library()
    comm = MPI.COMM_WORLD
    size = comm.Get_size()
    rank = comm.Get_rank()

    if rank == 0:
        start = time.time()
        result = sim_annealing(comm,data,size)
        elapsed = time.time() - start
        print result
        print elapsed
    else:
        sim_annealing_worker(comm,data)
