import cv2
import numpy as np
import face_recognition
import os

path = 'ImagesAttendence'
images = []
classNames = []

mylist = os.listdir(path)
print(mylist)

for cls in mylist:
    curImage = cv2.imread(f'{path}/{cls}')
    images.append(curImage)
    classNames.append(os.path.splitext(cls)[0])

print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGRA2BGR)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

encodeListKnown = findEncodings(images)

print('Encoding completed')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS,cv2.COLOR_BGRA2BGR)

    facesInCurrentFrame = face_recognition.face_locations(imgS)
    encodeCurrentFrame = face_recognition.face_encodings(imgS,facesInCurrentFrame)

    for encodeFace, faceLocation in zip(encodeCurrentFrame, facesInCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDistance = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDistance)
        matchIndex = np.argmin(faceDistance)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            print(name)
            y1, x2, y2, x1 = faceLocation
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow('webcam', img)
    cv2.waitKey(1)
