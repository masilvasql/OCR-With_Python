import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

class Util:

    def write_text(texto, x, y, img, fonte, text_size = 32):
        font= ImageFont.truetype(fonte, text_size)
        #convertendo imagem para formato do numpy
        img_pil =Image.fromarray(img)
        draw =ImageDraw.Draw(img_pil)
        draw.text((x, y - text_size), texto, font=font)
        #converte novamente para imagem NumPy
        img =np.array(img_pil)
        return  img

    def draw_text_box(resultado, img, position ,cor = (255,100,0)):
        left = resultado['left'][position]
        top = resultado['top'][position]
        width = resultado['width'][position]
        height = resultado['height'][position]

        cv2.rectangle(img ,(left, top), (left + width, top + height), cor, 3)

        return left, top, img

    def findWordsOnImage(resultado, confianca_minima, img_original, fonte, escrever_texto):
        img_copia = img_original.copy()

        for i in range(0, len(resultado['text'])):
            confianca = int(resultado['conf'][i])
            if(confianca >= confianca_minima):
                left, top, img = Util.draw_text_box(resultado, img_copia, i)
                texto = resultado['text'][i]
                if escrever_texto:
                    img_copia = Util.write_text(texto, left, top ,img_copia, fonte)
        return img_copia


