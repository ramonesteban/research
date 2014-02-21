import Image
from pytesser import *

image = Image.open('image.jpg')
print image_to_string(image)
