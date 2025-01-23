import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime

# Load student images and names
path = 'student_images'
images = []
classNames = []
mylist = os.listdir(path)

for cl in mylist:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

# Function to encode faces
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encoded_faces = face_recognition.face_encodings(img)
        if len(encoded_faces) > 0:
            encodeList.append(encoded_faces[0])
        else:
            print(f"No face detected in {img}. Skipping...")
    return encodeList

# Mark attendance in CSV
def markAttendance(name):
    file_exists = os.path.isfile('Attendance.csv')
    with open('Attendance.csv', 'a+') as f:
        if not file_exists:
            f.write("Name, Time, Date\n")
        f.seek(0)
        myDataList = f.readlines()
        nameList = [line.split(',')[0] for line in myDataList]
        if name not in nameList:
            now = datetime.now()
            time = now.strftime('%I:%M:%S:%p')
            date = now.strftime('%d-%B-%Y')
            f.write(f'{name}, {time}, {date}\n')

# Encode all student images
encoded_face_train = findEncodings(images)

# Ensure data alignment
if len(encoded_face_train) != len(classNames):
    print("Error: Number of encodings and class names do not match.")
    exit()

# Webcam for real-time face recognition
cap = cv2.VideoCapture(0)
print("Press 'q' to quit the webcam feed.")

while True:
    success, img = cap.read()
    if not success:
        print("Failed to capture image from webcam.")
        break
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    # Find faces in the frame
    faces_in_frame = face_recognition.face_locations(imgS)
    encoded_faces = face_recognition.face_encodings(imgS, faces_in_frame)

    # Compare faces
    for encode_face, faceloc in zip(encoded_faces, faces_in_frame):
        matches = face_recognition.compare_faces(encoded_face_train, encode_face)
        faceDist = face_recognition.face_distance(encoded_face_train, encode_face)
        if len(faceDist) > 0:
            matchIndex = np.argmin(faceDist)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper()
                y1, x2, y2, x1 = faceloc
                y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1 + 6, y2 - 5), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                markAttendance(name)
        else:
            print("No face matches found.")

    # Display webcam feed
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
