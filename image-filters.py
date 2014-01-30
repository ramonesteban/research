import sys, os, cv2, Image
import numpy as np
from pytesser import *

def show_image_in_window(image_array):
    new_width, new_height = image_array.shape[1]/4, image_array.shape[0]/4
    image_resized = cv2.resize(image_array, (new_width, new_height))

    cv2.imshow('test', image_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def get_text_from_image(image_array):
    image_pil = Image.fromarray(image_array)
    text = image_to_string(image_pil)
    return text

def show_pil_image(image_pil):
    image_pil.show()

def threshold(method, gray_image_array):
    if method == 'binary_inverted':
        # Binary inverted thresholding
        ret, image_thresholded = cv2.threshold(gray_image_array, 127, 255, cv2.THRESH_BINARY_INV)
        return image_thresholded
    elif method == 'binary':
        # Binary thresholding
        ret, image_thresholded = cv2.threshold(gray_image_array, 127, 255, cv2.THRESH_BINARY)
        return image_thresholded
    elif method == 'otsu':
        # Otsu's thresholding
        ret, image_thresholded = cv2.threshold(gray_image_array, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        return image_thresholded
    elif method == 'adaptive':
        image_thresholded = cv2.adaptiveThreshold(gray_image_array, 255, 1, 1, 11, 2)
    else:
        print 'threshold not found'
        return gray_image_array

def blur(method, gray_image_array):
    if method == 'gaussian':
        blur_image_array = cv2.GaussianBlur(gray_image_array, (5, 5), 0)
        return blur_image_array
    elif method == 'median':
        blur_image_array = cv2.medianBlur(gray_image_array, 5)
        return blur_image_array
    else:
        print 'blur not applied'
        return gray_image_array

def test_one(gray_image_array):
    result = threshold('binary_inverted', gray_image_array)
    show_image_in_window(result)
    return result

def test_two(gray_image_array):
    gray_image_array = cv2.GaussianBlur(gray_image_array, (5, 5), 0)
    result = threshold('otsu', gray_image_array)
    show_image_in_window(result)
    return result

def test_three(gray_image_array):
    gray_image_array = blur('median', gray_image_array)
    result = cv2.adaptiveThreshold(gray_image_array, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    show_image_in_window(result)
    return result

def test_four(gray_image_array):
    gray_image_array = blur('median', gray_image_array)
    result = cv2.adaptiveThreshold(gray_image_array, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
    show_image_in_window(result)
    return result

def run_tests(image_file_path, show_text):
    image = cv2.imread(image_file_path)
    gray_image_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    result = test_one(gray_image_array)
    if show_text == True: print get_text_from_image(result)

    result = test_two(gray_image_array)
    if show_text == True: print get_text_from_image(result)

    result = test_three(gray_image_array)
    if show_text == True: print get_text_from_image(result)

    #result = test_four(gray_image_array)
    #if show_text == True: print get_text_from_image(result)

def main():
    if len(sys.argv) > 1:
      image_file_path = sys.argv[1]
      if os.path.isfile(image_file_path):
        try:
            if sys.argv[2] == 'print':
                run_tests(image_file_path, True)
            else:
                run_tests(image_file_path, False)
        except:
            run_tests(image_file_path, False)
      else:
        print 'Image file does not exist'
    else:
      print 'First parameter must be an image file name'

if __name__ == '__main__':
    main()