import numpy as np
import cv2
from pytesser import *
 
im = cv2.imread('text-sample-1.jpg')

imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, cv2.THRESH_BINARY_INV)
# ret,thresh = cv2.threshold(imgray,127,255,0)

# kernel = np.ones((3,3),np.uint8)
# erosion = cv2.erode(thresh,kernel,iterations = 1)

# contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
# cnt = contours[0]
# cv2.drawContours(im,contours,-1,(0,255,0),3)

new_width, new_height = im.shape[1]/4, im.shape[0]/4
image_resized = cv2.resize(thresh, (new_width, new_height))
cv2.imshow('houghlines',image_resized)

ok = raw_input()
cv2.destroyAllWindows()

image_pil = Image.fromarray(thresh)
print image_to_string(image_pil)
