import sys, os

from image_processor import *

if len(sys.argv) > 1:
    image_file_path = sys.argv[1]
    if os.path.isfile(image_file_path):
        print image_processing(image_file_path)
    else:
        print 'File not found.'
else:
    print 'Internal parameter is missing.'
