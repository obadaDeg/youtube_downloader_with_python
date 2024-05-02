import pytube

# ask for YouTube URL and desired quality
url = input("Enter YouTube URL: ")
quality = input(
    "Enter desired quality (or press Enter for highest available quality): "
)

# create YouTube object
yt = pytube.YouTube(url)

# create list of available itags
itag_list = []
for stream in yt.streams:
    itag_list.append(stream.itag)
print(itag_list)

# choose stream with desired quality
if quality:
    stream = yt.streams.filter(res=quality).first()
else:
    stream = yt.streams.get_highest_resolution()

# download stream
stream.download()
print("Video downloaded successfully!")
