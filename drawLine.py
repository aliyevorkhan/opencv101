import cv2

img = cv2.imread("chick.png")

cv2.line(img,(10,0),(150,150),(255,255,255), 5)
cv2.imshow('image',img)  


