import cv2, Image
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

def get_text_from_file(image_file_path):
    image_pil = Image.open(image_file_path)
    text = image_to_string(image_pil)
    return text

def show_pil_image(image_pil):
    image_pil.show()
