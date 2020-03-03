import cv2

font = cv2.FONT_HERSHEY_SIMPLEX

img = cv2.imread("chick.png")

img = cv2.putText(img,'I learn OpenCV',(50,45), font, 1,(0,255,255),2)

cv2.imshow("image",img)  


