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
print(brasil1.info())
print(brasil1.columns)
print(brasil1['Nome Completo'])
brasil3 = brasil1.rename(columns={'Nome Completo': 'Nome Inteiro'})
print(brasil3)

# ACESSANDO ITENS ESPECIFICOS NO DATAFRAME
# Consultando dados com o as funções `loc[] e iloc[]`:
# *Acessando um valor específico do Dataframe;*

print("Função iloc [ 3 , 3 ]: ") # = LINHA 3 E COLUNA 3 = RETORNA APENAS UM UNICO VALOR (MAIS ESPECÍFICO)
print(brasil3.iloc[3,3])
print("Função loc [ 3 ]: ") # LINHA 3 = RETORNA A LINHA INTEIRA
print(brasil3.loc[3])
print(brasil3.iloc[3:8])
print()
print()

# SET INDEX - TRABALHANDO COM INDEX DE FORMA FÁCIL
brasil3.set_index('Clube', inplace=True)
print(brasil3)

# O ILOC ENCONTRA O OBJETO DA LINHA 3, USANDO A NOVA CHAVE
print(brasil3.iloc[3])

# O LOC ENCONTRA MULTIPLOS VALORES PELO VALOR DE UMA CHAVE
# CONCATENAÇÃO DE DATAFRAMES
# USAR SEMPRE O METODO  ==================>  concat([df1,df2])
# O método append() foi descontinuado.
membersSP = brasil3.loc['São Paulo']
membersRM = brasil3.loc['Real Madrid']
members = pd.concat([membersSP, membersRM])
print(members)


# RESETANDO INDICES NUMÉRICOS
membersBC = brasil1.loc[(brasil1['Clube'] == 'Barcelona') | (brasil1['Clube'] == 'Real Madrid')]
membersBC.reset_index(inplace=True)
membersBC = membersBC.drop(columns=['index'])
print(membersBC)
membersBC.to_csv('Brasileiros em Real e Barça')