import sys, os
import cv2
import numpy as np

# Hack to use modules in parent folder
sys.path.append('..')
from general_functions import *

def cut_text_box(image_file_path):
    image = cv2.imread(image_file_path)

    image_split = cv2.split(image)
    flag, b = cv2.threshold(image_split[2], 0, 255, cv2.THRESH_OTSU) 

    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (1, 1))
    cv2.erode(b, element)

    edges = cv2.Canny(b, 150, 200, 3, 5)

    lines = cv2.HoughLinesP(edges, 1, np.pi/2, 2, minLineLength = 800, maxLineGap = 50)[0]

    img = image.copy()

    x_min = 3000
    x_max = 0
    y_min = 3000
    y_max = 0

    for x1, y1, x2, y2 in lines:
        cv2.line(img, (x1,y1), (x2,y2), (0,255,0), 1)
        if x1 < x_min:
            x_min = x1
        if x2 > x_max:
            x_max = x2
        if y1 < y_min:
            y_min = y1
        if y2 > y_max:
            y_max = y2

    print x_min, x_max, y_min, y_max

    print 'Showing image with green lines'
    show_image_in_window(img)

    # img[y: y + h, x: x + w]
    img = image[y_min-50:y_max, x_min:x_max+50]

    print 'Showing cropped image'
    show_image_in_window(img)

    gray_image_array = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, img = cv2.threshold(gray_image_array, 127, 255, cv2.THRESH_BINARY_INV)

    print 'Showing binary image'
    show_image_in_window(img)

    print get_text_from_image(img)


def main():
    if len(sys.argv) > 1:
        image_file_path = sys.argv[1]
        if os.path.isfile(image_file_path):
            cut_text_box(image_file_path)
        else:
            print 'Image file does not exist'
    else:
        print 'First parameter must be an image file name'

if __name__ == '__main__':
    main()
