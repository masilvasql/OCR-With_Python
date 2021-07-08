'''
    Limiarização adaptativa (utilizando média),
    Calcula diferente tipos de limiares para partes da imagem
'''

import cv2
from pdf2image import convert_from_path,convert_from_bytes

import os
basePath = os.path.dirname(os.path.realpath(__file__))
pdf_file_path = os.path.join(basePath, "../../meus/THE ENTERTAINER.pdf")
images = convert_from_path(pdf_file_path)
'''for page in pages:
    cont += cont
    page.save('out'+cont+'.jpg', 'JPEG')'''

# img = cv2.imread('C:/Users/marcelo.silva/Downloads/THE%20ENTERTAINER.pdf')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# adapt_media = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21,21)

# val, otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#print(val)

# cv2.imshow("img",img)
# cv2.waitKey(0)