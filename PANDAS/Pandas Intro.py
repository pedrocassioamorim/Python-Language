import pandas as pd

# CRIANDO DATAFRAMES A PARTIR DE ARQUIVOS CSV
caminho = 'Base Geral.csv'
arquivo = pd.read_csv(caminho)
print(arquivo)

# CRIANDO DATAFRAMAS A PARTIR DE PLANILHAS
outro = 'plants.ods'
outro_arquivo = pd.read_excel(outro)
print(outro_arquivo)

# NOVOS EXEMPLOS DE DATAFRAMES
brasil1 = pd.read_excel('selecao brasileira 2002 (excel).xlsx') # A PARTIR DE UMA PLANILHA DE EXCEL
brasil2 = pd.read_csv('selecao brasileira 2002 (csv).csv') # A PARTIR DE UM ARQUIVO CSV

print(brasil1.head()) # HEAD: imprime as primeias 5 linhas
print(brasil2.head()) # HEAD: imprime as primeias 5 linhas
print(brasil1.tail()) # TAIL: imprime as ultimas 5 linhas