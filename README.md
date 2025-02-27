# Automated Transcription System

## Overview
The **Automated Transcription System** is a Python-based application that leverages OpenAI's Whisper model to transcribe audio and video files in real time. It features a user-friendly GUI built with Tkinter and automatically monitors a selected folder for new media files, transcribing them upon detection.

## Features
- **Real-time Transcription:** Watches a folder for new audio/video files and transcribes them automatically.
- **GUI Interface:** Provides an intuitive interface for selecting folders and managing transcriptions.
- **Whisper Model Integration:** Uses OpenAI's Whisper model for high-quality speech-to-text conversion.
- **Multi-Format Support:** Supports common media file types including MP3, WAV, MP4, MKV, and more.
- **Efficient Processing:** Avoids duplicate processing of already transcribed files.

## Installation
### Prerequisites
Ensure you have Python installed (Python 3.8+ recommended) and install the required dependencies:
```bash
pip install torch whisper tkinter watchdog
```
### Running the Application
Clone this repository:

```Bash

git clone [https://github.com/yourusername/transcription-system.git](https://github.com/yourusername/transcription-system.git)
```
Navigate to the project directory:

```Bash

cd transcription-system
```
Run the application:

```Bash

python realtime_transcriber.py
```

## How to Use
 - Select Folder: Choose a directory where media files will be monitored.
 - Start Monitoring: Click the "Start Monitoring" button to begin automatic transcription.
 - View Logs: The GUI displays updates on detected files and transcription progress.
 - Stop Monitoring: Click "Stop Monitoring" to stop the process.
## Supported File Formats
 - Audio: MP3, WAV, AAC, M4A
 - Video: MP4, MKV, MOV, FLV
## Future Enhancements
 - Support for more languages.
 - Cloud storage integration for transcriptions.
 - Live audio recording and transcription.
   
### License
 - This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
OpenAI for the Whisper model.
Python community for libraries like Tkinter and Watchdog.
Contribute
Feel free to submit issues or pull requests to improve this project!

## Contact
For any questions or suggestions, reach out via GitHub issues.
