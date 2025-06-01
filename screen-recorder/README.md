# Screen Recorder Application 

A Python screen recording utility that captures your desktop activity and saves it as an MP4 video file.

## Project Level 
**Intermediate** - Suitable for developers with basic Python experience who want to explore:
- Screen capture automation
- Video file handling
- System metrics access
- OpenCV operations

## Features 
- Full-screen capture
- Duration-based recording
- MP4 video output
- 30 FPS smooth recording
- Clean console feedback

## Technical Stack 
```python
import cv2          # Video encoding/processing
import pyautogui    # Screenshot capture
import win32api     # Screen dimensions
import numpy        # Image array conversion
import time         # Duration control
```
## Installation 
- ### Install required packages:
  ```bash
      pip install opencv-python pyautogui numpy pywin32
  ```
- ### Clone the repository:
  ```bash
      git clone https://github.com/bhargavatejagolla/screen-recorder.git
  ```
## Usage
- ### Modify these variables in the script:
    ```python
    output_path = "C:/your/path/recording.mp4"  # Change save location
    dur = 20  # Change recording duration (seconds)
    ```
- ### Run the script: screenrecording.py    
## What it does:
 - Captures the screen for 14 seconds (default)

- Saves the video to your system (path defined in script)

- Prints "ENDED RECORDING" when done

## How It Works:
- Gets screen dimensions using GetSystemMetrics

- Takes screenshots with pyautogui

- Converts screenshots to OpenCV format

- Writes frames to .mp4 using cv2.VideoWriter

- Stops after a set duration

## Customization: 
- Duration: Modify dur = 10 + 4 to change the recording time.

- File path: Change output_path to your preferred location.

- FPS: Adjust the frame rate (currently set to 30.0).
  
## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT) — free for personal and educational use.









    
