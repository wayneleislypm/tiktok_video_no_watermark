# TikTok Video Downloader (No Watermark)

## Description
This project is a simple Python script that allows users to download TikTok videos without watermarks. It utilizes the TikWM API to fetch video data and provides a straightforward command-line interface for user interaction.

## Features
- Download TikTok videos without watermarks
- User-friendly input for TikTok video URLs
- Error handling for API responses and network issues

## Installation
To run this project, you need to have Python installed on your machine. You can download Python from [python.org](https://www.python.org/downloads/).

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd tiktok_video_downloader
   ```

2. Install the required dependencies:
   ```bash
   pip install requests
   ```

## Usage
1. Run the script:
   ```bash
   python tiktok_video_downloader.py
   ```

2. Enter the TikTok video URL when prompted.

3. The video will be downloaded as `tiktok_video_no_watermark.mp4` in the current directory.

## Dependencies
- Python 3.x
- requests library

## API Information
This script uses the TikWM API to fetch video data. The API endpoint used is:
```
https://www.tikwm.com/api/?url={url}
```

## Error Handling
The script includes error handling for:
- Invalid URLs
- Network issues
- API response errors

If an error occurs, an appropriate message will be displayed to the user.

## Output
The downloaded video will be saved as `tiktok_video_no_watermark.mp4` in the current working directory.

## Limitations
- The script relies on the TikWM API, which may have rate limits or downtime.
- Ensure that you have permission to download and use the videos as per TikTok's terms of service.

## Potential Improvements
- Add support for downloading multiple videos in a single run.
- Implement a graphical user interface (GUI) for easier use.
- Enhance error handling and logging for better debugging.
