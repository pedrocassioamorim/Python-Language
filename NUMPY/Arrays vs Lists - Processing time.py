import numpy as np
from time import process_time
from numpy.random import default_rng

# CREATING A LIST OF 10.000.000 ITENS
rng = default_rng()
t0 = process_time()
lista = list(rng.integers(1,1000,10000000))
t1 = process_time()
print(type(lista))
print(t1-t0)

# CREATING AN ARRAY OF 10.000.000 ITENS
t2 = process_time()
arr = rng.integers(1,1000,10000000)
t3 = process_time()
print(type(arr))
print(t3-t2)

# <class 'list'>
# 1.1896024779999999
# <class 'numpy.ndarray'>
# 0.08916595900000024
