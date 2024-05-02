import os
import pytube

# function to download the video with the given resolution
def download_video(video, resolution):
    stream = video.streams.filter(res=resolution).first()
    if stream is None:
        print(f"Stream with resolution {resolution} not available. Downloading the next best quality.")
        stream = video.streams.filter(res="720p").first()  # download 720p if 1080p is not available
    print(f"Downloading video {video.title} with resolution {stream.resolution}...")
    stream.download(output_path=save_path)

# get the playlist URL from the user
playlist_url = input("Enter the URL of the YouTube playlist: ")

# create a folder to save the videos
save_path = input("Enter the path to save the videos (e.g. /home/user/Desktop/videos): ")
os.makedirs(save_path, exist_ok=True)

# get the desired video quality from the user
resolution = input("Enter the desired video quality (e.g. 1080p): ")

# create the playlist object
playlist = pytube.Playlist(playlist_url)

# iterate over the videos in the playlist and download them
for video_url in playlist.video_urls:
    video = pytube.YouTube(video_url)
    download_video(video, resolution)

print("All videos downloaded successfully!")



