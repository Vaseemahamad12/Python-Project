import cv2
import numpy as np

# in this we are use convex hull and now question is what is convex hull techniq
# so convex hull are find out the outer most pixel of boundry layer and connect to other pixel and so on

hand = cv2.imread('1.jpg',0)

# so we are change the image in binary image because by the binary image pixel collection are too much easy
ret,the = cv2.threshold(hand,70,255,cv2.THRESH_BINARY)
# here we are countour method this  is use find out the outer area

contours,hierachy = cv2.findContours(the.copy(),cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

# in above line we are copy.or thresholding image and RETT|RETR_TREE are find out the contour and CHAIN_APROX_SIMPLE
# this ios use to chaain the contour

# contour function are connect the pixel to other pixel and connect together

hull = [cv2.convexHull(c) for c in contours]
# by this line which value are coming by the contour that is pass in convexhull and convex hull are save this value
final = cv2.drawContours(hand,hull, -1,(255,0,0))
cv2.imshow('original Image', hand)
cv2.imshow('ThreshHold', the)
cv2.imshow("Convex Hull",final)
cv2.waitKey(0)
cv2.destroyAllWindows()

