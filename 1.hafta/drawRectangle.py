import cv2

img = cv2.imread("chick.png")

cv2.rectangle(img,(15,25),(200,150),(0,255,255),10)
cv2.imshow('image',img)  


