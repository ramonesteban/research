import cv2
import numpy as np
from image_filters import *

image = cv2.imread('text-sample-1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_split = cv2.split(image)
flag,b = cv2.threshold(image_split[2], 0, 255, cv2.THRESH_OTSU) 

element = cv2.getStructuringElement(cv2.MORPH_CROSS, (1,1))
cv2.erode(b, element)

edges = cv2.Canny(b, 150, 200, 3, 5)

lines = cv2.HoughLinesP(edges, 1, np.pi/2, 2, minLineLength = 620, maxLineGap = 50)[0]

img = image.copy()

for x1, y1, x2, y2 in lines:
    cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 1)

# img = cv2.imread('text-sample-2.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
# minLineLength = 200
# maxLineGap = 10
# lines = cv2.HoughLinesP(edges,1,np.pi/180,10,minLineLength,maxLineGap)
# for x1,y1,x2,y2 in lines[0]:
#     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

show_image_in_window(img)
