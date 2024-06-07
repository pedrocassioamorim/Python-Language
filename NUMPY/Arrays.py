import numpy as np

#   ARRAYS COM ZEROs
zero_array = np.zeros((5,2), dtype=int)     #   ARRAY BIDIMENSIONAL

#   ARRAYS COM UMs # TRIDIMENSIONAL
one_array = np.ones((6,8,4)) #    NÃO ESPECIFICAMOS DTYPE

#   ARRAYS COM MAIS INFORMAÇÕES
special_array = np.arange(1,100,3)


print("ARRAY com ZEROs: ")
print(f' dtype: {zero_array.dtype}')
print(zero_array)
print(f' ndim: {zero_array.ndim}')
print(f' shape: {zero_array.shape}')
print(f' size: {zero_array.size}')
print()

print("Arrays com UMs: ")
print("AQUI NO PADRÃO DO NUMPY, COMO FLOAT64")
print(f' dtype: {one_array.dtype}')
print(one_array)
print(f' ndim: {one_array.ndim}')
print(f' shape: {one_array.shape}')
print(f' size: {one_array.size}')