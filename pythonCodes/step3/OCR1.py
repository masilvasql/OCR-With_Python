'''
    EAST + Tesseract

    Processamento de imagens

    Arquitetura east suporta apenas imagens com dimensões múltipas de 32
'''


import cv2
import numpy as np
from imutils.object_detection import non_max_suppression

detector = '../../Util/modelos/frozen_east_text_detection.pb'
largura, altura = 320, 320
imagem = '../../Util/imagens/caneca.jpg'
min_confianca = 0.9


img = cv2.imread(imagem)
original = img.copy()
print(img.shape)

H = img.shape[0]
W = img.shape[1]

proporcao_w = W / float(largura)
proporcao_h = H / float(altura)
print(proporcao_w, proporcao_h)

img = cv2.resize(img, (largura, altura))
H = img.shape[0]
W = img.shape[1]
print(H, W)

nomes_camadas = ['feature_fusion/Conv_7/Sigmoid', 'feature_fusion/concat_3']


rede_neural = cv2.dnn.readNet(detector)

blob = cv2.dnn.blobFromImage(img, 1.0, (W,H), swapRB=True, crop=False)

print(blob.shape) #batch_size

rede_neural.setInput(blob)
scores, geometry = rede_neural.forward(nomes_camadas)
print('SCORES => ', scores)

print('Geometry =>', geometry)

print("scores.shape", scores.shape)
print("geometry.shape", geometry.shape)

linhas, colunas = scores.shape[2:4]
print(linhas, colunas)

caixas = []
confiancas = []
'''
def dados_geometricos(geometry, y):
    xData0 = geometry[0, 0, y]
    xData1 = geometry[0, 1, y]
    xData2 = geometry[0, 2, y]
    xData3 = geometry[0, 3, y]
    data_angulos = geometry[0, 4, y]
    return data_angulos, xData0, xData1, xData2, xData3

def calculos_geometria(data_angulos, xData0, xData1, xData2, xData3):
    (offesetX, offsetY) = (x * 4.0, y * 4.0)
    angulo = data_angulos[x]
    cos = np.cos(angulo)
    sin = np.sin(angulo)
    h = xData0[x] + xData2[x]
    w = xData1[x] + xData3[x]

    fimX = int(offesetX + (cos * xData1[x]) + (sin() * xData2[x]))
    fimY = int(offesetY - (sin * xData1[x]) + (sin() * xData2[x]))
    inicioX = int(fimX - w)
    inicioY = int(fimY - h)

    return inicioX, inicioY, fimX, fimY'''




cv2.imshow("imagem",img)
cv2.waitKey(0)