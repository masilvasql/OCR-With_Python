import pytesseract
import cv2
import numpy as np

img = cv2.imread('../../meus/1874ac2211ecb85903dac2293e720c2b.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# print(pytesseract.get_languages(config=''))

texto = pytesseract.image_to_string(rgb, lang='por')

print(texto)

cv2.imshow("image", rgb)
cv2.waitKey(0)
