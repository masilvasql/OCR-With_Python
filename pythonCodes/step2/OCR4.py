'''
    Limiarização adaptativa (utilizando média),
    Calcula diferente tipos de limiares para partes da imagem
'''

import cv2

img = cv2.imread('../../Util/Imagens/livro02.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adapt_media = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11,9)

#val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#print(val)

cv2.imshow("img",adapt_media)
cv2.waitKey(0)