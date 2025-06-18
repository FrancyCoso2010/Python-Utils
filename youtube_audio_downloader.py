import os
from yt_dlp import YoutubeDL

# === Configuration ===

# Folder where audio files will be saved
DOWNLOAD_FOLDER = r"PATH_TO\download\folder"

# List of song titles to search and download from YouTube
SONG_TITLES = [
    "Title 1",
    "Title 2"
]

# Path to your FFmpeg installation
FFMPEG_PATH = r"C:\ffmpeg-7.1.1-essentials_build\bin"

# === Ensure target folder exists ===
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

# === yt-dlp options ===
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
    'ffmpeg_location': FFMPEG_PATH,
    'noplaylist': True,
    'default_search': 'ytsearch',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'quiet': False,
    'no_warnings': True,
    'ignoreerrors': True,
}

# === Main download loop ===
def download_songs():
    with YoutubeDL(ydl_opts) as ydl:
        for title in SONG_TITLES:
            print(f"\n🔎 Searching and downloading: {title}")
            try:
                ydl.download([title])
            except Exception as e:
                print(f"❌ Error downloading '{title}': {e}")

if __name__ == "__main__":
    download_songs()
