# Importar librerias
import numpy as np
import matplotlib.pyplot as plt
import pygame
# Tablero aleatorio de 0 ( muerto) y 1 ( vivo)
xc = 30
yc = 30
# Donde a = estado.
a = np.zeros((xc,yc))

# Sembrar estados
a[11, 11] = 1
a[12, 12] = 1
a[12, 13] = 1
a[11, 13] = 1
a[10, 13] = 1
plt.matshow(a)
plt.show()

while 1:
    new_a = np.copy(a)

    for i in range(0, (xc-1)):
        for j in range(0, (yc-1)):

            # center, top and down
            vecinos = a[i-1, j], a[i, (j-1)], a[i, (j+1)], \
                    a[(i-1), (j-1)], a[(i-1), (j+1)],\
                    a[(i+1), (j-1)], a[(i+1), j], a[(i+1), (j+1)]
            # una celula muerta con exactamente 3 celulas vecinas vivas "NACE"
            if a[i, j] == 0 and np.sum(vecinos) == 3:
                new_a[i, j] = 1
            # una celula viva con 2 o 3 celulas vecinas vivas siguue vivo, en otro caso muere
            elif a[i, j] == 1 and (np.sum(vecinos) < 2 or np.sum(vecinos) > 3):
                new_a[i, j] = 0
    a = new_a
    plt.matshow(a)
    plt.title('Game of Life')
    plt.show()