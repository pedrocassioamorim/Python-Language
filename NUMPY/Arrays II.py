import numpy as np

dados = np.array([1,2,3,4,5,6,7,8])

#   SALVANDO ARRAYS EM ARQUIVOS BINÁRIOS DO TIPO NPY
np.save('dados.npy', dados)
#   CARREGANDO ARQUIVOS BINÁRIOS
b = np.load('dados.npy')
print(b)

# LENDO ARQUIVOS CSV
import csv
from numpy import genfromtxt
from google.colab import files
