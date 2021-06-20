import numpy as np
from pytesseract import Output, pytesseract
import cv2
from PIL import  Image
from Util import Util
import matplotlib.pyplot as plt

#importação de fontes para garantir melhores resultados
font_dir = '../../Util/Fontes/calibri.ttf'

image = cv2.imread('../../meus/img2.png')
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#dicionário de dados coletados da imagem
resultado = pytesseract.image_to_data(rgb, lang='por', output_type= Output.DICT)
print(resultado)

#Mínimo de confiança ao encontrar as palavras
min_conf = 60

escreve_texto = False

final_image = Util.findWordsOnImage(resultado,min_conf, rgb, font_dir, escreve_texto)

im = final_image

plt.imshow(im)
plt.show()

# cv2.imshow("Imagem",final_image)
# cv2.waitKey(0)


