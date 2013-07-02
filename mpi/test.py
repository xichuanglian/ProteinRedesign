#!/usr/bin/python

from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = 10
    comm.send(data,dest=1,tag=11)
else:
    data = None
    data = comm.recv(source=0,tag=11)

print rank,data
