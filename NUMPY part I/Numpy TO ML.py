from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import matplotlib.pyplot as plt

# CARREGANDO DATASET
iris = load_iris()
iris.keys()
print(iris.keys())

# Mostrando a Descrição do DATASET:
print(iris['DESCR'][:193])

# A classificação que iremos utilizar:
print(iris['target_names'])

# Características que iremos analisar:
print(iris['feature_names'])

#Dados sobre nosso DATASET, vistos anteriormente:
print(iris['data'].shape)
print(iris['data'][:10]) # AS 10 PRIMEIRAS LINHAS DO ARRAY

# TARGET:
print(iris['target'])

# Dividindo DATASET em treino e teste:
X_train, X_test, y_train, y_test = train_test_split(iris['data'], iris['target'], random_state=0)
print(X_train.shape)
print(X_test.shape)

# ANALISE GRAFICA DOS DADOS: DECISÃO DO MODELO DE ML

fig, ax = plt.subplots(3,3,figsize=(15,15))
for i in range(3):
    for j in range(3):
        ax[i,j].scatter(X_train[:,j], X_train[:, i + 1], c=y_train, s=60)
        ax[i,j].set_xticks(())
        ax[i,j].set_yticks(())

        if i == 2:
            ax[i,j].set_xlabel(iris['feature_names'][j])
        if j == 0:
            ax[i,j].set_ylabel(iris['feature_names'][i + 1])
        if j > i:
            ax[i,j].set_visible(False)
plt.show()

# CRIANDO O NOSSO MODELO
kmn = KNeighborsClassifier(n_neighbors=1)
kmn.fit(X_train, y_train)

# TESTANDO O MODELO
X_new = np.array([[5, 2.9, 1, 0.2]])
print(f' X_new shape: {X_new.shape}')

# PREDIZENDO VALORES
prediction = kmn.predict(X_new)
print(prediction)
print(iris['target_names'][prediction])  # RESULTADO

#ACURACIA DO MODELO DE ML
final = kmn.score(X_test, y_test)
print(f' Acurácia do Modelo KNeighbors:  {final}')
