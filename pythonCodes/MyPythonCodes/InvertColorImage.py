import cv2

img = cv2.imread('../../meus/paisagem1.jpg')

new = 35 - img
cv2.imshow("img",new)
cv2.waitKey(0)