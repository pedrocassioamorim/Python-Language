import numpy as np

# ARRAYS
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

# CONCATENATING ARRAYS
c = np.concatenate((a, b))
d = np.concatenate((b, a))

# EXEMPLE OF CONSULTING VALUES INSIDE ARRAYS
e = np.arange(100).reshape(10, 10)

# INSERINDO LÓGICA NA PROCURA DOS ELEMENTOS
f = e[e > 45] # TODOS OS NUMEROS DE 'e' QUE SÃO MAIORES QUE 45
g = f[f % 2 == 0] # TODOS OS NUMEROS DE 'f' QUE SÃO PARES


# PRINTING
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#PRINTING
print(e[4][5]) # consultando elemento da linha 4 x coluna 5