import numpy as np

# UM EXEMPLO DE UMA LISTA COM VÁRIOS TODOS OS TIPOS DE DADOS (STRING, BOOLEAN, INTEGER & FLOAT)
list1 = [1, "bia", 2,3, False ,4,5, "Pedro",6,7.7, "Amorim" ,8,9]
print(list1)
print(type(list1))
print(len(list1))
print()

arr = np.array(list1) # TRANSFORMOU TODOS OS DADOS EM STRING
print(arr)
print(type(arr))

# OPERAÇÕES COM LISTAS E ARRAYS:
lista2 = [1, 5, 8, 9]
arr2 = np.array(lista2)

# A MULTIPLICAÇÃO EM LISTAS, GERA UMA NOVA LISTAS COM OS ELEMENTOS REPLICADOS 5 VEZES
multiL = lista2 * 5
print(multiL)
print(type(multiL))
print()

# A MULTIPLICAÇÃO DE ARRAYS, GERA UM ARRAY DO MESMO TAMANHO E OS VALORES SÃO MULTIPLICADOS POR 5, TODOS DE UMA VEZ
multiA = arr2 * 5
print(multiA)
print(type(multiA))
