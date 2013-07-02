#!/bin/bash

mpiexec -f hosts2 -n 2 ./gen_data.sh 10
echo "Test 10:" >> result.log
echo "Running test 10..."
mpiexec -f hosts -n 40 python annealing_mpi.py >> result.log

mpiexec -f hosts2 -n 2 ./gen_data.sh 11
echo "Test 11:" >> result.log
echo "Running test 11..."
mpiexec -f hosts -n 40 python annealing_mpi.py >> result.log

mpiexec -f hosts2 -n 2 ./gen_data.sh 12
echo "Test 12:" >> result.log
echo "Running test 12..."
mpiexec -f hosts -n 40 python annealing_mpi.py >> result.log

mpiexec -f hosts2 -n 2 ./gen_data.sh 13
echo "Test 13:" >> result.log
echo "Running test 13..."
mpiexec -f hosts -n 40 python annealing_mpi.py >> result.log

mpiexec -f hosts2 -n 2 ./gen_data.sh 14
echo "Test 14:" >> result.log
echo "Running test 14..."
mpiexec -f hosts -n 40 python annealing_mpi.py >> result.log

mpiexec -f hosts2 -n 2 ./gen_data.sh 15
echo "Test 15:" >> result.log
echo "Running test 15..."
mpiexec -f hosts -n 40 python annealing_mpi.py >> result.log

mpiexec -f hosts2 -n 2 ./gen_data.sh 16
echo "Test 16:" >> result.log
echo "Running test 16..."
mpiexec -f hosts -n 40 python annealing_mpi.py >> result.log

mpiexec -f hosts2 -n 2 ./gen_data.sh 17
echo "Test 17:" >> result.log
echo "Running test 17..."
mpiexec -f hosts -n 40 python annealing_mpi.py >> result.log

mpiexec -f hosts2 -n 2 ./gen_data.sh 18
echo "Test 18:" >> result.log
echo "Running test 18..."
mpiexec -f hosts -n 40 python annealing_mpi.py >> result.log

mpiexec -f hosts2 -n 2 ./gen_data.sh 19
echo "Test 19:" >> result.log
echo "Running test 19..."
mpiexec -f hosts -n 40 python annealing_mpi.py >> result.log

mpiexec -f hosts2 -n 2 ./gen_data.sh 20
echo "Test 20:" >> result.log
echo "Running test 20..."
mpiexec -f hosts -n 40 python annealing_mpi.py >> result.log
