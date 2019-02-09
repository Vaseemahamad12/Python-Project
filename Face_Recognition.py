import cv2
# from cv2 import *
import numpy as np
from os import listdir
from os.path import isfile , join
# ===================================================== 1st part=======================================================
# we are collect face sample we are coolect it by face harcascade clssifier
# in the first part we are check how to face sample are collect

# haarcascade file--- this is classifier this is persent in Opencv library
# this is haarcascade file are already persent some point by this point classifier model
# are know,what is the part of body

face_classifier = cv2.CascadeClassifier(r'C:\Users\Vaseem\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')
# we simply collect cascadeclassfier on this address for collection the face sample


def face_extracter(img):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray,1.3,5)
    #     # 1.3 is the image factor and 5 is k neabour
    if faces is ():
        #         # this is call when function value will be None
        return None
    for(x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]
        # x and y codinates
        #         # and w is use for width changes,h is use for height changes

    return cropped_face


cap = cv2.VideoCapture(0)
# call the camera
count = 0

while (True):
    ret,frame = cap.read()
    if face_extracter(frame) is not None:
        # face_extractor() function we are call and camera capture veriable are pass in this
        count+=1
        face = cv2.resize(face_extracter(frame),(200,200))
        # this is use to resize the face frame in (200X200) pixel forem
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        #  face is change into gray color
        file_name_path = (r'C:\Users\Vaseem\Desktop\OpenCv_Tut\face_sample\user' + str(count) + '.jpg')
        # in this line we are collect the sample of faces and count and sample are perform in jpg formn
        cv2.imwrite(file_name_path,face)
        # this is use to save the image in our file
        cv2.putText(face, str(count),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
        cv2.imshow('Face Cropper', face)
        # this line are use to count the sample fo face
    else:
        print('Face not Found')
        pass
    if cv2.waitKey(1) == 13 or count == 100:
        # or count == 100:
        #         # after take  100 sample loop are stop
        #         # here 13 is ascii code
        break
cap.release()
cv2.destroyAllWindows()
print('collecting sample complete')


# =====================================2nd part==========================================
# in first part we are ready dataset
# now in this phase we are trend the model on own data
# we are start with the tranning of cascade classifier

data_path = ('C:/Users/Vaseem/Desktop/OpenCv_Tut/face_sample/')
# this is path where face sample are store


onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]
# f is veriable which is save face sample one by one by iterater method and condition on
# it isfile means file are persent in this then join the data path and face veriable

Training_Data, Labels = [],[]
# here trainning data is pic which we are collect by cascade classifier
for i,files in enumerate(onlyfiles):
    # here we are write enumerate function for count the iteration
    image_Path = data_path + onlyfiles[i]
    images = cv2.imread(image_Path,cv2.IMREAD_GRAYSCALE)
    # read the image in grayscale
    Training_Data.append(np.asarray(images, dtype=np.uint8))
    Labels.append(i)

Labels = np.asarray(Labels,dtype=np.int32)
# now we are build a model

model = cv2.face.LBPHFaceRecognizer_create()
# this si model we are this model in cv2.face,,, Linear Binary Phase Histogram Face_recongnizer

model.train(np.asarray(Training_Data), np.asarray(Labels))
print('Model Trainning is Complete')

# ================================================== 3rd part=======================================================

# in this part we are predictions perfrom on the sample of pics which we are collect in part 1

face_classifier = cv2.CascadeClassifier(r'C:\Users\Vaseem\AppData\Local\Programs\Python\Python36\Lib\site-packages\cv2\data\haarcascade_frontalface_default.xml')

# this function are used to match the current vedio face smple to which we re collect first
def face_detector(img,size = 0.5):
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # which image are coming we are change into gray scale color
    faces = face_classifier.detectMultiScale(gray , 1.3,5)

    if faces is ():
        return img,[]
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
        # for are check on face what is change in weight of x(face),and height of y(face_height)
        roi = img[y:y+h,x:x+w]
        # this is reason of interest
        roi = cv2.resize(roi,(200,200))
        # we are resize this reason of interest

    return img,roi

# now we are create main function
cap = cv2.VideoCapture(0)
while(True):
    ret,frame = cap.read()

    image,face = face_detector(frame)
    try:
        face = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
        result = model.predict(face)

        if result[1] < 500:
            confidence = int(100*(1-(result[1])/300))
            # this condition re gave percentage value how much owr face arr match
            display_string = str(confidence) + '% confidence it is user'
        cv2.putText(image,display_string, (100,120),cv2.FONT_HERSHEY_COMPLEX,1,(255,250,120),2)
        # by the puttext function we are show the text on the video frame
        if confidence > 75:
            cv2.putText(image,"unlocked",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(150,250,255),2)
            cv2.imshow('Face Cropper', image)
        else:
            cv2.putText(image,"Locked",(250,450),cv2.FONT_HERSHEY_COMPLEX,1,(230,23,251),2)
            cv2.imshow('Face Cropper ', image)
    except:
        cv2.putText(image, "Face Not Found", (250, 450), cv2.FONT_HERSHEY_COMPLEX, 1, (20, 23, 251), 2)
        cv2.imshow('Face Cropper ', image)
        pass

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()