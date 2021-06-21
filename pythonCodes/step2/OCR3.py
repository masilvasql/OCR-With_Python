'''
    Método de Otsu
    faz o uso de um limiar global, mas de forma automática utilizando histogramas
'''

import cv2

img = cv2.imread('../../Util/Imagens/receita01.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

print(val)

cv2.imshow("IMG", otsu)
cv2.waitKey(0)