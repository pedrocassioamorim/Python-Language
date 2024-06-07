import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 10, 100)
y1 = x1 ** 3

fig1 = plt.figure(figsize = (6,5))
axes1 = fig1.add_axes([0,0,1,1])
axes1.set_xlabel('Eixo X')
axes1.set_ylabel('Eixo Y')
axes1.set_title('Gráfico 1')
axes1.plot(x1,y1, label = 'X ^ 3')
axes1.plot(-x1, y1, label = '-X ^ 3')
axes1.legend(loc = 'upper right')

axes2 = fig1.add_axes([0.35,0.45,0.35,0.35])
axes2.set_title('Zoom gráfico 1')
axes2.plot(x1,y1,
           color = 'blue',
           label = 'X ^ 3',
           ls = 'dashdot',
           lw = 2,
           marker = 'o',
           markerfacecolor = 'y',
           markersize = 7,
           markeredgecolor = 'r',
           markeredgewidth = 2)

axes2.plot(-x1, y1,
           color = 'blue',
           ls = 'dashdot',
           lw = 2,
           marker = 'o',
           markerfacecolor = 'y',
           markersize = 7,
           markeredgecolor = 'r',
           markeredgewidth = 2)

axes2.axis([-3, 3, -1, 15]) #Delimita os limites do gráfico
axes2.grid(True, color = '0.7', dashes = (5,2)) #Habilita a grade
axes2.set_facecolor('lightcyan') #Define a cor de fundo

plt.show()