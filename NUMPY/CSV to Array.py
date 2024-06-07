import numpy as np
import csv

# LENDO ARQUIVOS CSV
caminho = '/home/pedro/PycharmProjects/Python-RawLanguageComplete/NUMPY/Base Geral.csv'
arquivo = csv.reader(caminho)

# CONVERT FROM CSV TO ARRAY
data = np.recfromcsv(caminho, encoding='utf-8')

# PRINTING
print(data)
print(type(data))
print(f'ndim: {data.ndim}')

# LEITURA DE ARQUIVOS EM PYTHON
with open (caminho, 'r') as f:
    # AQUI A VARIAVEL RECEBE O VALOR DOS ARQUIVOS EM FORMA DE LISTA
    dados = list(csv.reader(f))
    print(dados)
# TEM SEUS DADOS TRANSFORMADOS EM ARRAY
array_dados = np.recfromtxt(caminho, delimiter=",")
print(array_dados)
print(f'type: {type(array_dados)}')
print(f' shape: {array_dados.shape}')
print(f' dtype: {array_dados.dtype}')
print(f' ndim: {array_dados.ndim}')
# PRINTING
# print(array_dados)