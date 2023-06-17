# FingerCounting-OpenCV-Arduino

## About
This project utilizes OpenCV and Arduino to count fingers based on image processing techniques and control LEDs accordingly.
The system captures hand gestures using a camera, processes them using OpenCV algorithms to detect the number of fingers in the image,
and sends this information to the Arduino board. The Arduino board then turns on/off the corresponding number of LEDs based on the number of fingers detected.

## Hand Landmark Model
* After the palm detection over the whole image our subsequent hand landmark model performs precise keypoint localization of 21 3D hand-knuckle coordinates inside the detected hand regions via regression, that is direct coordinate prediction. The model learns a consistent internal hand pose representation and is robust even to partially visible hands and self-occlusions.
![ddd](https://user-images.githubusercontent.com/115498182/236805586-37eac86a-7fb3-4c0b-b9dd-3ef1a5bfe2f4.png)

## Libraries

* ## OpenCV
  * It is a popular open-source computer vision library that provides various tools and algorithms for image and video processing.
In this project, OpenCV is used to capture images from a camera, apply image processing techniques to detect hand gestures,
and count fingers based on the number of detected landmarks.

* ## Mediapipe 
  * It is a cross-platform, customizable framework for building machine learning pipelines that can process various types of data such as image,
video, and audio. In this project, Mediapipe is used to detect hand landmarks in the captured image,
which are then used to calculate the angle between the thumb and the index finger.

* ## Math
  * It is a standard Python library that provides various mathematical operations and functions. In this project,
it is used to perform mathematical calculations required for finger counting, such as calculating the angle between the thumb and the index finger.

* ## Pyserial
  * It is a Python library that provides tools for serial communication between a computer and an external device such as an Arduino board.
In this project, Pyserial is used to establish a serial communication link between the computer and the Arduino board to send the finger count information,
which is then used to control the corresponding number of LEDs based on the number of fingers detected.

## Did you find this repository helpful?
Do not forget to give a start

## Didn't you?
Then fork this repo, make it BETTER and do not forget to give a STAR
