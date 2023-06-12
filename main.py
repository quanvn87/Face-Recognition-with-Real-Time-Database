import cv2
import os

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

#load the encoding file
file = open('EncodeFile.p','rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, peopleIds = encodeListKnownWithIds
print(peopleIds)




while True:
    susccess, img = cap.read()

    imgBackground[162:162+480, 55:55+640] = img
    imgBackground[44:44 + 633, 800:800 + 414] = imgModeList[0]
    cv2.imshow("Webcam", img)
    cv2.imshow('Face Attendence', imgBackground)
    cv2.waitKey(1)
