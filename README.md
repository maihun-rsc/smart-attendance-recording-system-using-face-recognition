# Smart Attendance System using Face Recognition

This is a Python-based Smart Attendance System that utilizes facial recognition to automate the process of taking attendance. The project uses OpenCV for face detection, K-Nearest Neighbors (KNN) from scikit-learn for face recognition, and Streamlit to display the attendance records in a web interface.

## Features
- **Face Registration**: Capture and store face encodings along with the user's name and registration number.
- **Automated Attendance**: Real-time face recognition to mark attendance seamlessly.
- **Audio Feedback**: Voice greeting using Windows Text-to-Speech when attendance is marked.
- **Live Dashboard**: A Streamlit web application that auto-refreshes to display the day's attendance records.

## Project Structure
- `add_faces.py`: Script to register new users by capturing 100 face images through the webcam and saving their encodings in the `data/` directory.
- `test.py`: Main script for taking attendance. It captures video feed, recognizes registered faces using a trained KNN model, and logs the attendance with a timestamp into a CSV file inside the `Attendance/` directory.
- `app.py`: A Streamlit web dashboard that reads the daily attendance CSV file and displays it in a tabular format. The dashboard auto-refreshes every 2 seconds.
- `data/`: Directory containing the Haar cascade XML file (`haarcascade_frontalface_default.xml`) for face detection and the pickled `.pkl` files storing names, registration numbers, and face encodings.
- `Attendance/`: Directory where daily attendance is saved as CSV files (`Attendance_DD-MM-YYYY.csv`).

## Prerequisites
Ensure you have Python installed. Install the required dependencies using:

```bash
pip install opencv-python numpy pandas scikit-learn streamlit streamlit-autorefresh pywin32
```
*Note: `pywin32` is required for the Text-to-Speech functionality on Windows.*

## How to Run

1. **Register a User**:
   Run the `add_faces.py` script. Enter your name and registration number in the terminal. Look at the webcam until 100 frames of your face are captured.
   ```bash
   python add_faces.py
   ```

2. **Take Attendance**:
   Run the `test.py` script. It will open your webcam and draw a bounding box around your face. Press the **`o`** key to confirm and mark your attendance. Your details will be saved in today's CSV file. Press **`x`** to exit the window.
   ```bash
   python test.py
   ```

3. **View Attendance Dashboard**:
   Run the Streamlit app to view the live attendance sheet.
   ```bash
   streamlit run app.py
   ```

## Notes
- To reset the system or remove users, delete the `.pkl` files inside the `data/` directory (except the `haarcascade` xml file).
- The Text-to-Speech feature (`win32com.client`) works out-of-the-box on Windows. If running on another OS, you'll need to modify the `speak()` function in `test.py` to use an alternative TTS library like `pyttsx3`.
- Ensure you have `before_attendance.png` and `attendance_taken.png` in the root directory for the UI frames to load properly in `test.py`.


## Created by 
- Rananjay Singh Chauhan
- [Anugya Chaubey](https://github.com/chaubeyanugya/face-recognition-attendance-system)
