import os
import cv2
import face_recognition
import pickle

#import people images


folderPath = "Images"
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
peopleIds = []
imgList.append(cv2.imread("Images/1234.png"))
# for path in pathList:
#     imgList.append(cv2.imread(os.path.join(folderPath)))
#     peopleIds.append(os.path.splitext(path)[0])
    # print(path)
    # print(os.path.splitext(path))
cv2.imshow('ss',imgList)
cv2.waitKey(0)
print(peopleIds)
print(os.path.join(folderPath))
# def findEncodings(imageslist):
#     encodeList = []
#     for img in imageslist:
#         img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#         encode = face_recognition.face_encodings(img)[0]
#         encodeList.append(encode)
#
#     return encodeList
# print("Encoding Start ...")
# encodeListKnown = findEncodings(imgList)
# encodeListKnownWithIds = [encodeListKnown, peopleIds]
# print("Encoding Complete")
#
# file = open('EncodeFile.p','wb')
# pickle.dump(encodeListKnownWithIds, file)
# file.close()
# print('File Saved')
