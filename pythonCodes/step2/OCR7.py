'''

Redimensionamento de imagens
'''
import cv2

img = cv2.imread('../../Util/Imagens/img-process.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert = 255 - gray

maior = cv2.resize(gray, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_CUBIC)

menor = cv2.resize(gray, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow("image", menor)
cv2.waitKey(0)

