'''
Limiarização Simples (Thresholding)
Na limiarização é essencial fazer a conversão para a escala de cinza
'''

import cv2

img = cv2.imread('../../Util/part2.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

'''
    imagem, 
    valor do trash (127, meio da escala entre cinza e preto
    valor máximo = valor que os pixels à cima do limiar vão receber
    
    Caso os pixels tenham o valor maior q 127, automaticamente serão 255
    
    tipo de algoritmo = THRESH_BINARY (binarização simples)
'''
val, thresh = cv2.threshold(gray, 140, 255, cv2.THRESH_BINARY)

cv2.imshow("img",thresh)
cv2.waitKey(0)