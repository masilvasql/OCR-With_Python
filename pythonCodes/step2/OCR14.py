'''
    Exercício
'''

import cv2
import pytesseract

img = cv2.imread('../../Util/Imagens/exer1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

invert = 255 - gray


config_tesseract = "--psm 6"

texto = pytesseract.image_to_string(invert, lang="por", config=config_tesseract)
print(texto)

cv2.imshow("IMG", invert)
cv2.waitKey(0)