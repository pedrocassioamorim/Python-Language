import pandas as pd

# CRIANDO DATAFRAMES A PARTIR DE ARQUIVOS CSV
caminho = 'Base Geral.csv'
arquivo = pd.read_csv(caminho)
print(arquivo)

# CRIANDO DATAFRAMAS A PARTIR DE PLANILHAS
outro = 'plants.ods'
outro_arquivo = pd.read_excel(outro)
print(outro_arquivo)