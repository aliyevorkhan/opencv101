import cv2
import numpy as np
img = cv2.imread("chick.png")

pts = np.array([[10,50],[20,30],[70,20],[50,10]], np.int32)

cv2.polylines(img, [pts], True, (0,255,255), 3)
cv2.imshow('image',img)  

