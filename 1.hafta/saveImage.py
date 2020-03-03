import cv2  

# read image as grey scale  
img = cv2.imread("chick.png", 1)  
  
# save image  
status = cv2.imwrite("chick_copy.png", img)  
print("Image written to file-system : ", status) 


