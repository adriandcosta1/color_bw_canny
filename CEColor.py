import cv2
import cv
import numpy as np
import matplotlib.image as mpimg
from matplotlib import pyplot as plt

cam = cv2.VideoCapture(0)
cv2.namedWindow("test")

img_counter = 0

while True:
    ret, color = cam.read()
    
    edges = cv2.Canny(color, 50,500)
    gray = cv2.cvtColor(color,cv2.COLOR_RGB2GRAY)
    grey_3_channel = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
    edges_3_channel = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
    #blank_image = np.zeros((color.height*3,color.width*3,3), np.uint8)
    
       
    horiz = np.hstack((color, grey_3_channel,edges_3_channel))
    
    cv2.imshow('HORIZONTAL', horiz)
    
    if not ret:
        break
    k = cv2.waitKey(1)

    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    
        
cam.release()

cv2.destroyAllWindows()
   
        
       
    
    
    
