import cv2  
# read image  
img = cv2.imread("chick.png")  
      
# height, width, number of channels in image
dimensions = img.shape
height = img.shape[0]  
width = img.shape[1]  
channels = img.shape[2]  
size1 = img.size  
      
print('Image Dimension    : ',dimensions)  
print('Image Height       : ',height)  
print('Image Width        : ',width)  
print('Number of Channels : ',channels)  
print('Image Size  :', size1)  
