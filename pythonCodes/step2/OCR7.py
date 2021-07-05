'''

Redimensionamento de imagens
'''
import cv2

img = cv2.imread('../../Util/icon.png')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert = 255 - gray

maior = cv2.resize(gray, None, fx=3.5, fy=3.5, interpolation=cv2.INTER_CUBIC)

menor = cv2.resize(gray, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

cv2.imshow("image", maior)
cv2.waitKey(0)

