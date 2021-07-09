import cv2
import pytesseract

url = "http://192.168.1.27:8080/video"


def ocrLeitura(image):
    img = image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    val, tresh = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)

    invert = 255 - tresh

    config_tesseract = "--psm 6"

    texto = pytesseract.image_to_string(image, lang="por", config=config_tesseract)
    print('-> ', texto)



cap = cv2.VideoCapture(url)

while(True):
    ret, frame = cap.read()
    if frame is not None:
        cv2.imshow('frame',frame)
        ocrLeitura(frame)
    q = cv2.waitKey(0)
    if q == ord("q"):
        break

cv2.destroyAllWindows()