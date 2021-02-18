import numpy as np
import sys
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

n_ranks = int(sys.argv[1])

x = np.random.randint(10, size=10)

sumRank = np.zeros(1)
total = np.zeros(1)
sumRank[0] = np.sum(x)
comm.Reduce(sumRank, total, op=MPI.SUM, root=0)
if rank == 0:
    print(f"Total sum across all ranks: {total}")
