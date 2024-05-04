import os
import pytube


def download_video(video, resolution):
    stream = video.streams.filter(res=resolution).first()
    if stream is None:
        print(f"Stream with resolution {resolution} not available. Downloading the next best quality.")
        stream = video.streams.filter(res="720p").first()  
    print(f"Downloading video {video.title} with resolution {stream.resolution}...")
    stream.download(output_path=save_path)


playlist_url = input("Enter the URL of the YouTube playlist: ")


save_path = input("Enter the path to save the videos (e.g. /home/user/Desktop/videos): ")
os.makedirs(save_path, exist_ok=True)


resolution = input("Enter the desired video quality (e.g. 1080p): ")


playlist = pytube.Playlist(playlist_url)


for video_url in playlist.video_urls:
    video = pytube.YouTube(video_url)
    download_video(video, resolution)

print("All videos downloaded successfully!")



