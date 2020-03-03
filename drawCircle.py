import cv2

img = cv2.imread("chick.png")

cv2.circle(img,(80,80), 55, (0,255,0), 1) #if we change the parameter 1 with -1 what will happen
cv2.imshow('image',img)  


