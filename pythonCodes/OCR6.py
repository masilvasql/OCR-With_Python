#com OSD não usar o opencv
'''

OSD possui algumas informações à mais sobre a imagem
como orientação, número da página
Não precisa fazer a tratativa de BGR para RGB
'''
import  pytesseract
import numpy
import cv2
from PIL import Image
import matplotlib.pyplot as plt

img = Image.open('../Util/Imagens/livro01.jpg')

print(pytesseract.image_to_osd(img))

plt.imshow(img)
plt.show()