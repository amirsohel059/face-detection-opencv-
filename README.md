## Face Recognition using Raspy

This repository contains code for performing face recognition and detection using OpenCV and dlib on a Raspberry Pi. The face recognition part is based on reference code from Core Electronics, with some updates. You can find the original blog post [here](https://core-electronics.com.au/guides/face-identify-raspberry-pi/).

### Materials Required
- Raspberry Pi 4B/5
- Camera module
- SD card flashed with the latest OS

### Getting Started
1. Flash your SD card with the provided image. The recommended image is 64 Bookworm.
2. Install all the necessary libraries mentioned below.

### Installation
You need to install the following libraries on your Raspberry Pi:
- OpenCV
- CMake
- dlib
- Face Recognition Library

#### Guides for Installation:
- [Guide to Install OpenCV](https://qengineering.eu/install%20opencv%20on%20raspberry%20pi%205.html)
- Guide to Install CMake and dlib [here](https://core-electronics.com.au/guides/face-identify-raspberry-pi/).

### Usage
1. Clone this GitHub repository to your local machine.
2. Open the `headshots.py` file in either Tony or Ginny and run it.
3. Take photos by pressing the space button. Note: There might be a small terminal window you need to type 'space'  in that window to take the images.
4. After taking several images (e.g., 8), close the terminal.
5. Move the faces to a folder named `dataset` and create a subfolder with your name. For example, `dataset/amir`, and paste all the images inside it.
6. Open the `train.py` file and run it to train the faces. This will create an `encodings.py` file.
7. Open the `facial_req.py` file to start using the face recognition system.

### Note
Ensure that your Raspberry Pi is adequately configured and all hardware components are connected properly before running the code.

### Disclaimer
This project is provided as-is without any warranty. Use it at your own risk.

### Contribution
Contributions are welcome! If you find any bugs or have suggestions for improvement, feel free to create a pull request or open an issue.

### License
This project is licensed under the [MIT License](LICENSE).
