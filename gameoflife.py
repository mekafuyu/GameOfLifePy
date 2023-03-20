from time import sleep
import copy
import os

AOREDOR = [
    [-1,-1],
    [-1, 0],
    [-1, 1],
    [ 0,-1],
    [ 0, 1],
    [ 1,-1],
    [ 1, 0],
    [ 1, 1]]

matriz = []

for i in range(50):
    linha = []
    for j in range(50):
        linha.append(0)
    matriz.append(linha)

matriz[2][3],matriz[3][4],matriz[4][2],matriz[4][3], matriz[4][4] = 1,1,1,1,1
#matriz[6][6],matriz[5][7],matriz[6][7],matriz[7][7],matriz[4][8],matriz[6][8],matriz[8][8],matriz[4][9],matriz[6][9],matriz[8][9],matriz[5][10],matriz[6][10],matriz[7][10],matriz[6][11] = 1,1,1,1,1,1,1,1,1,1,1,1,1,1
#matriz[6][14],matriz[5][15],matriz[6][15],matriz[7][15],matriz[4][16],matriz[6][16],matriz[8][16],matriz[4][17],matriz[6][17],matriz[8][17],matriz[5][18],matriz[6][18],matriz[7][18],matriz[6][19] = 1,1,1,1,1,1,1,1,1,1,1,1,1,1
#matriz[2][2],matriz[2][3],matriz[3][2],matriz[3][3] = 1,1,1,1

def mostraxadrez(matrizant):
    matriztxt = ""

    matriznova = copy.deepcopy(matrizant)
    for x in range(len(matrizant)):
        for y in range(len(matrizant[x])):
            vivos = 0

            if not (x == 0 or y == 0 or x == (len(matrizant[x])-1) or y == (len(matrizant)-1)):
                for i in AOREDOR:
                    if matrizant[x-i[0]][y-i[1]] == 1:
                        vivos+=1

            if vivos > 3 or vivos < 2:
                matriznova[x][y] = 0
            elif matrizant[x][y] == 0 and vivos ==3:
                matriznova[x][y] = 1

            if  matrizant[x][y] == 0:
                matriztxt += "⬛ "
            else:
                matriztxt += "⬜ "
        matriztxt += "\n"
    print(matriztxt)
    return matriznova

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    matriz = mostraxadrez(matriz)
    #sleep(0.1)