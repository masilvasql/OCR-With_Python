'''
    Desfoque passa baixa
'''

import cv2
import matplotlib.pyplot as plt

img = cv2.imread('../../Util/Imagens/ruido1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

desfoque_media = cv2.blur(gray, (5,5))

desfoque_gausiano = cv2.GaussianBlur(gray, (5,5), 0)

desfoque_mediana = cv2.medianBlur(gray, 3)

desfoque_bilateral = cv2.bilateralFilter(gray, 15, 55, 45)


cv2.imshow("img", desfoque_mediana)
cv2.waitKey(0)
