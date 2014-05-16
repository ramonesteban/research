import Image
import numpy as np
from pytesser import *

def get_text_from_image(image_array):
    image_pil = Image.fromarray(image_array)
    text = image_to_string(image_pil)
    return text
