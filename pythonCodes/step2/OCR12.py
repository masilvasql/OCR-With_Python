'''
    Desfoque passa baixa
    Detecção de texto
'''

import cv2
import matplotlib.pyplot as plt
import pytesseract

img = cv2.imread('../../Util/Imagens/teste_ruido.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

desfoque_media = cv2.blur(gray, (5,5))

desfoque_gausiano = cv2.GaussianBlur(gray, (5,5), 0)

desfoque_mediana = cv2.medianBlur(gray, 3)

desfoque_bilateral = cv2.bilateralFilter(gray, 15, 55, 45)

config_tesseract = "--psm 8"
texto = pytesseract.image_to_string(desfoque_bilateral, lang="por", config=config_tesseract)
print(texto)



