import numpy as np
from numpy.random import default_rng

rng=default_rng(42)

a=rng.integers(100,size=(3,5))

np.sort(a,axis=0)

print(np.sort(a,axis=1))