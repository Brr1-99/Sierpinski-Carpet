import matplotlib.pyplot as plt
import numpy as np
import math


def Sierpinski(n: int, mapa: str) -> np.ndarray:
    p1 = []
    puntoscentrales = []
    centro = [(int(3**n/2), int(3**n/2))]
    puntoscentrales.append(centro)
    for i in range(1, n):
        nuevosPuntos = []
        for x in range(0, 3**n):
            for y in range(0, 3**n):
                for j in range(0, 8 ** (i-1)):
                    if (x-int(puntoscentrales[i-1][j][0]))**2+(y-int(puntoscentrales[i-1][j][1]))**2 == 2*((3**(n-i))**2)\
                            or (abs(x-int(puntoscentrales[i-1][j][0])) == 3**(n-i) and abs(y-int(puntoscentrales[i-1][j][1])) == 0)\
                            or (abs(x-int(puntoscentrales[i-1][j][0])) == 0 and abs(y-int(puntoscentrales[i-1][j][1])) == 3**(n-i)):
                        nuevosPuntos.append((x, y))
                        p1.append((x, y))
        puntoscentrales.append(nuevosPuntos)
    print(puntoscentrales)
    relleno = []
    for k in range(0, n):
        for x1 in range(0, 3**n+1):
            for y1 in range(0, 3**n+1):
                for j1 in range(0, 8 ** k):
                    if abs(x1-int(puntoscentrales[k][j1][0])) <= (int(3**(n-k-1)/2)) and abs(y1-int(puntoscentrales[k][j1][1])) <= (int(3**(n-k-1)/2)):
                        relleno.append((x1, y1))

    t = p1 + relleno + centro

    X = np.array([[0 for e in range(3**n+1)] for f in range(3**n+1)], dtype=float)
    valor = 0
    for e in range(3**n):
        for f in range(3**n):
            X[e][f] = valor
        valor = valor + 1
    Y = X.T
    u = np.array([[0 for i in range(3**n+1)] for j in range(3**n+1)], dtype=float)
    for dato in t:
        for i in range(3**n):
            if i == dato[0]:
                for j in range(3**n):
                    if j == dato[1]:
                        u[i][j] = 1
    dimension = [2000, 669, 96, 13, 5]

    plt.clf()
    plt.close()
    size = dimension[n-1]
    size = math.ceil(size)
    cm = plt.cm.get_cmap(mapa)
    plt.scatter(X, Y, c=u, s=size, cmap=cm, marker=u's', linewidths=0)
    plt.ylim(ymax=3**n+1, ymin=-1)
    plt.xlim(xmax=3**n+1, xmin=-1)
    plt.colorbar()
    plt.title('Sierpinski ' + str(n) + ' iteraciones')
    plt.show()
    return [u]


print(Sierpinski(2, 'binary'))

