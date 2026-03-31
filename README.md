
# Face Recognition Attendance System with KNN


## Overview

This project is a face recognition-based attendance system that leverages K-Nearest Neighbors (KNN) for classification. It captures video frames using a webcam, detects faces, and identifies individuals based on a pre-trained model. The system records attendance by logging names, registration numbers, and timestamps.

## Features

- Face Detection: Uses OpenCV's Haar cascade classifier to detect faces in real-time from webcam footage.
- Face Recognition: Employs a KNeighborsClassifier model trained on labeled images to recognize individuals.
- Registration Number Identification: A separate KNeighborsClassifier model predicts registration numbers linked to recognized faces.
- Attendance Logging: Once confirmed (by pressing the 'o' key), the system records attendance details in a CSV file named "Attendance\_Date.csv" (Date follows DD-MM-YYYY format).

### Optional Features

- Text-to-Speech Notification: Announces attendance confirmation (requires `win32com` library).
- Custom Background Overlay: Allows a background image to be added to the video frame.

## Requirements

Ensure you have the following installed:

- Python 3.x
- OpenCV (`pip install opencv-python`)
- NumPy (`pip install numpy`)
- Scikit-learn (`pip install scikit-learn`)
- Pickle (included in Python)
- CSV (included in Python)
- `win32com` (optional, for Text-to-Speech functionality)

## Setup Instructions

1. Download Face Detection Classifier: Obtain OpenCV's Haar cascade classifier for frontal face detection from [OpenCV's official documentation](https://docs.opencv.org/4.x/db/d28/tutorial_cascade_classifier.html). Place the file in a newly created `data` folder within the project directory.
2. Train the KNN Models: Prepare a dataset containing labeled face images along with corresponding names and registration numbers. Train the KNN models using provided scripts or custom code. Save the trained models as `names.pkl`, `faces_data.pkl`, and `regs.pkl` in the `data` folder.
3. Run the Script: Execute `test.py` using Python. The script will initiate the webcam, detect and recognize faces, and record attendance upon confirmation.

## Additional Notes

- System accuracy depends on the quality and diversity of the training data, as well as optimal KNN parameter selection.
- Enhancements can include confidence-based predictions, handling multiple faces in a single frame, and improved database integration.

## 📧 **Created by** 
Rananjay Singh Chauhan
[Anugya Chaubey]https://github.com/chaubeyanugya/face-recognition-attendance-system/
