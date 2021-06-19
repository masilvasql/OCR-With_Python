import pytesseract
import numpy as np
import cv2

img = cv2.imread('C:\marcelo\python\OCR com Python\meus/1874ac2211ecb85903dac2293e720c2b.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

texto = pytesseract.image_to_string(rgb)

print(texto)

cv2.imshow("image", rgb)
cv2.waitKey(0)
