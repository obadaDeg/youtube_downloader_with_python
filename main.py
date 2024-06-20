import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import re

class YouTubeDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1000x600")
        self.root.title("YouTube Downloader")
        self.root.configure(bg='white')
        self.setup_ui()

    def setup_ui(self):
        self.create_image_frame()
        self.create_main_labels()
        self.create_download_frames()
        self.create_input_frame()

    def create_image_frame(self):
        self.image_frame = tk.Frame(self.root)
        self.image_frame.place(x=0, y=0, width=500, height=550)

        self.image1 = tk.PhotoImage(file="assets/main_frame_image.png")
        self.image11 = tk.Label(self.image_frame, image=self.image1, bg='white')
        self.image11.pack(side=tk.TOP, fill=tk.Y, expand=True)

        self.label1 = tk.PhotoImage(file="assets/logo.png")
        self.label11 = tk.Label(self.image_frame, image=self.label1, bg='white')
        self.label11.place(x=10, y=0)

        self.text_label = tk.Label(self.image_frame, text="YouAAUP", font=('Arial', 16), bg='white', fg='#360DB3')
        self.text_label.place(x=10 + self.label1.width() + 10, y=0 + self.label1.height() // 2 - 12)

    def create_main_labels(self):
        self.text_label1 = tk.Label(self.root, text="   YouTube Converter", font=('Arial', 14), bg='white', fg='#360DB3')
        self.text_label1.place(x=10 + self.image1.width() + 10, y=0 + self.label1.height() // 2 - 12)

        self.text_label2 = tk.Label(self.root, text="          Downloaded", font=('Arial', 14), bg='white', fg='#360DB3')
        self.text_label2.place(x=30 + self.image1.width() + self.text_label.winfo_reqwidth() * 2, y=self.label1.height() // 2 - 12)
        self.text_label2.bind("<Button-1>", self.open_downloaded_page)  # Add this line to bind the label to the function

    def create_download_frames(self):
        self.canvas1 = tk.Canvas(self.root, bg='#360DB3', highlightthickness=0)
        self.canvas1.place(x=10 + self.image1.width() + 10, y=self.text_label1.winfo_reqheight() * 4, width=202, height=202)
        self.frame1 = tk.Frame(self.root, bg='white')
        self.frame1.place(x=10 + self.image1.width() + 10, y=self.text_label1.winfo_reqheight() * 4, width=200, height=200)
        self.frame1.bind("<Button-1>", self.change_bg_color_frame1)

        self.listphotopath = tk.PhotoImage(file="assets/Sound_fill_selected.png")
        self.listphoto = tk.Label(self.frame1, image=self.listphotopath, bg='white')
        self.listphoto.place(x=70, y=self.text_label1.winfo_reqheight() * 2 - 15)
        self.listphoto.bind("<Button-1>", self.change_bg_color_frame1)
        self.text_label3 = tk.Label(self.frame1, text="Download Audio", font=('Arial', 14), fg='#360DB3', bg='white')
        self.text_label3.place(x=20, y=self.text_label1.winfo_reqheight() * 4 - 12)
        self.text_label3.bind("<Button-1>", self.change_bg_color_frame1)

        self.canvas2 = tk.Canvas(self.root, bg='#360DB3', highlightthickness=0)
        self.canvas2.place(x=10 + self.image1.width() + 70 + self.text_label3.winfo_reqwidth(), y=self.text_label1.winfo_reqheight() * 4, width=202, height=202)
        self.frame2 = tk.Frame(self.root, bg='white')
        self.frame2.place(x=10 + self.image1.width() + 70 + self.text_label3.winfo_reqwidth(), y=self.text_label1.winfo_reqheight() * 4, width=200, height=200)
        self.frame2.bind("<Button-1>", self.change_bg_color_frame2)

        self.listphotopath1 = tk.PhotoImage(file="assets/single_video_button.png")
        self.listphoto1 = tk.Label(self.frame2, image=self.listphotopath1, bg='white')
        self.listphoto1.place(x=70, y=self.text_label1.winfo_reqheight() * 2 - 15)
        self.listphoto1.bind("<Button-1>", self.change_bg_color_frame2)
        self.text_label4 = tk.Label(self.frame2, text="Download single", font=('Arial', 14), fg='#360DB3', bg='white')
        self.text_label4.place(x=20, y=self.text_label1.winfo_reqheight() * 4 - 12)
        self.text_label4.bind("<Button-1>", self.change_bg_color_frame2)

    def create_input_frame(self):
        self.frame3 = tk.Frame(self.root, bg='white')
        self.frame3.place(x=10 + self.image1.width() + 10, y=320, width=420, height=300)

        self.text_label5 = tk.Label(self.frame3, text="Select Download Method", font=('Arial', 12), fg='#360DB3', bg='white')
        self.text_label5.place(x=120, y=12)

        self.text_field = tk.Text(self.frame3, height=0, width=50)
        self.text_field.insert("1.0", 'URL')
        self.text_field.config(fg='grey')
        self.text_field.bind("<FocusIn>", self.on_entry_click)
        self.text_field.bind("<Return>", self.on_enter_press)
        self.text_field.place(x=0, y=40)

        self.options = ["1080px", "720px", "px", "px"]
        self.selected_option = tk.StringVar()
        self.dropdown = ttk.Combobox(self.frame3, textvariable=self.selected_option, values=self.options)
        self.dropdown.place(x=0, y=65)
        self.dropdown.current(0)
        self.dropdown.bind("<Button-1>", self.selectdrop1)

        self.text_field1 = tk.Text(self.frame3, height=0, width=50)
        self.text_field1.insert("1.0", 'select the path')
        self.text_field1.config(fg='grey')
        self.text_field1.bind("<FocusIn>", self.on_entry_click1)
        self.text_field1.bind("<Return>", self.on_enter_press1)
        self.text_field1.place(x=0, y=90)

        self.listphotopath2 = tk.PhotoImage(file="assets/icons8-browse-64.png")
        self.listphoto2 = tk.Label(self.frame3, image=self.listphotopath2, text='brows', bg='white', width=200, height=50)
        self.listphoto2.place(x=250, y=85)
        self.listphoto2.bind("<Button-1>", self.brows)

        self.listphotopath3 = tk.PhotoImage(file="assets/down.png")
        self.listphoto3 = tk.Label(self.frame3, image=self.listphotopath3, text='brows', bg='white', width=200, height=50)
        self.listphoto3.place(x=120, y=160)
        self.listphoto3.bind("<Button-1>", self.download)

        self.text_label7 = tk.Label(self.frame3, text="press the icon to Download", font=('Arial', 12), bg='white', fg='#360DB3')
        self.text_label7.place(x=0, y=175)

    def change_bg_color_frame1(self, event):
        current_color = self.frame1.cget("bg")
        new_color = 'purple' if current_color == 'white' else 'white'
        new_colorframe2 = 'white' if current_color == 'white' else 'white'
        self.frame1.config(bg=new_color)
        self.text_label3.config(bg=new_color)
        self.listphoto.config(bg=new_color)
        self.frame2.config(bg=new_colorframe2)
        self.text_label4.config(bg=new_colorframe2)
        self.listphoto1.config(bg=new_colorframe2)

    def change_bg_color_frame2(self, event):
        current_color = self.frame2.cget("bg")
        new_color = 'purple' if current_color == 'white' else 'white'
        new_colorframe1 = 'white' if current_color == 'white' else 'white'
        self.frame2.config(bg=new_color)
        self.text_label4.config(bg=new_color)
        self.listphoto1.config(bg=new_color)
        self.frame1.config(bg=new_colorframe1)
        self.text_label3.config(bg=new_colorframe1)
        self.listphoto.config(bg=new_colorframe1)

    def on_entry_click(self, event):
        if self.text_field.get("1.0", "end-1c") == 'URL':
            self.text_field.delete("1.0", "\end")
            self.text_field.config(fg='black')

    def on_enter_press(self, event):
        content = self.text_field.get("1.0", "end-1c")
        print(content)
        self.root.focus()

    def selectdrop1(self, event):
        self.root.focus()

    def on_entry_click1(self, event):
        if self.text_field1.get("1.0", "end-1c") == 'select the path':
            self.text_field1.delete("1.0", "end")
            self.text_field1.config(fg='black')

    def on_enter_press1(self, event):
        content = self.text_field1.get("1.0", "end-1c")
        print(content)
        self.root.focus()

    def brows(self, event=None):
        file_path = filedialog.askdirectory()
        self.text_field1.delete("1.0", "end")
        self.text_field1.insert("1.0", file_path)
        print(file_path)

    def download(self, event=None):
        # Add download functionality here
        pass

    def open_downloaded_page(self, event):
        new_window = tk.Toplevel(self.root)
        new_window.geometry("600x400")
        new_window.title("Downloaded Videos")
        new_window.configure(bg='white')

        tk.Label(new_window, text="Downloaded Videos", font=('Arial', 16), bg='white', fg='#360DB3').pack(pady=10)

        # Example content - replace with your actual downloaded videos logic
        videos_frame = tk.Frame(new_window, bg='white')
        videos_frame.pack(fill=tk.BOTH, expand=True)

        video_list = ["Video 1", "Video 2", "Video 3"]  # Replace with your list of downloaded videos
        for video in video_list:
            tk.Label(videos_frame, text=video, font=('Arial', 14), bg='white', fg='#360DB3').pack(pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    icon = tk.PhotoImage(file="assets/logo.png")
    root.iconphoto(False, icon)
    root.grid_columnconfigure(1, weight=1)
    root.grid_rowconfigure(1, weight=1)
    app = YouTubeDownloaderApp(root)
    root.mainloop()
