import sys, os
import Image
from pytesser import *

if len(sys.argv) > 1:
    image_file_path = sys.argv[1]
    if os.path.isfile(image_file_path):
        image = Image.open(image_file_path)
        print image_to_string(image)
    else:
        print 'File not found.'
else:
    print 'Internal parameter is missing.'
