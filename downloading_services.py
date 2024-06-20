import os
from pytube import YouTube, Playlist
from pydub import AudioSegment
import re


def is_playlist(url):
    playlist_pattern = re.compile(r"(?:list=)([a-zA-Z0-9-_]+)")
    return bool(playlist_pattern.search(url))


def get_next_highest_resolution(yt, current_quality):
    video_streams = yt.streams.filter(progressive=True, file_extension="mp4").order_by(
        "resolution"
    )

    for stream in video_streams:
        if stream.resolution and stream.resolution >= current_quality:
            return stream.resolution
    return video_streams[-1].resolution if video_streams else None


def get_next_highest_audio_bitrate(yt, current_bitrate):
    audio_streams = yt.streams.filter(only_audio=True).order_by("abr")

    for stream in audio_streams:
        if stream.abr and int(stream.abr[:-4]) >= current_bitrate:
            return stream.abr
    return audio_streams[-1].abr if audio_streams else None


def download_audio(url, desired_bitrate, output_path="output"):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    yt = YouTube(url)

    chosen_bitrate = get_next_highest_audio_bitrate(yt, desired_bitrate)
    stream = yt.streams.filter(abr=chosen_bitrate, only_audio=True).first()
    if stream:
        audio_file = stream.download(output_path=output_path)
        base, _ = os.path.splitext(audio_file)
        mp3_file = base + ".mp3"

        audio = AudioSegment.from_file(audio_file)
        audio.export(mp3_file, format="mp3")
        os.remove(audio_file)

        print(f"Audio downloaded and converted to mp3: {mp3_file}")
        return mp3_file
    else:
        print(f"No matching audio stream found for {yt.title} at {desired_bitrate}")


def download_video(url, desired_quality, destination):
    yt = YouTube(url)

    chosen_resolution = get_next_highest_resolution(yt, desired_quality)
    stream = yt.streams.filter(
        res=chosen_resolution, progressive=True, file_extension="mp4"
    ).first()
    if stream:
        stream.download(output_path=destination)
        print(f"Video downloaded successfully: {yt.title}")
    else:
        print(f"No matching stream found for {yt.title} at {desired_quality}")


def download_playlist(url, quality, destination, audio=False):
    playlist = Playlist(url)
    for video in playlist.videos:
        if audio:
            download_audio(video.watch_url, quality, destination)
        else:
            download_video(video.watch_url, quality, destination)
    print("Playlist downloaded successfully.")

