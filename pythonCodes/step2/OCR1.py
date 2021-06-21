'''
Pré processamento de imagens
convertendo para a escala de cinza
'''


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("../../Util/Imagens/img-process.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Imagem",gray)
cv2.waitKey(0)