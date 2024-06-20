from pytube import YouTube
from pydub import AudioSegment
import os


def download_audio(url, output_path="output"):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    # Download video from YouTube
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    audio_file = video.download(output_path=output_path)

    # Convert to .mp3 format
    base, ext = os.path.splitext(audio_file)
    mp3_file = base + ".mp3"
    audio = AudioSegment.from_file(audio_file)
    audio.export(mp3_file, format="mp3")

    # Remove the original audio file
    os.remove(audio_file)

    return mp3_file


# URL of the YouTube video
url = "https://www.youtube.com/watch?v=MGSTRJmN2VQ"
audio_file_path = download_audio(url)
print(f"Audio file saved at: {audio_file_path}")
