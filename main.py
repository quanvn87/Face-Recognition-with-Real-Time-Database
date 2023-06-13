import cv2
import os
import pickle

import face_recognition
import numpy as np
import cvzone

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendentrealtime-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendentrealtime.appspot.com"
})

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imgBackground = cv2.imread('Resources/background.png')

#import the mode images into a list
folderModelPath = 'Resources/Modes'
modePathList = os.listdir(folderModelPath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModelPath,path)))

def resize_images_in_folder(input_folder, target_size):
    # Lặp qua tất cả các tệp trong thư mục input
    for filename in os.listdir(input_folder):
        # Đường dẫn đầy đủ đến tệp
        input_path = os.path.join(input_folder, filename)

        # Đọc ảnh từ tệp gốc
        image = cv2.imread(input_path)

        # Kiểm tra xem ảnh có được đọc thành công hay không
        if image is not None:
            # Resize ảnh
            resized_image = cv2.resize(image, target_size)

            # Ghi đè lên ảnh gốc
            cv2.imwrite(input_path, resized_image)

input_folder = "Images"

target_size = (216,216)

resize_images_in_folder(input_folder, target_size)


#load the encoding file
print("Loading Encode File ...")
file = open('EncodeFile.p','rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, personIds = encodeListKnownWithIds
print("Encode File Loaded")
#print(personIds)

modeType = 0
counter = 0
id=-1


while True:
    susccess, img = cap.read()
    imgS = cv2.resize(img, (0,0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)


    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44 + 633, 800:800 + 414] = imgModeList[modeType]

    for encodeFace, faceLocation in zip(encodeCurFrame, faceCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown,encodeFace)
        # print("matches",matches)
        # print("faceDistance", faceDistance)

        matchIndex = np.argmin(faceDistance)

        if matches[matchIndex]:
            # print("Known Face Detected")
            # print(personIds[matchIndex])
            y1, x2, y2, x1 = faceLocation
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            bbox = 55+x1, 162+y1, x2-x1, y2-y1
            imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
            id = personIds[matchIndex]

            if counter==0:
                counter=1

    if counter!=0:
        if counter==1:
            personInfor = db.reference(f'People/{id}').get()
            print(personInfor)

        counter+=1

    cv2.imshow('Face Attendence', imgBackground)
    cv2.waitKey(1)
