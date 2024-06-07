# NUMPY part I & ARRAYS - O NumPy é um framework muito utilizado para análise de dados
# e cálculos científicos devido a sua velocidade de processamento.
# Ele processa vetores, matrizes e tensores (de várias dimensões) com grande eficiência.
# Além disso, ele opera funções matemáticas sobre essas estruturas de forma esplêndida.
# Ou seja, dada as informações, é clara a ideia de lidar, de forma eficaz,
# sobre grande quantidade de dados que estarão compondo essas estruturas.

# Vale lembrar que a principal estrutura de dados do NumPy é o array,
# e todas as funções são estruturadas em cima dele.
# Por meio dele nós podemos gerar vetores, matrizes e tensores,
# os quais armazenarão os dados que iremos trabalhar.

import numpy as np
# CRIANDO ARRAY COM UMA DIMENSÃO
a = np.array([1,2,3,4])

# CRIANDO ARRAY COM DUAS DIMENSÕES
b = np.array([[1, 2, 3], [4,5,6]])
c = np.array([[7,8], [9,10], [11,12]])

# CRIANDO ARRAY COM TRÊS DIMENSÕES
d = np.ones((4,8,10))

# PRODUTO ESCALAR
# O produto escalar, também conhecido como produto interno ou produto ponto, é uma operação matemática que combina dois vetores em um único número real.
#
# Como funciona:
#
#     Vetores 1D: Se ambos a e b forem arrays 1D, o np.dot calcula o produto interno dos vetores.
#     Vetores 2D (Matrizes): Se ambos a e b forem arrays 2D, o np.dot calcula a multiplicação de matrizes.
#     Arrays N dimensionais: Se um dos arrays for 0D (escalar) ou se os arrays tiverem dimensões incompatíveis,
#                            o np.dot gera um erro.
#     Conjugado complexo: Se a ou b forem complexos, o np.dot usa o conjugado complexo de a no cálculo.
np.dot(b,c) # PRODUTO INTERNO DE B (2 LINHAS) E C (2 COLUNAS) = RESULTADO = UMA MATRIZ 2 X 2


# Visualizando o tamanho do ARRAY
print("Array a dimensions:")
print(a)
print(f'ndim: {a.ndim}') #DIMENSÕES com .ndim
print(f'size: {a.size}') #SIZE com .size
print(f'shape: {a.shape}') #SHAPE com .shape
print()
print("Array b dimensions:")
print(b)
print(f'ndim: {b.ndim}') #DIMENSÕES com .ndim
print(f'size: {b.size}') #SIZE (numero de elementos) com .size
print(f'shape: {b.shape}') #SHAPE (organização dos elementos) com .shape
print()
print("Array c dimensions:")
print(c)
print(f'ndim: {c.ndim}') #DIMENSÕES com .ndim
print(f'size: {c.size}') #SIZE com .size
print(f'shape: {c.shape}') #SHAPE com .shape
print()
print("Array d dimensions:")
print(d)
print(f'ndim: {d.ndim}') #DIMENSÕES com .ndim
print(f'size: {d.size}') #SIZE com .size
print(f'shape: {d.shape}') #SHAPE com .shape
print()


print("Dot product of two arrays: b x c")
print(np.dot(b,c)) #PRODUTO ESCALAR B (2 linhas) X C (2 colunas) = RESULTADO = Uma matriz 2 x 2 com a multiplicação das matrizes
