# YouTube Video Downloader and Catalog Organizer

This program allows you to download YouTube videos and organize them by creating directories based on the authors' names. You can customize the title and author of a video, and specify a path where the program will automatically create the corresponding directories.

## Features
- Accepts a YouTube video link as input.
- Allows you to specify a custom title and author for the video.
- Downloads videos in different resolutions (high, low) or as audio-only files.
- Creates directories based on the author's name.
- Organizes your videos efficiently into the specified path.

## How It Works
1. **Input the YouTube Video Link**: Provide the URL of the YouTube video you want to download.
2. **Customize Video Metadata**: Enter a custom title and author for the video.
3. **Specify the Path**: Define the root directory where the program will create the author's catalog.
4. **Download Options**: Choose between downloading audio-only, low-resolution, or high-resolution versions of the video.
5. **Organized Storage**: The program creates a folder for the author and stores the downloaded video or audio within the specified path.

## Installation
To use this program, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/maciejblawat/YouTube-Video-Downloader.git
   ```
2. Navigate to the project directory:
   ```bash
   cd youtube-video-catalog-organizer
   ```
3. Install the required dependencies using pip:
   ```bash
   pip install tkinter pytube pyglet
   ```

## Usage
Run the program by executing the following command:
```bash
python "youtube video downloader.py"
```

### Example Workflow
1. Input: `https://www.youtube.com/watch?v=dQw4w9WgXcQ`
2. Title: `Never Gonna Give You Up`
3. Author: `Rick Astley`
4. Path: `/Users/username/YouTubeVideos`

The program will create the following structure:
```
/Users/username/YouTubeVideos
|-- Rick Astley
    |-- Never Gonna Give You Up
```


