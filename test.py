import tkinter as tk
from tkinter import filedialog, ttk
from pytube import YouTube, Playlist
from utils.qualities import VideoQualities, AudioQualities


def download_video(url, quality, destination):
    try:
        yt = YouTube(url)
        if quality == VideoQualities.FHD_1080P.value:
            stream = yt.streams.filter(res="1080p", file_extension="mp4").first()
        elif quality == VideoQualities.HD_720P.value:
            stream = yt.streams.filter(res="720p", file_extension="mp4").first()
        else:
            stream = yt.streams.get_highest_resolution()

        if stream:
            stream.download(output_path=destination)
            print("Video downloaded successfully.")
        else:
            print("No matching stream found.")
    except Exception as e:
        print("Error:", e)


def download_playlist(url, quality, destination):
    try:
        playlist = Playlist(url)
        for video in playlist.videos:
            download_video(video.watch_url, quality, destination)
        print("Playlist downloaded successfully.")
    except Exception as e:
        print("Error:", e)


def download_audio(url, quality, destination):
    try:
        yt = YouTube(url)
        stream = yt.streams.filter(only_audio=True).first()
        if quality == AudioQualities.MP3.value:
            stream = stream.filter(file_extension="mp4").first()
        elif quality == AudioQualities.M4A.value:
            stream = stream.filter(file_extension="m4a").first()
        elif quality == AudioQualities.WAV.value:
            stream = stream.filter(file_extension="wav").first()
        elif quality == AudioQualities.FLAC.value:
            stream = stream.filter(file_extension="flac").first()
        elif quality == AudioQualities.AAC.value:
            stream = stream.filter(file_extension="aac").first()
        elif quality == AudioQualities.VORBIS.value:
            stream = stream.filter(file_extension="webm").first()
        elif quality == AudioQualities.OPUS.value:
            stream = stream.filter(file_extension="webm").first()

        if stream:
            stream.download(output_path=destination)
            print("Audio downloaded successfully.")
        else:
            print("No matching stream found.")
    except Exception as e:
        print("Error:", e)


class TubeTunesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("TubeTunes Downloader")
        self.root.configure(bg="#ffffff")  # Set background color

        # Font and colors
        label_font = ("Arial", 12)
        button_font = ("Arial", 10, "bold")
        label_fg = "#333"
        button_bg = "#6a0dad"
        button_fg = "white"

        # Create widgets
        self.url_label = tk.Label(
            root, text="Enter YouTube URL:", font=label_font, fg=label_fg, bg="#ffffff"
        )
        self.url_entry = tk.Entry(root, width=50)
        self.quality_label = tk.Label(
            root, text="Select Quality:", font=label_font, fg=label_fg, bg="#ffffff"
        )
        self.quality_combo = ttk.Combobox(
            root, values=VideoQualities.list() + ["Audio"], state="readonly"
        )
        self.quality_combo.current(0)
        self.destination_label = tk.Label(
            root,
            text="Select Download Location:",
            font=label_font,
            fg=label_fg,
            bg="#ffffff",
        )
        self.destination_button = tk.Button(
            root,
            text="Browse",
            command=self.browse_destination,
            font=button_font,
            bg=button_bg,
            fg=button_fg,
        )
        self.destination_entry = tk.Entry(root, width=50)
        self.download_button = tk.Button(
            root,
            text="Download",
            command=self.start_download,
            font=button_font,
            bg=button_bg,
            fg=button_fg,
        )
        self.type_label = tk.Label(
            root, text="Download Type:", font=label_font, fg=label_fg, bg="#ffffff"
        )
        self.download_type = tk.StringVar()
        self.download_type.set("Single")
        self.single_radio = tk.Radiobutton(
            root,
            text="Single Download",
            variable=self.download_type,
            value="Single",
            font=label_font,
            fg=label_fg,
            bg="#ffffff",
        )
        self.playlist_radio = tk.Radiobutton(
            root,
            text="Download Playlist",
            variable=self.download_type,
            value="Playlist",
            font=label_font,
            fg=label_fg,
            bg="#ffffff",
        )

        # Layout
        self.url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.url_entry.grid(row=0, column=1, padx=5, pady=5, columnspan=2)
        self.quality_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.quality_combo.grid(row=1, column=1, padx=5, pady=5)
        self.destination_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.destination_button.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.destination_entry.grid(row=2, column=2, padx=5, pady=5)
        self.type_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
        self.single_radio.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.playlist_radio.grid(row=3, column=2, padx=5, pady=5, sticky="w")
        self.download_button.grid(row=4, column=0, columnspan=3, pady=10)

    def browse_destination(self):
        folder = filedialog.askdirectory()
        self.destination_entry.delete(0, tk.END)
        self.destination_entry.insert(0, folder)

    def start_download(self):
        url = self.url_entry.get().strip()
        quality = self.quality_combo.get()
        destination = self.destination_entry.get().strip()
        download_type = self.download_type.get()

        if download_type == "Single":
            download_video(url, quality, destination)
        else:
            download_playlist(url, quality, destination)


if __name__ == "__main__":
    root = tk.Tk()
    app = TubeTunesApp(root)
    root.mainloop()
