import sys, os
import Image
from pytesser import *

from test_filters import *

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
