# YouTube Downloader with Python

A versatile Python application for downloading YouTube videos and audio with a user-friendly interface.

![YouTube Downloader](assets/logo.png)

## Features

- Download individual YouTube videos in various resolutions (144p to 1080p)
- Download entire YouTube playlists
- Convert videos to audio files (MP3, M4A, WAV, FLAC, AAC, etc.)
- Simple and intuitive graphical user interface
- Select download path and quality options
- Progress tracking for downloads

## Requirements

- Python 3.6+
- Required packages:
  - pytube
  - pydub
  - tkinter
  - re

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/youtube_downloader_with_python.git
   cd youtube_downloader_with_python
   ```

2. Install required packages:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   python main.py
   ```

## Usage

### GUI Application

1. Launch the application by running `main.py`
2. Enter the YouTube URL (video or playlist)
3. Select the desired quality
4. Choose the download path
5. Select whether to download as video or audio
6. Click the download button

### Command Line Interface

For quick downloads, you can also use the command line scripts:

- To download a single video:
  ```
  python vider_dowloader.py
  ```

- To download audio only:
  ```
  python voice_downloader.py
  ```

- To download a playlist:
  ```
  python playlist_downloader.py
  ```

## Project Structure

- `main.py` - Main application GUI
- `downloading_services.py` - Core download functionality
- `test.py` - Alternative GUI implementation
- `playlist_downloader.py` - Script for downloading playlists
- `vider_dowloader.py` - Script for downloading single videos
- `voice_downloader.py` - Script for downloading audio from videos
- `utils/qualities.py` - Enums for video and audio quality options
- `assets/` - Contains images for the GUI

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- [pytube](https://github.com/pytube/pytube) for providing YouTube download functionality
- [pydub](https://github.com/jiaaro/pydub) for audio conversion
