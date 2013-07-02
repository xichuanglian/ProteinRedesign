#!/bin/bash

cd test_data
./convert_data.py 16_rotamer_table 16_energy_table
mv rotamerLibrary energyTable ../
cd ..
~/spark-0.7.0/pyspark protein_redesign.py local 1 > experiment_log/astar_16_local_1.log

cd test_data
./convert_data.py 17_rotamer_table 17_energy_table
mv rotamerLibrary energyTable ../
cd ..
~/spark-0.7.0/pyspark annealing.py local 15 > experiment_log/annealing_17_local_1.log
~/spark-0.7.0/pyspark protein_redesign.py local 1 > experiment_log/astar_17_local_1.log

cd test_data
./convert_data.py 18_rotamer_table 18_energy_table
mv rotamerLibrary energyTable ../
cd ..
~/spark-0.7.0/pyspark annealing.py local 15 > experiment_log/annealing_18_local_1.log
~/spark-0.7.0/pyspark protein_redesign.py local 1 > experiment_log/astar_18_local_1.log

cd test_data
./convert_data.py 19_rotamer_table 19_energy_table
mv rotamerLibrary energyTable ../
cd ..
~/spark-0.7.0/pyspark annealing.py local 15 > experiment_log/annealing_19_local_1.log
~/spark-0.7.0/pyspark protein_redesign.py local 1 > experiment_log/astar_19_local_1.log

cd test_data
./convert_data.py 20_rotamer_table 20_energy_table
mv rotamerLibrary energyTable ../
cd ..
~/spark-0.7.0/pyspark annealing.py local 15 > experiment_log/annealing_20_local_1.log
~/spark-0.7.0/pyspark protein_redesign.py local 1 > experiment_log/astar_20_local_1.log
