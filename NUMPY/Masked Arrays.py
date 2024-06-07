import numpy as np
import numpy.ma as ma


# No NumPy, um array mascarado (também conhecido como masked array) é uma extensão da
# classe ndarray que permite armazenar valores e máscaras em um único objeto.
# A máscara é um array booliano do mesmo tamanho e forma do array de dados,
# indicando quais elementos são válidos e quais devem ser ignorados em cálculos ou análises.
#
# Vantagens dos arrays mascarados:
#
#     1 - Tratamento de dados faltantes e inválidos: Arrays mascarados são ideais para lidar com dados faltantes,
#     inválidos ou corrompidos, pois permitem marcar esses elementos como inválidos na máscara
#     e realizar operações apenas com os dados válidos.
#
#     2 - Eliminação de ruído: A máscara pode ser utilizada para eliminar valores atípicos ou ruídos dos dados,
#     preservando apenas as informações relevantes.
#
#     3 - Seleção de subconjuntos: A máscara pode ser usada para selecionar subconjuntos específicos de dados
#     do array original, sem a necessidade de criar novos arrays.
#
#     4 - Eficiência de memória: Arrays mascarados podem ser mais eficientes em memória do que arrays padrão,
#     especialmente quando se trabalha com grandes conjuntos de dados com muitos valores ausentes ou inválidos.
#
#     Operações em arrays mascarados:
#
#     Operações matemáticas: Arrays mascarados suportam operações matemáticas padrão,
#     como adição, subtração, multiplicação e divisão. As operações são realizadas apenas nos
#     elementos válidos, ignorando os elementos mascarados.
#
#     Funções de agregação: Funções de agregação como sum(), mean(), min(), max() e std()
#     podem ser aplicadas a arrays mascarados, computando os valores apenas para os elementos válidos.
#
#     Indexação e fatiamento: Arrays mascarados podem ser indexados e fatiados da mesma forma
#     que arrays NumPy padrão. A máscara é preservada durante a indexação e fatiamento.


a = np.array([1,2,3,4,5])
mx = ma.masked_array(a, mask = [0,0,0,1,0]) #
print(f'Array com o Intruso: {a}')
print(f'Array sem o Intruso: {mx}')
print(f'Soma dos elementos desconsiderando o Intruso: {mx.sum()}')