import sys, os, Image
from pytesser import *

def get_text(image_file_path):
  image = Image.open(image_file_path)
  print image_to_string(image) 

def main():
  if len(sys.argv) > 1:
    image_file_path = sys.argv[1]
    if os.path.isfile(image_file_path):
      get_text(image_file_path)
    else:
      print 'Image file does not exist'
  else:
    print 'First parameter must be an image file name'

if __name__ == '__main__':
  main()
