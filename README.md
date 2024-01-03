# Webcam-Edge-Tracing

This Python script utilizes the OpenCV library to perform edge detection on real-time webcam footage. It captures video from the webcam, processes the frames to detect edges, and displays the output in real-time.

## Features

- **Real-Time Edge Detection**: Uses the webcam to capture video and performs edge detection on the captured frames.
- **Canny Edge Detection**: Implements Canny edge detection algorithm.
- **Resizable Frame**: Adjusts the size of the video frame.
- **Mirror-like Effect**: Flips the video frame to create a mirror-like effect.

## Requirements

To run this script, you need to have Python installed on your system along with the OpenCV library. You can install OpenCV using pip:

 ```bash
 pip install opencv-python

## Usage

To start the edge detection, simply run the script
Tracing edges from webcam.py

## Note

The script currently uses the Canny edge detection method. However, it can be modified to use other methods like Laplacian and Sobel by uncommenting the respective lines in the code


# Image-Edge-Tracing
This Python project demonstrates various edge detection techniques using the OpenCV library. It provides an easy-to-follow script that showcases three different methods of edge detection: Sobel Edge Detection, Laplacian Edge Detection, and Canny Edge Detection.

### Key Features:

1. **Reading and Resizing Images:** The script starts by reading an image from a file and resizing it for optimal processing.
2. **Sobel Edge Detection:** Implements both horizontal and vertical edge detections using the Sobel operator.
3. **Laplacian Edge Detection:** Demonstrates the use of the Laplacian operator for edge detection.
4. **Canny Edge Detection:** Showcases the popular Canny edge detection algorithm, with adjustable threshold values.

### Prerequisites

- Python 3.x
- OpenCV library (cv2)

## Setup and Installation

1. **Python Installation:** Ensure Python 3.x is installed on your system. If not, download and install it from the [Python website](https://www.python.org/downloads/).

2. **OpenCV Installation:** Install OpenCV for Python by running the following command:
   ```bash
   pip install opencv-python
