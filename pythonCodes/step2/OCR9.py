'''
Operações morfológicas
Erosão
Dilatação
Abertura
Fechamento
'''

import cv2
import numpy as np

img = cv2.imread('../../Util/part1.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

erosao = cv2.erode(gray, np.ones((3,3),np.uint8))

dilatacao = cv2.dilate(gray, np.ones((3,3), np.uint8))

erosao2 = cv2.erode(gray, np.ones((5,5),np.uint8))

'Abertura é a erosão + dilatação'
abertura = cv2.dilate(erosao2, np.ones((5,5), np.uint8))


'Fechamento - Dialtação + erosão'
img2 = cv2.imread('../../Util/Imagens/texto-opencv2.jpg')
gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)


dilatacao2 = cv2.dilate(gray, np.ones((5,5)))
Fechamento = cv2.erode(dilatacao2, np.ones((5,5)))


cv2.imshow("img", erosao)
cv2.waitKey(0)