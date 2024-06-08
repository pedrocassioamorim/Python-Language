import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

jogadores = {
    "Nome": [ "Marcos", "Cafu", "Luísão", "Edmilson", "Juninho Paulista", "Rivaldo", "Ronaldo", "Ronaldinho Gaúcho", "Kléber", "Dida",
        "Gilberto", "Anderson Polga", "Lúcio", "Juan", "Carlos Alberto", "Roberto Carlos", "Adriano", "Denílson", "Kaká", "Ronaldo Luís Nazário de Lima",
        "Emerson", "Maicon", "Lúcio", "Juan", "Felipe Melo", "Gilberto Silva", "Elano", "Kaká", "Robinho", "Adriano",
        "Júlio César", "Maicon", "Lúcio", "Juan", "David Luiz", "Dani Alves", "Thiago Silva", "Marcelo", "Oscar", "Hulk",
        "Fred", "David Luiz", "Thiago Silva", "Marcelo", "Dani Alves", "Fernandinho", "Paulinho", "Neymar", "Gabriel Jesus", "Willian",
        "Alisson", "Ederson", "Marquinhos", "Thiago Silva", "Dani Alves", "Alex Sandro", "Casemiro", "Arthur", "Neymar", "Roberto Firmino",
        "Vinicius Junior", "Alisson", "Ederson", "Marquinhos", "Thiago Silva", "Militão", "Alex Sandro", "Casemiro", "Bruno Guimarães", "Lucas Paquetá",
        "Neymar", "Vinicius Junior", "Raphinha", "Richarlison"],
    "Idade": [ 31, 32, 29, 26, 31, 31, 25, 22, 24, 32,
        31, 27, 28, 28, 28, 31, 29, 24, 22, 31,
        27, 29, 30, 30, 28, 31, 28, 25, 26, 29,
        33, 30, 33, 30, 27, 31, 29, 28, 22, 27,
        30, 33, 32, 29, 31, 29, 29, 25, 21, 25,
        29, 29, 30, 29, 32, 29, 29, 24, 29, 29,
        22, 30, 28, 30, 29, 25, 29, 24, 24, 25,
        29, 22, 25, 25],
    "Clube": [ "Palmeiras", "Roma", "Corinthians", "São Paulo", "Flamengo", "Barcelona", "Real Madrid", "Paris Saint-Germain", "Stuttgart", "Milan",
        "Cruzeiro", "Corinthians", "Bayer Leverkusen", "Flamengo", "Corinthians", "Real Madrid", "Internazionale", "São Paulo", "Milan", "Real Madrid",
        "Roma", "Internazionale", "Bayer Leverkusen", "Roma", "Juventus", "Milan", "Galatasaray", "Milan", "Manchester City", "Flamengo",
        "Internazionale", "Internazionale", "Chelsea", "Paris Saint-Germain", "Chelsea", "Juventus", "Milan", "Real Madrid", "Chelsea", "Zenit",
        "Fluminense", "Chelsea", "Paris Saint-Germain", "Chelsea", "Paris Saint-Germain", "Chelsea", "Juventus", "Milan", "Real Madrid", "Chelsea", "Zenit",
        "Fluminense", "Chelsea", "Paris Saint-Germain", "Real Madrid", "Juventus", "Manchester City", "Spartak Moscou", "Barcelona", "Manchester City", "Chelsea",
        "Liverpool", "Manchester City", "Liverpool", "Tottenham Hotspur", "Real Madrid", "Juventus", "Real Madrid", "Arsenal", "Paris Saint-Germain", "Liverpool",
        "Real Madrid", "Leeds United", "Tottenham"]}

nomes = 0
idades = 0
clubes =0

for i in range(len(jogadores['Nome'])):
    nomes += 1
for j in range(len(jogadores['Idade'])):
    idades += 1
for k in range(len(jogadores['Clube'])):
    clubes += 1

print(f' nomes: {nomes}')
print(f' idades: {idades}')
print(f' clubes: {clubes}')

# AQUI TEMOS UM DATAFRAME PARA USAR NOS TESTES DO SEABORN
selecao = pd.DataFrame(jogadores)
print(selecao)

# HISTOGRAMAS
sns.displot(selecao['Idade'])
plt.title("Distribuição de Idades")
plt.show()

# BOXPLOT
sns.boxplot(x="Idade", data=selecao)
plt.title("Distribuição de Idade por Copas")
plt.show()

# VIOLINPLOT   =>  COMPARANDO IDADES
sns.violinplot(x="Idade", y="Nome", data=selecao, palette="hls")
plt.title("Idade média por Copa")
plt.show()

