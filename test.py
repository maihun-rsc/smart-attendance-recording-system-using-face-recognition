# File for testing the project by recognizing faces and taking attendance

#install required modules/libraries using command pip install -r requirements.txt

# Import libraries
from sklearn.neighbors import KNeighborsClassifier # For K-Nearest Neighbors classification
import cv2  # OpenCV library for computer vision (webcam, image processing)
import pickle # For saving and loading trained models (KNeighborsClassifier)
import numpy as np # For numerical operations (array manipulation)
import os # For file system interaction (checking file existence)
import csv # For reading and writing CSV files (attendance records)
import time # For time-related functions (attendance timestamp)
from datetime import datetime # For creating formatted timestamps

# Import library for Text-to-Speech (using win32com)
from win32com.client import Dispatch

# Function to speak text using Text-to-Speech (replace if not using win32com)
def speak(str1):
    speak = Dispatch(("SAPI.SpVoice"))
    speak.Speak(str1)


# Initialize video capture object from webcam (index 0)
video = cv2.VideoCapture(0)

# Load the pre-trained face detection classifier (Haar cascade)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Load the pickled data files containing names, faces, and registration numbers
with open('data/names.pkl', 'rb') as w:
    LABELS = pickle.load(w)
with open('data/faces_data.pkl', 'rb') as f:
    FACES = pickle.load(f)
with open('data/regs.pkl', 'rb') as q:
    REGS = pickle.load(q)

# Print the shape of the faces matrix for debugging or verification
print('Shape of Faces matrix --> ', FACES.shape)

# Create a KNeighborsClassifier object for face recognition (k=5 neighbors)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(FACES, LABELS)  # Train the classifier on faces and their corresponding names

# Create another KNeighborsClassifier object for registration number recognition (k=2 neighbors)
pnn = KNeighborsClassifier(n_neighbors=2)
pnn.fit(FACES, REGS)  # Train the classifier on faces and their corresponding registration numbers

# Load a background image (optional, for visual enhancement)
imgBackground = cv2.imread("before_attendance.png")

# Define column names for the attendance CSV file
COL_NAMES = ['NAME', 'REG', 'TIME']

# Counter variable to limit the number of attendance confirmations
count = 0

while count <= 80:
    # Capture frame-by-frame from the video stream
    ret, frame = video.read()

    # Convert the frame from BGR to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame using the classifier
    faces = facedetect.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:     
        # Extract the face region from the frame
        crop_img = frame[y:y + h, x:x + w, :]

        # Resize the extracted face to a fixed size for consistency
        resized_img = cv2.resize(crop_img, (50, 50)).flatten().reshape(1, -1)

        # Predict the name using the trained KNeighborsClassifier
        output = knn.predict(resized_img)

        # Predict the registration number using the trained KNeighborsClassifier
        notput = pnn.predict(resized_img)

        # Get the current timestamp for attendance record
        ts = time.time()
        date = datetime.fromtimestamp(ts).strftime("%d-%m-%Y")
        timestamp = datetime.fromtimestamp(ts).strftime("%H:%M-%S")

        # Check if an attendance CSV file exists for the current date
        exist = os.path.isfile("Attendance/Attendance_" + date + ".csv")

        # Draw a rectangle around the detected face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 1)

        # Draw a colored rectangle around the face for better visibility
        cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 2)

        cv2.rectangle(frame,(x,y-40),(x+w,y),(50,50,255),-1)
        cv2.putText(frame, str(output[0]), (x,y-15), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255), 1)
        cv2.rectangle(frame, (x,y), (x+w, y+h), (50,50,255), 1)

        # Logic for attendance confirmation (press 'o' to confirm)
        attendance = [str(output[0]), str(notput[0]), str(timestamp)]
    imgBackground[162:162 + 480, 55:55 + 640] = frame
    cv2.imshow("Frame",imgBackground)
    k=cv2.waitKey(1)
    if k == ord('o'):
        count += 1
        # Change background image after attendance confirmation (optional)
        imgBackground = cv2.imread("attendance_taken.png")
            # Text-to-Speech announcement (replace if needed)
        speak("Welcome to VIT " + str(output[0]))
        # Reduce sleep time after confirmation (optional)
        time.sleep(1)
        # Write attendance record to CSV file (if file exists, append, otherwise create a new file with header)
        if exist:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(attendance)
        else:
            with open("Attendance/Attendance_" + date + ".csv", "+a") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(COL_NAMES)
                writer.writerow(attendance)
        # Exit loop if 'x' key is pressed
    if k==ord('x'):
        break

# Release the video capture object
video.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()