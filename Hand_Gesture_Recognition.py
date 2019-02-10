import cv2
import numpy as np
import math
import pandas as pd

capture = cv2.VideoCapture(0)
# open the camera
while capture.isOpened():
    # isopened are check untill live feed are coming the this is True anbd work otherwise it is stop
    ret,frame = capture.read()

     # Get hand dataa from the rectanglle sub window simply if we are saying we are try to catch the hand data by
    # rectangle
    cv2.rectangle(frame, (100,100),(300,300),(0,255,0),0)
    # rectngle are create on frame and 100x100 is strating vaalue and 300x 300 is lst value this is X,Y codienent value
    # and we are pass the value of color or width is 0
    crop_image = frame[100:300,100:300]
    # by crop_image we are crop the frame the on X,Y value

    # apply guassian blur
    blur = cv2.GaussianBlur(crop_image, (3,3),0)
    # simply we are perform the gaaussian blur kernal value is 3x3

    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)
    # now we are change the frame iun csv

    mask2 = cv2.inRange(hsv, np.array([2,0,0]), np.array([20,255,255]))
    # ceate thye binary image with where white will be skin colors and rest is balck
    # so in np.arrayt we are define the value of accoding to skin color minimum value and maximum value

    kernal = np.ones((5,5))
    # kernal for morphological transform

    dilation = cv2.dilate(mask2, kernal , iterations=1)
    # apply morphological transformation to filter out the background noise
    erosion = cv2.erode(dilation, kernal , iterations=1)

    # apply again Gaussian blur because after erosion if any noise aare coming then it control on it
    filtered = cv2.GaussianBlur(erosion , (3,3), 0)
    ret,thresh=  cv2.threshold(filtered , 127,255,0)
    # we are threshold perform on it
    cv2.imshow("Thresholded" , thresh)

    contours ,hierarchy = cv2.findContours(thresh , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # we are contour find out here this is use to collect the pixel of outer boundaaary

    try:
        contour = max(contours, key = lambda x: cv2.contourArea(x) )
        # by max we re find out maximum number of area lmabda function are use because we are dont know which area area
        # are coming

        x,y,w,h = cv2.boundingRect(contour)
        cv2.rectangle(crop_image , (x,y ) , (x+w ,y + h) , (0,0,255),0)
        hull = cv2.convexHull(contour)

        # Draw contour
        drawing = np.zeros(crop_image.shape, np.uint8)
        cv2.drawContours(drawing, [contour] , -1, (0,255,0),0)
        # this is use for contour output
        cv2.drawContours(drawing , [hull], -1, (0,0,255),0)
        # this is use for hull output

        # find convexity defects
        # this is collect the gap amoung fingers ,, use consider rule to find the angle of far point from the start
        # and end point
        hull = cv2.convexHull(contour , returnPoints= False)
        defects = cv2.convexityDefects(contour , hull)

        count_defects = 0
        # this is calculate the defects by this function we are calculate how many finger are available on screen
        for i in range(defects.shape[0]):
            s,e,f,d = defects[i, 0]
            # s ius starting point and e is endpoint and f is far point and d is distance
            start = tuple(contour[s][0])
            end = tuple(contour[e][0])
            far = tuple(contour[f][0])
             # by this function we are calculate the finger of hand

            a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
            b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) **2 )
            c= math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
            angle = (math.acos((b ** 2 + c **2 - a ** 2) / (2 * b * c)) * 180)/ 3.14
            # this is formula of cos sin function in the geometric this is use for when angle of hand are change them
            # this is know in which direction hand have to change
            if angle <= 90:
                # if hand angle is less then 90 then
                count_defects += 1
                # couint increase 1
                cv2.circle(crop_image, far ,1, [0,0,255],-1)
                # here we are gave -1 because fill the under line in circle
                # we are draw a circle
            cv2.line(crop_image , start , end , [0,255,0],2)
            # and we are draw aa line for connect the point of line , on crop_image start point to end point and 2
            # is thickness

        if count_defects == 0 :
            cv2.putText(frame , "ONE" , (50,50), cv2.FONT_HERSHEY_SIMPLEX , 2 , (0,0,255),2)
        elif count_defects ==1:
            cv2.putText(frame, "TWO", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects ==2 :
            cv2.putText(frame, "THREE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif count_defects == 3:
            cv2.putText(frame, "FOUR", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        elif  count_defects ==4 :
            cv2.putText(frame, "FIVE", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2)
        else:
            pass
        # this function are print the finger value which is cout by the count_defects function

    except:
        pass


    cv2.imshow("GESTURE" , frame)
    all_image = np.hstack((drawing , crop_image))
    # horizontal stack we are use to show both output of drwing and crop_image
    cv2.imshow("CONTOUR" , all_image)

    if cv2.waitKey(1) == ord('v'):
        # this is ord function means not need to type and buttuon asci code any button enter and then program is close
        break
capture . release()
cv2.destroyAllWindows()

