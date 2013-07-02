f = open("experiment.sh","w")
f.write("#!/bin/bash\n")
for i in range(10,21):
    f.write("\n")
    f.write("mpiexec -f hosts2 -n 2 ./gen_data.sh {0}\n".format(i))
    f.write("echo \"Test {0}:\" >> result.log\n".format(i))
    f.write("echo \"Running test {0}...\"\n".format(i))
    f.write("mpiexec -f hosts -n 40 python annealing_mpi.py >> result.log\n")

