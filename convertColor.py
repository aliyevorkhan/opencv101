# importing cv2    
import cv2    
         
# path of the input image  
path = ("chick.png")  
         
# Reading an image in default mode   
src = cv2.imread(path)   
         
# Window name in which image is displayed   
window_name = 'Image'   
# Using cv2.cvtColor() method   
# Using cv2.COLOR_BGR2GRAY color space for convert BGR image to grayscale  
# conversion code   
image = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY )   
# Displaying the image    
cv2.imshow(window_name, image)  


