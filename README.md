# **Yolov5_Person Detection and Tracking** 



https://github.com/Nbn03/Yolov5_Person-Detection-and-Tracking/assets/136473086/967041bc-ea3f-4525-8278-13cedef190df




## Overview
This repository contains code for person detection and tracking using Yolov5 and OpenCV. The model is trained using a custom dataset and is designed to detect and track individuals in video frames, marking them with bounding boxes and counting the number of people crossing a specified line.

## Main Functionalities
- **Person Detection:** Uses Yolov5 for detecting persons in video frames.
- **Person Tracking:** Tracks each detected person using OpenCV.
- **Crossing Line Detection:** Identifies when a person crosses a specified line in the video frame.
- **Bounding Box Coloring:** Marks individuals on different sides of the line with distinct colors.
- **Counting:** Counts and displays the number of people who have crossed the line.
  
## Dependencies
- **Yolov5:** A family of YOLO (You Only Look Once) models designed for object detection. Yolov5 is known for its speed and accuracy in detecting objects.
- **OpenCV:** An open-source computer vision library that provides tools for image and video processing. In this project, OpenCV is used for tracking detected persons and drawing bounding boxes on video frames.

### Yolov5 and YOLO Models
YOLO (You Only Look Once) models are convolutional neural networks (CNN) designed for real-time object detection. Yolov5, a version of YOLO, is known for its improved performance and ease of use. The model used in this project is trained with custom weights (best.pt) to detect persons in video frames.

## Model Training
The model is trained using the Yolov5 architecture with the following specifics:

- **Custom Weight File:** best.pt
- **Dataset:** Approximately 400 frames annotated with a single class "Person"
- **Annotation Tool:** LabelImg tool in Anaconda Prompt
- **Training:** 150 epochs
  
## Tracking and Detection Details
- **Tracker File:** tracker.py is used to track every single "Person" class.
- **Line Detection:** A line is added on the video frames to detect when a person crosses it.
- **Green Bounding Box:** Person on the upper side of the line.
- **Red Bounding Box:** Person who has crossed the line.
- **Counter:** Displays the number of people in the red bounding box.
  
## Running the Code
### Points to Note
- Ensure all files in the repository are present in the folder where the main.py file is running. If the video or weight file is in a different folder, provide the paths accordingly.
- The code can also run on pre-trained Yolov5 weights by specifying the classes properly.
- Future versions may include a speed detection function to calculate the walking speed of people in the video.
  
## Usage

1. Clone the repository:

```
git clone https://github.com/Nbn03/Yolov5_Person-Detection-and-Tracking.git
cd Yolov5_Person-Detection-and-Tracking
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Run the main script:
```
python main.py
```
