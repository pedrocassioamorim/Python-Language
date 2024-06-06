import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 10, 100)
y1 = x1 ** 3

fig1 = plt.figure(figsize = (6,5))
axes1 = fig1.add_axes([0,0,1,1])
axes1.set_xlabel('Eixo X de FIG1')
axes1.set_ylabel('Eixo Y de FIG1')
axes1.set_title('Gráfico de FIG1')
axes1.plot(x1, y1, label = 'X^3')
axes1.plot(- x1, y1, label = '- X^3')
axes1.legend(loc = 0)
# Define a posição da legenda
# loc = 0: automatico,
# loc = 1: direita superior,
# loc = 2: esquerda superior,
# loc = 3: esquerda inferior; e
# loc = 4: direita inferior.

axes2 = fig1.add_axes([0.325,0.45,0.35,0.35])
axes2.set_title("Zoom Gráfico 1")
axes2.plot(x1, y1, 'X')
axes2.plot(- x1, y1, 'X')
axes2.axis([-3, 3, -1, 10])

plt.show()