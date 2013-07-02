#!/bin/bash

cd ../test_data
./convert_data.py 11_rotamer_table 11_energy_table
mv rotamerLibrary energyTable ../mpi
cd ../mpi
echo "11" >> result.log
mpiexec -n 20 python annealing_mpi.py >> result.log

cd ../test_data
./convert_data.py 12_rotamer_table 12_energy_table
mv rotamerLibrary energyTable ../mpi
cd ../mpi
echo "12" >> result.log
mpiexec -n 20 python annealing_mpi.py >> result.log

cd ../test_data
./convert_data.py 13_rotamer_table 13_energy_table
mv rotamerLibrary energyTable ../mpi
cd ../mpi
echo "13" >> result.log
mpiexec -n 20 python annealing_mpi.py >> result.log

cd ../test_data
./convert_data.py 14_rotamer_table 14_energy_table
mv rotamerLibrary energyTable ../mpi
cd ../mpi
echo "14" >> result.log
mpiexec -n 20 python annealing_mpi.py >> result.log

cd ../test_data
./convert_data.py 15_rotamer_table 15_energy_table
mv rotamerLibrary energyTable ../mpi
cd ../mpi
echo "15" >> result.log
mpiexec -n 20 python annealing_mpi.py >> result.log

cd ../test_data
./convert_data.py 16_rotamer_table 16_energy_table
mv rotamerLibrary energyTable ../mpi
cd ../mpi
echo "16" >> result.log
mpiexec -n 20 python annealing_mpi.py >> result.log

cd ../test_data
./convert_data.py 17_rotamer_table 17_energy_table
mv rotamerLibrary energyTable ../mpi
cd ../mpi
echo "17" >> result.log
mpiexec -n 20 python annealing_mpi.py >> result.log

cd ../test_data
./convert_data.py 18_rotamer_table 18_energy_table
mv rotamerLibrary energyTable ../mpi
cd ../mpi
echo "18" >> result.log
mpiexec -n 20 python annealing_mpi.py >> result.log

cd ../test_data
./convert_data.py 19_rotamer_table 19_energy_table
mv rotamerLibrary energyTable ../mpi
cd ../mpi
echo "19" >> result.log
mpiexec -n 20 python annealing_mpi.py >> result.log

cd ../test_data
./convert_data.py 20_rotamer_table 20_energy_table
mv rotamerLibrary energyTable ../mpi
cd ../mpi
echo "20" >> result.log
mpiexec -n 20 python annealing_mpi.py >> result.log
