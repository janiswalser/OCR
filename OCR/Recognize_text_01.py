import cv2
import numpy as np
import pytesseract
from PIL import Image
import sys

# Path of working folder on Disk
src_path = str(sys.argv[1])



def get_string(img_path):
    # Read image with opencv
    img = cv2.imread('test.png',0)

    # Apply dilation and erosion to remove some noise
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)

    cv2.imwrite(src_path + "removed_noise.png", img)

    cv2.imwrite(src_path + "thres.png", img)

    # Recognize text with tesseract for python
    result = pytesseract.image_to_string(Image.open(src_path + "thres.png"))

    return result

file = open("testfile.txt","w+") 

file.write(get_string(src_path))

file.close() 

print '--- Yes I can read that shit ! ---'
print get_string(src_path)

print "-------------- Done --------------"