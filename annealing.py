import random
import math
import time
from dataset import Dataset

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
    if new_v <= old_v:
        return True
    else:
        d = old_v - new_v
        return math.exp(t*d/new_v) < random.random()

def average(s):
    sum_v = 0.0
    for l,v in s:
        sum_v += v
    return sum_v / len(s)

def sim_annealing(spark_context,data,core_num):
    def sub_annealing(s):
        data.load_library()
        sub_best = ([],0.0)
        t = T
        min_t = T * 0.8
        while t > min_t:
            old_node,old_v = s
            new_node = old_node[:]
            ri = random.randrange(data.residue_num)
            new_node[ri] = random.randrange(data.rotamer_num[ri])
            new_v = data.calc_energy(new_node)
            if accept(new_v,old_v,t):
                s = (new_node,new_v)
            if new_v < sub_best[1]:
                sub_best = (new_node,new_v)
            t *= 0.98
        return (s,sub_best)

    n = data.residue_num
    rot_n = data.rotamer_num
    solution = generate_solution(core_num,data.rotamer_num)
    avg_s = average(solution)
    best = ([],0.0)
    T = 100.0
    while T > 1:
        if core_num > 1:
            solution_p = spark_context.parallelize(solution)
            new_s_and_best = solution_p.map(sub_annealing).collect()
        else:
            new_s_and_best = [sub_annealing(solution[0])]
        new_s,b = split(new_s_and_best)
        new_avg = average(new_s)
        if accept(new_avg,avg_s,T):
            solution = new_s
            avg_s = new_avg
        if b[1] < best[1]:
            best = b
        T = T * 0.9
    return best

if __name__ == '__main__':
    data = Dataset("rotamerLibrary", "energyTable")
    start = time.time()
    result = sim_annealing(0,data,1)
    elapsed = time.time() - start
    print result
    print elapsed
