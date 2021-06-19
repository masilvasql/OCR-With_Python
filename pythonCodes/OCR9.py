#Seleção de Textos
import numpy as np
import pytesseract
from pytesseract import Output
import cv2
import re #expressão regular
from PIL import ImageFont, Image, ImageDraw

image = cv2.imread("../Util/Imagens/tabela_teste.jpg")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
resultado = pytesseract.image_to_data(rgb, lang='por', output_type=Output.DICT) #DICT = Dicionário
# https://regexr.com/
padrao_data = '^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[012])/(19|20)\d\d$'

img_copia = rgb.copy()

min_conf = 40

fonte_dir = '../Util/Fontes/calibri.ttf'

def escreve_texto(texto, x, y, img, fonte, tamanho_texto=32):
  fonte = ImageFont.truetype(fonte, tamanho_texto)

  # convertendo formato nampy para formato do PIL
  img_pil = Image.fromarray(img)
  draw = ImageDraw.Draw(img_pil)
  draw.text((x, y - tamanho_texto), texto, font=fonte)
  img = np.array(img_pil)
  return img

def caixa_texto(resultado, img, cor=(255, 100, 0)):
    x = resultado['left'][i]
    y = resultado['top'][i]
    w = resultado['width'][i]
    h = resultado['height'][i]

    cv2.rectangle(img, (x, y), (x + w, y + h), cor, 2)

    return x, y, img

datas = []
for i in range(0, len(resultado['text'])):
  confianca = int(resultado['conf'][i])
  if confianca > min_conf:
    texto = resultado['text'][i]
    if re.match(padrao_data, texto):
      x, y, img = caixa_texto(resultado, img_copia, (0,0,255))
      img_copia = escreve_texto(texto, x, y, img_copia, fonte_dir, 12)
      datas.append(texto)
    else:
      x, y, img_copia = caixa_texto(resultado, img_copia)

cv2.imshow("imagem",img_copia)
cv2.waitKey(0)


