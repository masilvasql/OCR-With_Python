'''
   Extração de textos com PyTesseract
'''
import pytesseract
import cv2

#Efetua a leitura com o CV2
img = cv2.imread('../../meus/img1.jpg')

#converte a imagem para RGB pois o padrão de leitura é BGR
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#extração do texto
tesseract_config = "--psm 7"
texto = pytesseract.image_to_string(img, lang="por")

print(texto)

cv2.imshow("Imagem",rgb)
cv2.waitKey(0)
