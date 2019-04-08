from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askopenfilenames
import cv2
import numpy as np
import os.path
from PIL import Image
from pathlib import Path

path = Path.cwd()

Tk().withdraw()
filename = askopenfilenames()

d = 0

# path = 'C:/Users/Vaseem/Desktop/Practice/Image_Sample'

for file in filename:
    x1 = file
    #     print(x)
    img1 = cv2.imread(file, 0)
    ret, Bry = cv2.threshold(img1, 127, 255, 0, cv2.THRESH_BINARY)

    img = cv2.imread(file, 0)
    x = cv2.imread(x1)

    size = np.size(img)
    skel = np.zeros(img.shape, np.uint8)
    ret, img = cv2.threshold(img, 127, 255, 0)
    element = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    done = False

    while (not done):
        eroded = cv2.erode(img, element)
        temp = cv2.dilate(eroded, element)
        temp = cv2.subtract(img, temp)
        skel = cv2.bitwise_or(skel, temp)
        img = eroded.copy()

        zeros = size - cv2.countNonZero(img)
        if zeros == size:
            done = True

    cv2.imshow("Thinning_Image", skel)
    #     cv2.imwrite('write_name.png', img)
    cv2.imshow('Original_Image', x)
    cv2.imshow('Binary_Image', Bry)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

cv2.imwrite('write_name.png', img)

print('Your image save on this path ')
path