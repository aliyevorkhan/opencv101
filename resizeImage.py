import cv2

img = cv2.imread("chick.png")
cv2.imshow("orginal image", img)

print("orginal image dimensions: ", img.shape)

img = cv2.resize(img,(150,100))
cv2.imshow("resized image", img)

print("resized image dimensions: ", img.shape)



