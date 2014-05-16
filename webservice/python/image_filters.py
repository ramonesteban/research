import cv2
import numpy as np

def threshold(method, gray_image_array):
    if method == 'binary_inverted':
        # Binary inverted thresholding
        ret, image_thresholded = cv2.threshold(gray_image_array, 127, 255, cv2.THRESH_BINARY_INV)
        return image_thresholded
    elif method == 'binary':
        # Binary thresholding
        ret, image_thresholded = cv2.threshold(gray_image_array, 127, 255, cv2.THRESH_BINARY)
        return image_thresholded
    elif method == 'otsu':
        # Otsu's thresholding
        ret, image_thresholded = cv2.threshold(gray_image_array, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        return image_thresholded
    elif method == 'adaptive':
        image_thresholded = cv2.adaptiveThreshold(gray_image_array, 255, 1, 1, 11, 2)
    else:
        print 'threshold not found'
        return gray_image_array

def blur(method, gray_image_array):
    if method == 'gaussian':
        blur_image_array = cv2.GaussianBlur(gray_image_array, (5, 5), 0)
        return blur_image_array
    elif method == 'median':
        blur_image_array = cv2.medianBlur(gray_image_array, 5)
        return blur_image_array
    else:
        print 'blur not applied'
        return gray_image_array
