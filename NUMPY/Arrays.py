import numpy as np

#   ARRAYS COM ZEROs
zero_array = np.zeros((5,2), dtype=int)     #   ARRAY BIDIMENSIONAL

#   ARRAYS COM UMs # TRIDIMENSIONAL
one_array = np.ones((6,8,4)) #    NÃO ESPECIFICAMOS DTYPE

#   ARRAYS COM MAIS INFORMAÇÕES
special_array = np.arange(1,100,3)

#   ARRAYS COM DADDOS PERSONALIZADOS E USO DO RESHAPE
#   PEGANDO UM ARRAY LINEAR DE 100 ELEMENTOS E RESHAPANDO PARA 4 ESTRUTURAS DE 5 LINHAS E 5 COLUNAS (TRIDIMENSIONAL)
array1 = np.arange(100).reshape(4,5,5)
#   IMPORTANTE PRESTAR ATENÇÃO QUE O NUMERO DE ELEMENTOS (100) TEM QUE SER IGUAL AO NUMERO DE ELEMENTOS NO TENSOR (4,5,5)

#   FUNÇÃO LINSPACE
array_linear = np.linspace(1,100,100, endpoint=True)



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
print()

print("Arrays com Dados Personalizados")
print(f'dtype: {special_array.dtype}')
print(special_array)
print(f' ndim: {special_array.ndim}')
print(f' shape: {special_array.shape}')
print(f' size: {special_array.size}')
print()
print()
print("Arrays com Personalização e RESHAPE")
print(f'dtype: {array1.dtype}')
print(array1)
print(f' ndim: {array1.ndim}')
print(f' shape: {array1.shape}')
print(f' size: {array1.size}')
print()
print("Array com Linspace")
print(f'dtype: {array_linear.dtype}')
print(array_linear)
print(f' ndim: {array_linear.ndim}')
print(f' shape: {array_linear.shape}')
print(f' size: {array_linear.size}')