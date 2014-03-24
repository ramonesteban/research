import os
import Image
from pytesser import *

if os.path.isfile('public/image.jpg'):
  image = Image.open('public/image.jpg')
  print image_to_string(image)
else:
  print 'File not found.'
