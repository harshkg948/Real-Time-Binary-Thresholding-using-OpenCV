# Real-Time Binary Thresholding using OpenCV

A simple real-time computer vision project using OpenCV and Python that captures webcam video and converts each frame into a binary black-and-white image using thresholding.

## 🚀 Features

* Real-time webcam capture
* Binary thresholding on live video
* Converts frames into black & white output
* Lightweight and beginner-friendly
* Built using Python + OpenCV

## 🛠️ Tech Stack

* Python
* OpenCV

## 📌 How It Works

The webcam continuously captures frames.

Each frame:

1. Is read using `VideoCapture`
2. Processed using `cv2.threshold()`
3. Converted into a binary image
4. Displayed in real time

Threshold Logic:

```python id="6zy1o9"
pixel > 120  → 255 (White)
pixel <= 120 → 0 (Black)
```

## 💻 Code

```python id="45ixck"
import cv2 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    _, thresh = cv2.threshold(
        src=frame,
        thresh=120,
        maxval=255,
        type=cv2.THRESH_BINARY
    )

    cv2.imshow('thresh', thresh)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
```

## ▶️ Run the Project

Install OpenCV:

```bash id="7ls8rj"
pip install opencv-python
```

Run:

```bash id="1wy3z4"
python app.py
```

Press `q` to exit the webcam window.

## 📷 Output

The application shows a live binary thresholded webcam feed where brighter pixels become white and darker pixels become black.

## 🎯 Learning Concepts

* Webcam handling
* Frame processing
* Image thresholding
* Real-time computer vision
* OpenCV basics

## 📚 Future Improvements

* Adaptive Thresholding
* Edge Detection
* Contour Detection
* Object Tracking
* Hand Gesture Recognition

## ⭐ Beginner Friendly

Perfect mini-project for learning real-time image processing and understanding how thresholding works in computer vision.


# Real-Time-Binary-Thresholding-using-OpenCV
