# 🤖 PyAutoGUI Automation Demo

![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python&logoColor=white)
![PyPI](https://img.shields.io/badge/PyPI-PyAutoGUI-orange)
![License](https://img.shields.io/badge/License-MIT-green)

A **powerful Python automation script** demonstrating the capabilities of [`PyAutoGUI`](https://pypi.org/project/PyAutoGUI/) to automate mouse, keyboard, and GUI interactions. Perfect for automating repetitive tasks, creating bots, or testing applications.

---

## 📌 Features

- ✅ Detects screen size dynamically.
- ✅ Moves the mouse, clicks, double-clicks, right-clicks, and drags.  
- ✅ Types text with controlled speed and executes keyboard shortcuts.  
- ✅ Takes screenshots and searches for images on screen.  
- ✅ Safety features: `PAUSE` and `FAILSAFE` to prevent errors.  

---

## 🛠️ Installation

Install the main package:

```bash
pip install pyautogui
```
**Optional dependencies for image recognition and screenshots:**
 ```bash
    pip install pillow opencv-python
 ```
▶️ **Usage Example:**
  ```python
  import pyautogui
  import time
  
  # Safety
  pyautogui.PAUSE = 1.0
  pyautogui.FAILSAFE = True
  
  # Screen size
  screen_width, screen_height = pyautogui.size()
  print(f"Screen size: {screen_width}x{screen_height}")
  
  # Mouse actions
  pyautogui.moveTo(500, 500, duration=1)
  pyautogui.click()
  pyautogui.doubleClick()
  pyautogui.rightClick()
  pyautogui.dragTo(600, 600, duration=1)
  
  # Keyboard actions
  pyautogui.write("Hello from PyAutoGUI!", interval=0.1)
  pyautogui.press("enter")
  pyautogui.hotkey("ctrl", "a")
  pyautogui.hotkey("ctrl", "c")
  
  # Screenshot & image search
  screenshot = pyautogui.screenshot("screenshot.png")
  location = pyautogui.locateOnScreen("example.png")
  if location:
      print(f"Found image at: {location}")
  else:
      print("Image not found")
```
---
## 🚀 Features in Action

| Action              | Example                                                   |
| ------------------- | --------------------------------------------------------- |
| Mouse Movement      | Move, click, drag to coordinates                          |
| Keyboard Automation | Type text, press keys, hotkeys                            |
| GUI Interaction     | Take screenshots, locate images                           |
| Safety              | `PAUSE` between actions, `FAILSAFE` top-left corner abort |

---

## 👨‍💻 Author

**Bhargava Teja Golla**  

* 🌐 [LinkedIn](https://www.linkedin.com/in/golla-bhargava-teja/)  
* 💻 [GitHub](https://github.com/<your-username>)


