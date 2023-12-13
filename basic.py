import cv2
import numpy as np
import face_recognition

imageElon = face_recognition.load_image_file('ImagesBasics/elon1.jpg')
imageElon = cv2.cvtColor(imageElon, cv2.COLOR_BGR2RGB)
elonTest = face_recognition.load_image_file('ImagesBasics/elontest.jpg')
elonTest = cv2.cvtColor(elonTest, cv2.COLOR_BGR2RGB)

faceLocation = face_recognition.face_locations(imageElon)[0]
encodeElon = face_recognition.face_encodings(imageElon)[0]
cv2.rectangle(imageElon, (faceLocation[3], faceLocation[0]), (faceLocation[1], faceLocation[2]), (255, 0, 255), 2)

faceLocationTest = face_recognition.face_locations(elonTest)[0]
encodeElonTest = face_recognition.face_encodings(elonTest)[0]
cv2.rectangle(elonTest, (faceLocationTest[3], faceLocationTest[0]), (faceLocationTest[1], faceLocationTest[2]), (255, 0, 255), 2)

results = face_recognition.compare_faces([encodeElon], encodeElonTest)
print(results)

faceDistance = face_recognition.face_distance([encodeElon], encodeElonTest)

print(faceDistance)

cv2.putText(elonTest, f'{results} {round(faceDistance[0],2)}',(50, 50), cv2.FONT_HERSHEY_COMPLEX,1, (0, 3, 200),1)

cv2.imshow('Elon Musk', imageElon)
cv2.imshow('Elon Test', elonTest)
cv2.waitKey(0)

