#Seleção de Textos
import pytesseract
from pytesseract import Output
import cv2
import matplotlib.pyplot as plt

image = cv2.imread("../../Util/Imagens/teste_manuscrito_01.jpg")
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# config_tesseract = "--psm "
resultado = pytesseract.image_to_data(rgb, lang='por', output_type=Output.DICT) #DICT = Dicionário
print(resultado)

min_conf = 35 #confiança mínima da detecção das palavras

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
        cv2.putText(img_copia, texto,(x,y - 10) ,cv2.FONT_HERSHEY_PLAIN, 1.1, (0,0,255))

cv2.imshow("Imagem",img_copia)
cv2.waitKey(0)


