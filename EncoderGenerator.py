import os
import cv2
import face_recognition
import pickle

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': "https://faceattendentrealtime-default-rtdb.firebaseio.com/",
    'storageBucket': "faceattendentrealtime.appspot.com"
})

#import person images


folderPath = "Images"
pathList = os.listdir(folderPath)
print(pathList)
imgList = []
personIds = []
for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath,path)))
    personIds.append(os.path.splitext(path)[0])
    # print(path)
    # print(os.path.splitext(path))
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

print(personIds)

def findEncodings(imageslist):
    encodeList = []
    for img in imageslist:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
print("Encoding Start ...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, personIds]
print("Encoding Complete")

file = open('EncodeFile.p','wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print('File Saved')
