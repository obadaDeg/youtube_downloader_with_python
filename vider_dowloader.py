from pytube import YouTube


def download_video(url, quality, destination):
    try:
        yt = YouTube(url)
        if quality.lower() == "highest":
            stream = yt.streams.get_highest_resolution()
        elif quality.lower() == "lowest":
            stream = yt.streams.get_lowest_resolution()
        elif quality.lower() == "audio":
            stream = yt.streams.filter(only_audio=True).first()

        if stream:
            stream.download(output_path=destination)
            print("Video downloaded successfully.")
        else:
            print("No matching stream found.")
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    url = input("Enter the YouTube video URL: ")
    quality = input("Enter the desired quality (highest, lowest, audio): ")
    destination = input("Enter the destination directory: ")

    download_video(url, quality, destination)
