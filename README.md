# AI Assignment – OpenCV and DeepFace

## Overview
This project contains three computer vision tasks implemented using OpenCV and DeepFace.

---

## Task 1 – Real-Time Motion Detection Using OpenCV

### Description
Detects motion in real-time using a webcam by comparing consecutive video frames.

### Technologies Used
- Python
- OpenCV

### Output
Motion is highlighted whenever movement is detected in front of the camera.

---

## Task 2 – Emotion-Based Smart Alert System

### Description
Uses DeepFace to analyze facial emotions in real time.

### Functionality
- Detects emotions from webcam feed.
- Displays the dominant emotion.
- Prints:

```text
ALERT: SAD
```

when a sad emotion is detected.

### Technologies Used
- Python
- OpenCV
- DeepFace

---

## Task 3 – Gender Classification System

### Description
Uses DeepFace to classify gender from a live webcam stream.

### Functionality
- Detects face using webcam.
- Predicts gender.
- Displays:

```text
Gender: Man
```

or

```text
Gender: Woman
```

on the video feed.

### Technologies Used
- Python
- OpenCV
- DeepFace

---

## Project Structure

AI-ASSIGNMENT/
│
├── exp1.py
├── exp2.py
├── exp3.py
├── requirements.txt
├── task1_motion_detection.png
├── task2_emotion_alert.png
├── task3_gender_classification.png
└── README.md

---

## Installation

```bash
pip install -r requirements.txt
```

## Requirements

- Python 3.x
- OpenCV
- DeepFace
- TensorFlow

## Author

Aanya Chawla
SRM University