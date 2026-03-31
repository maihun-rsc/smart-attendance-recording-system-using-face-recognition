# Import necessary modules

import cv2  # OpenCV library for computer vision tasks (image processing, face detection)
import pickle  # Module for serializing and deserializing Python objects (storing data)
import numpy as np  # Library for numerical computations (array manipulation)
import os  # Module for interacting with the operating system (file system)

# Initialize video capture object from webcam (index 0)
video = cv2.VideoCapture(0)

# Load the pre-trained face detection classifier (Haar cascade)
facedetect = cv2.CascadeClassifier('data/haarcascade_frontalface_default.xml')

# Empty list to store captured face encodings
faces_data = []

# Counter variable for captured faces
i = 0

# Get user input for name and registration number
name = input("Enter Your Name: ")
reg = input("Enter Your Registration Number: ")

while True:
  # Capture frame-by-frame from the video stream
  ret, frame = video.read()

  # Convert the frame from BGR to grayscale for face detection
  gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

  # Detect faces in the grayscale frame using the classifier
  faces = facedetect.detectMultiScale(gray, 1.3, 5)

  # Loop through detected faces
  for (x, y, w, h) in faces:
    # Extract the face region from the framepic
    crop_img = frame[y:y + h, x:x + w, :]

    # Resize the extracted face to a fixed size for consistency
    resized_img = cv2.resize(crop_img, (50, 50))

    # Only capture a face every 10 frames for efficiency
    if len(faces_data) <= 100 and i % 10 == 0:
      # Append the resized face encoding to the list
      faces_data.append(resized_img)

    # Increment counter
    i = i + 1

    # Display the number of captured faces on the frame
    cv2.putText(frame, str(len(faces_data)), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (50,50,255), 1)

    # Draw a rectangle around the detected face
    cv2.rectangle(frame, (x, y), (x + w, y + h), (50, 50, 255), 1)

  # Display the captured video frame
  cv2.imshow("Frame", frame)

  # Wait for a key press with a delay of 1 millisecond
  k = cv2.waitKey(1)

  # Exit loop if 'q' key is pressed or 100 faces are captured
  if k == ord('q') or len(faces_data) == 100:
    break

# Release the video capture object
video.release()

# Destroy all OpenCV windows
cv2.destroyAllWindows()

# Convert the list of faces to a NumPy array
faces_data = np.asarray(faces_data)

# Reshape the array to a format suitable for machine learning (100 faces, flattened features)
faces_data = faces_data.reshape(100, -1)

# ------------------------ Data Management --------------------------

# Check if a file named 'names.pkl' exists in the 'data' folder
if 'names.pkl' not in os.listdir('data/'):
  # If not, create a list containing the user's name repeated 100 times
  names = [name] * 100
  # Open the file in write binary mode and pickle the list of names
  with open('data/names.pkl', 'wb') as f:
    pickle.dump(names, f)
else:
  # If the file exists, open it in read binary mode and unpickle the list of names
  with open('data/names.pkl', 'rb') as f:
    names = pickle.load(f)
  # Append the user's name to the existing list and repeat it 100 times
  names = names + [name] * 100
  # Open the file again in write binary mode and pickle the updated list of names
  with open('data/names.pkl', 'wb') as f:
    pickle.dump(names, f)

  # Similar process for storing face encodings ('faces_data.pkl') and registration numbers ('regs.pkl')
  if 'faces_data.pkl' not in os.listdir('data/'):
    with open('data/faces_data.pkl', 'wb') as f:
      pickle.dump(faces_data, f)
  else:
    with open('data/faces_data.pkl', 'rb') as f:
      faces = pickle.load(f)
    faces = np.append(faces, faces_data, axis=0)
    with open('data/faces_data.pkl', 'wb') as f:
      pickle.dump(faces, f)

  if 'regs.pkl' not in os.listdir('data/'):
    regs = [reg] * 100
    with open('data/regs.pkl', 'wb') as f:
      pickle.dump(regs, f)
  else:
    with open('data/regs.pkl', 'rb') as f:
      regs = pickle.load(f)
    regs = regs + [reg] * 100
    with open('data/regs.pkl', 'wb') as f:
      pickle.dump(regs, f)
    