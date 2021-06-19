import pytesseract
import numpy as np
import cv2

img = cv2.imread('../Util/Imagens/trecho-livro.jpg')
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#tesseract --help-extra (executar o comando no cmd)
config_tesseract = "--psm 6"
texto = pytesseract.image_to_string(img, lang="por", config=config_tesseract)

print(texto)
cv2.imshow("Image",rgb)
cv2.waitKey(0)

