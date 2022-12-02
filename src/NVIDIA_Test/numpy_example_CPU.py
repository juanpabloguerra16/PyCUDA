#!/usr/bin/python3

###########################################
# numpy excutes on CPU side
# cupy  excutes on GPU side 
###########################################

import numpy as np 

SIZE=10

fward=np.empty([SIZE,SIZE], dtype=float)
bward=np.empty([SIZE,SIZE], dtype=float)
diff= np.empty([SIZE,SIZE], dtype=float)

A = np.random.rand(SIZE,SIZE)
B = np.random.rand(SIZE,SIZE)
C = np.random.rand(SIZE,SIZE)
D = np.random.rand(SIZE,SIZE)

fward = A * B * C * D
bward = D * C * B * A

diff = fward - bward

print( diff )


