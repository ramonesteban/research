import cv2
import numpy as np

from image_filters import *
from image_functions import *

def image_processing(image_file_path):
    image = cv2.imread(image_file_path)
    gray_image_array = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray_image_array = cv2.GaussianBlur(gray_image_array, (5, 5), 0)
    image_filtered = threshold('otsu', gray_image_array)
    return get_text_from_image(image_filtered)
