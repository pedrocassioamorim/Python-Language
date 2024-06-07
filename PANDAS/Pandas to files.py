import pandas as pd
import numpy as np

# Criando um Array Numpy com valores aleatórios entre 0 e 100
dadosRandom = np.random.randint(0, 101, size=(100, 8))
print(dadosRandom)

# Criando dados em ordem crescente com Numpy e usando um reshape tridimensional
# Tensor (8 tabelas de 10 linhas e 10 colunas)
dadosOrganizados = np.arange(800).reshape(8,10,10)
print(dadosOrganizados)

#   AQUI TEMOS UM ARRAY DE TRES DIMENSÕES (TENSOR 3D), PRECISAMOS CONVERTER PARA UMA ESTRETURA DE DUAS DIMENSOES
#   PARA PODERMOS SALVAR COMO UM DATAFRAME

dadosOrganizados = dadosOrganizados.reshape(100,8)

# Criando um Dataframa a partir dos Arrays de Numpy
dataRandom = pd.DataFrame(dadosRandom, columns=list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']))
dataOrganizado = pd.DataFrame(dadosOrganizados, columns=list(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']))

print(dataRandom)
print(dataOrganizado)

# Inserindo valores NaN em todos os valores menores de 15, por exemplo:
prob_nan = 15
for i in range (dataRandom.shape[0]):
    for j in range (dataRandom.shape[1]):
        if dataRandom.iloc[i, j] <= prob_nan:
            dataRandom.iloc[i, j] = np.nan
print(dataRandom)

# AGORA IREMOS REMOVER VALORES NaN do nosso dataframe:
print(dataRandom.isnull().sum())

# Removendo valores nulos de A pelo valor int 10  => TBM FUNCIONA PARA STRINGS E FLOATS
dataRandom = dataRandom.fillna('Pedro')
print(dataRandom)
