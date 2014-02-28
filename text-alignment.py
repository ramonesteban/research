import cv2
import numpy as np

im = cv2.imread('text-sample-1.jpg')
gray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)

imgSplit = cv2.split(im)
flag,b = cv2.threshold(imgSplit[2],0,255,cv2.THRESH_OTSU) 

element = cv2.getStructuringElement(cv2.MORPH_CROSS,(1,1))
cv2.erode(b,element)

edges = cv2.Canny(b,150,200,3,5)

img = im.copy()

lines = cv2.HoughLinesP(edges,1,np.pi/2,2, minLineLength = 620, maxLineGap = 50)[0]

for x1,y1,x2,y2 in lines:        
    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)

new_width, new_height = img.shape[1]/4, img.shape[0]/4
image_resized = cv2.resize(img, (new_width, new_height))
cv2.imshow('lines',image_resized)


# img = cv2.imread('text-sample-2.jpg')
# gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# edges = cv2.Canny(gray,50,150,apertureSize = 3)
# minLineLength = 200
# maxLineGap = 10
# lines = cv2.HoughLinesP(edges,1,np.pi/180,10,minLineLength,maxLineGap)
# for x1,y1,x2,y2 in lines[0]:
#     cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)

ok = raw_input()
cv2.destroyAllWindows()
