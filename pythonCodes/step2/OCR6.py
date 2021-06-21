'''
    Inversão de Cores
    recomendada em casos de casos que a imagem possui texto branco com fundo preto
'''

import cv2

img = cv2.imread('../../Util/Imagens/img-process.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert = 255 - gray

cv2.imshow("image", invert)
cv2.waitKey(0)