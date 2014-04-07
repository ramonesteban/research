import cv2, Image
import numpy as np
from pytesser import *

from image_filters import *
from general_functions import *
from recognition_accuracy import *

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

def run_tests(image_file_path, show_text):
    image = cv2.imread(image_file_path)
    gray_image_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    text_file_path = image_file_path.split('.')[0]
    text_file_path = text_file_path.split('/')[1]
    text_file_path = 'texts/' + text_file_path + '.txt'

    similarity_test(gray_image_array, text_file_path)
    show_image_in_window(gray_image_array)
    if show_text == True: print get_text_from_image(gray_image_array)

    result = test_one(gray_image_array)
    similarity_test(result, text_file_path)
    if show_text == True: print get_text_from_image(result)

    result = test_two(gray_image_array)
    similarity_test(result, text_file_path)
    if show_text == True: print get_text_from_image(result)

    result = test_three(gray_image_array)
    similarity_test(result, text_file_path)
    if show_text == True: print get_text_from_image(result)
