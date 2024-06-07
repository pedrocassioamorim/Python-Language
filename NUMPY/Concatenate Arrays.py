import numpy as np

# ARRAYS
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# CONCATENATING ARRAYS
c = np.concatenate((a, b))
d = np.concatenate((b, a))

# EXEMPLE OF CONSULTING VALUES INSIDE ARRAYS
e = np.arange(100).reshape(10, 10)

# PRINTING
print(a)
print(b)
print(c)
print(d)
print(e)

#PRINTING
print(e[4][5]) # consultando elemento da linha 4 x coluna 5