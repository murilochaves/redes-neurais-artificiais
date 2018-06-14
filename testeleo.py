matriz = [
    [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
    [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6],
    [2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6],
    [3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6],
    [4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 0.6],
    [5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6],
    [6.0, 6.1, 6.2, 6.3, 6.4, 6.5, 6.6]
]
class Topologia:
    def __init__(self, matriz):
        self.m = matriz
        self.lx = len(matriz)
        self.ly = len(matriz[0])

      

    def hexagonal(self, x, y , R=1):
        lista = []

        if (x-R) >= 0 and (y-R) >= 0:
            lista.append(self.m[x-R][y-R])
        if (x-R) >= 0:
            lista.append(self.m[x-R][y])
        if (y-R) >=0 :
            lista.append(self.m[x][y-R])
        if (y+R) < self.ly:
            lista.append(self.m[x][y+R])
        if (x+R) < self.lx and (y-R) >=0:
            lista.append(self.m[x+R][y-R])
        if (x+R) < self.lx:
            lista.append(self.m[x+R][y])

        return lista

top = Topologia(matriz)

print(top.hexagonal(3,  3, 2))
