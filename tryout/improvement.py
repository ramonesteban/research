import sys, os
import cv2
import numpy as np

# Hack to use modules in parent folder
sys.path.append('..')
from pytesser import *
from general_functions import *

def improvement(image_file_path):
    image = cv2.imread(image_file_path)
    gray_image_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray_image_array, 127, 255, 0)
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(thresh, kernel, iterations = 1)

    show_image_in_window(thresh)
    print get_text_from_image(thresh)

def main():
    if len(sys.argv) > 1:
        image_file_path = sys.argv[1]
        if os.path.isfile(image_file_path):
            improvement(image_file_path)
        else:
            print 'Image file does not exist'
    else:
        print 'First parameter must be an image file name'

if __name__ == '__main__':
    main()
