# Create a 5x5 matrix and fill it with a checkerboard pattern

import numpy as np

x = np.ones((3,3))
x = np.zeros((5,5),dtype=int)
x[1::2,::2] = 1
x[::2,1::2] = 1
print(x)