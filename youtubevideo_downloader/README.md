# YouTube Video Downloader 🎬⬇️

A Python GUI application that downloads YouTube videos in MP4 format with the highest available resolution.

## Features 
-  Simple GUI folder selection
-  One-click downloading
-  Automatic highest resolution selection
-  Progressive stream support (video+audio)
-  Error handling for invalid URLs/paths

## Requirements 
- Python 3.6+
- Required packages:
  ```bash
  pip install pytube tkinter
# Installation & Usage 
1. ### Install dependencies:
   ```bash
     pip install pytube
   ```
2. ### Run the downloader:
   ```bash
     python youtube_downloader.py
   ```
3. ## Follow Prompts 
- Enter YouTube URL when prompted  
- Select download directory via file dialog  
- View download progress in the console
4.## Code Structure 

###  Core Functions:
- `download_video(url, save_path)` — Handles the actual download  
- `open_file_dialog()` — Opens the GUI folder selector

###  Main Execution Flow:
1. Get YouTube URL from user input  
2. Open folder selection dialog  
3. Download video to selected location
## Example Usage 
<pre>
Please enter a YouTube URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
Selected folder: C:/Users/You/Videos
Started download...
Video downloaded successfully!</pre>
## Customization Options 

- **Change download format** by modifying:
  ```python
  streams.filter(progressive=True, file_extension="mp4")
  ```
- **Add resolution preference**:
  ```python
  streams.filter(res="1080p")  # For specific resolution
  ```
- **Add a download progress bar using pytube's callback functions**
## Known Limitations 

- Doesn't handle age-restricted content  
- May not work with some live streams  
- No playlist/download queue support

---

## Troubleshooting 

| Issue              | Solution                                      |
|--------------------|-----------------------------------------------|
| `URLError`         | Check internet connection                     |
| `RegexMatchError`  | Verify YouTube URL is correct                 |
| Permission errors  | Run as admin or choose a different folder     |
## License 

MIT License – free for personal and educational use.
