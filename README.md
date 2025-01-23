## Face Recognition Attendance System 📸✅

A Python-based real-time attendance system that uses face recognition to identify users and mark their attendance. Built using OpenCV, face_recognition, and NumPy.

## Features ✨
- **Real-Time Face Recognition**: Detects faces using a webcam feed.
- **Automatic Attendance Logging**: Marks attendance with timestamps in a CSV file.
- **Customizable Dataset**: Easily add or remove student images.
- **Visual Feedback**: Displays bounding boxes and names on the webcam feed.

- ## How It Works 🛠️

1. **Load Student Images**:
   - Add student images to the `student_images` folder. Each file name should be the name of the student (e.g., `john_doe.jpg`).

2. **Face Encoding**:
   - The system encodes all the student images into unique numerical representations.

3. **Webcam Feed**:
   - The webcam detects faces in real-time and compares them to the encoded faces.

4. **Attendance Logging**:
   - If a match is found, the system logs the student’s name, time, and date into `Attendance.csv`.

## Installation and Setup ⚙️

### Prerequisites
- Python 3.9 or higher
- Webcam or Camera

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/pranav727/Face-Recognition-Attendence-System-using-python.git

2.Navigate to the project directory:
     ```bash
     
    cd Face-Recognition-Attendance-System 
    
3.Install the required dependencies:
       ```bash

       pip install -r requirements.txt

4.Run the project:
       ```bash

       python main.py

       

       




