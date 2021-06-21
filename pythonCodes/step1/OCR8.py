#Seleção de Textos
import numpy as np
import pytesseract
from pytesseract import Output
import cv2
import matplotlib.pyplot as plt
from PIL import ImageFont, Image, ImageDraw

font_dir = '../../Util/Fontes/calibri.ttf'

image = cv2.imread("../../Util/Imagens/teste02.jpg")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
resultado = pytesseract.image_to_data(rgb, lang='por', output_type=Output.DICT) #DICT = Dicionário
print(resultado)

min_conf = 35 #confiança mínima da detecção das palavras

def escreve_texto(texto, x, y, img, fonte, tamanho_texto = 32):
    fonte = ImageFont.truetype(fonte, tamanho_texto)

    #convertendo formato nampy para formato do PIL
    img_pil = Image.fromarray(img)
    draw = ImageDraw.Draw(img_pil)
    draw.text((x,y - tamanho_texto), texto , font=fonte)
    img = np.array(img_pil)
    return img
def caixa_texto(resultado, img, cor = (255, 100,0)):
    x = resultado['left'][i]
    y = resultado['top'][i]
    w = resultado['width'][i]
    h = resultado['height'][i]

    cv2.rectangle(img, (x,y), (x + w,y + h), cor, 2)

    return x,y,img

img_copia = rgb.copy()

for i in range(0, len(resultado['text'])):
    confianca = int(resultado['conf'][i])
    if confianca > min_conf:
        x,y, img = caixa_texto(resultado, img_copia)
        texto = resultado['text'][i]
        img_copia = escreve_texto(texto, x, y, img_copia, font_dir)

cv2.imshow("Imagem",img_copia)
cv2.waitKey(0)


