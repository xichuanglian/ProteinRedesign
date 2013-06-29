#!/usr/bin/python
import sys
rotamer_table = open(sys.argv[1])
energy_table = open(sys.argv[2])
n = int(rotamer_table.readline())
rotamer_number = [0] * n
for i in range(n):
    rotamer_number[i] = int(rotamer_table.readline())
pre_sum = []
s = 0
for i in rotamer_number:
    pre_sum.append(s)
    s += i
rotamer_out = open("rotamerLibrary",'w')
energy_out = open("energyTable",'w')
rotamer_out.write(str(n)+"\n")
for i in rotamer_number:
    rotamer_out.write(str(i)+' ')
m = int(energy_table.readline())
assert sum(rotamer_number) == m
nums = [None]*m
for i in range(m):
    line = energy_table.readline()
    nums[i] = [float(s) for s in line.split()]
energy_out.write(str(n)+"\n")
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        energy_out.write(str(i)+" "+str(j))
        for ii in range(rotamer_number[i]):
            for jj in range(rotamer_number[j]):
                energy_out.write(" "+str(nums[pre_sum[i]+ii][pre_sum[j]+jj]))
        energy_out.write("\n")
rotamer_out.close()
energy_out.close()
