import matplotlib.pyplot as plt
import numpy as np

list1 = ['Domingo', 'Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Média']
list2 = []

for i in range (len(list1) - 1):
    total = 0
    for i in range(5):
        num1 = np.random.randint(100)
        total += num1
    list2.append(total)
media = sum(list2) / len(list1)
list2.append(media)

plt.bar(list1, list2)
plt.title('Numero de Mosquitos na minha casa')
plt.xlabel('Dias da Semana')
plt.ylabel('Numero de Mosquitos')
plt.tight_layout
plt.show()