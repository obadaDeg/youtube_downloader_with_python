import tkinter as tk
from tkinter import ttk
from pytube import YouTube


class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")

        
        tk.Label(root, text="Enter YouTube URL:").grid(
            row=0, column=0, padx=10, pady=10
        )
        self.url_entry = tk.Entry(root, width=40)
        self.url_entry.grid(row=0, column=1, padx=10, pady=10)

        
        self.download_button = tk.Button(
            root, text="Download", command=self.download_video
        )
        self.download_button.grid(row=0, column=2, padx=10, pady=10)

        
        self.progress = ttk.Progressbar(
            root, orient="horizontal", length=300, mode="determinate"
        )
        self.progress.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

    def download_video(self):
        url = self.url_entry.get()
        yt = YouTube(url, on_progress_callback=self.progress_callback)
        stream = yt.streams.get_highest_resolution()
        stream.download(output_path="YOUR_PATH")

    def progress_callback(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        percent_complete = (total_size - bytes_remaining) / total_size * 100
        self.progress["value"] = percent_complete
        self.root.update_idletasks()


if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
