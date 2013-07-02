from dataset import Dataset
from ctypes import *
import time

def next_solution(current,rotamer_num):
    idx = 0
    l = len(current)
    while idx < l and current[idx] == rotamer_num[idx] - 1:
        idx += 1
    if idx == l:
        return None
    re = [0] * l
    re[idx] = current[idx] + 1
    for i in range(idx+1,l):
        re[i] = current[i]
    return re


data = Dataset("rotamerLibrary", "energyTable")
data.load_library()
data.lib.calc_energy.restype = c_float
current = [0] * data.residue_num

start = time.time()
solution = dict()
count = 0
while current:
    nodes_c = (c_int * len(current))(*current)
    e = data.lib.calc_energy(byref(nodes_c), data.residue_num,
                             byref(data.rotamer_num_c), byref(data.offset_c), byref(data.energy_c));
    solution[e] = current
    current = next_solution(current,data.rotamer_num)
    count += 1
    if count % 10000000 == 0:
        print count
elapsed = time.time() - start

count = 0
pairs = solution.items()
pairs.sort()
for v,s in pairs:
    print v,s
    count += 1
    if count > 10:
        break
print "Time:",elapsed
