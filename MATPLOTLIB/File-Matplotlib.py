import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 10, 100) #Cria 100 valores de 0 a 10
y1 = x1**3
plt.plot(x1, y1) #Gera o gráfico
plt.title('Titulo do Gráfico') #Adiciona um título no gráfico
plt.xlabel('Eixo X') #Adiciona um titulo ao Eixo X
plt.ylabel('Eixo Y') #Adiciona um titulo ao Eixo Y
plt.show() #Mostra o gráfico

plt.subplot(2,2,1)
plt.plot(x1, y1, 'r') # r = red
plt.title('Subplot 2,2,1')
plt.xlabel('Eixo X 1')
plt.ylabel('Eixo Y 1')

plt.subplot(2,2,2)
plt.plot(- x1, y1, 'b') # b = blue
plt.title('Subplot 2,2,2')
plt.xlabel('Eixo X 2')
plt.ylabel('Eixo Y 2')

plt.subplot(2,2,3)
plt.plot(x1, - y1, 'y') # y = yellow
plt.title('Subplot 2,2,3')
plt.xlabel('Eixo X 3')
plt.ylabel('Eixo Y 3')

plt.subplot(2,2,4)
plt.plot(- x1, - y1, 'g')
plt.title('Subplot 2,2,4')
plt.xlabel('Eixo X 4')
plt.ylabel('Eixo Y 4')

plt.tight_layout() # Organiza os Subplots dentro da figura
plt.show()