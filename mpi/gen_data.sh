#!/bin/bash

cd ../test_data
./convert_data.py $1_rotamer_table $1_energy_table
mv rotamerLibrary energyTable ../mpi
cd ../mpi
