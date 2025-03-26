# YouTube MP3 Downloader

A Flask web application that allows users to download MP3 audio from YouTube videos. This application provides a simple web interface where users can input multiple YouTube URLs and download them as MP3 files.

## Features

- Download MP3 audio from YouTube videos
- Support for multiple URL downloads simultaneously
- Simple and intuitive web interface
- Concurrent processing using ThreadPoolExecutor
- High-quality audio output (192kbps)

## Prerequisites

- Python 3.x
- FFmpeg (required for audio conversion)
- Flask
- yt-dlp

## Installation

1. Clone this repository:

```bash
git clone <your-repository-url>
cd render
```

2. Install the required Python packages:

```bash
pip install flask yt-dlp
```

3. Install FFmpeg:
   - Windows: Download from [FFmpeg official website](https://ffmpeg.org/download.html)
   - Linux: `sudo apt-get install ffmpeg`
   - macOS: `brew install ffmpeg`

## Usage

1. Start the Flask application:

```bash
python app.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

3. Enter one or more YouTube URLs (one per line) in the text area
4. Click the download button to start the conversion process
5. The MP3 files will be saved in the `downloads` directory

## Project Structure

```
render/
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   └── index.html     # Main web interface
└── downloads/         # Directory for downloaded MP3 files
```

## Technical Details

- The application uses `yt-dlp` for YouTube video downloading
- Audio conversion is handled by FFmpeg
- Downloads are processed concurrently using ThreadPoolExecutor
- MP3 files are saved with 192kbps quality

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
