import cv2

img = cv2.imread("chick.png")
cv2.ellipse(img, (250, 150), (80, 20), 5, 0, 360, (0,0,255), -1)
cv2.imshow('image',img)  


