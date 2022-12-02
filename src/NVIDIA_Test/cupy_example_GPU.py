#!/usr/bin/python3

###########################################
# numpy excutes on CPU side
# cupy  excutes on GPU side 
###########################################

import cupy as cp 

SIZE=10

fward=cp.empty([SIZE,SIZE], dtype=float)
bward=cp.empty([SIZE,SIZE], dtype=float)
diff= cp.empty([SIZE,SIZE], dtype=float)

A = cp.random.rand(SIZE,SIZE)
B = cp.random.rand(SIZE,SIZE)
C = cp.random.rand(SIZE,SIZE)
D = cp.random.rand(SIZE,SIZE)

fward = A * B * C * D
bward = D * C * B * A

diff = fward - bward

print( diff )



###########################################
# Note: installing cupy
#
# python3 -m pip install cupy-cuda11x
###########################################
