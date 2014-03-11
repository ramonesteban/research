import sys, os
import difflib
import re

from general_functions import *

def similarity_test(image_array, text_file_path):
    image_text = get_text_from_image(image_array)

    file_text = open(text_file_path, 'r')
    plain_text = file_text.read()

    similarity = difflib.SequenceMatcher(None, plain_text, image_text).ratio()
    print '### Similarity Ratio ###'
    print similarity

def accuaracy_test(image_file_path):
    image = cv2.imread(image_file_path)
    gray_image_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ret, thresh = cv2.threshold(gray_image_array, 127, 255, 0)
    kernel = np.ones((5,5), np.uint8)
    erosion = cv2.erode(thresh, kernel, iterations = 1)

    show_image_in_window(thresh)

    image_text = get_text_from_image(thresh)

    file_text = open('text.txt', 'r')
    plain_text = file_text.read()

    similarity = difflib.SequenceMatcher(None, plain_text, image_text).ratio()
    print similarity

def main():
    if len(sys.argv) > 1:
        image_file_path = sys.argv[1]
        if os.path.isfile(image_file_path):
            accuaracy_test(image_file_path)
        else:
            print 'Image file does not exist'
    else:
        print 'First parameter must be an image file name'

if __name__ == '__main__':
    main()
