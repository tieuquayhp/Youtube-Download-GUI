import tkinter as tk
from tkinter import ttk, filedialog
import yt_dlp
import os
from textual.app import App, ComposeResult
from textual.widgets import Static
from textual.containers import Container

class ConsoleApp(App):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.static = Static("")

    def compose(self) -> ComposeResult:
        yield Container(self.static)

    def on_mount(self):
        self.static.update("Sẵn sàng tải video...\n")

    def append_text(self, text):
        self.static.update(self.static.renderable + text)

class YoutubeDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Downloader")

        # URL video
        url_label = ttk.Label(self, text="URL video:")
        url_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        self.url_entry = ttk.Entry(self, width=50)
        self.url_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        # Định dạng file
        format_label = ttk.Label(self, text="Định dạng:")
        format_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
        self.format_combobox = ttk.Combobox(self, values=["mp4", "webm", "mkv", "mp3 (chỉ âm thanh)"])
        self.format_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        # Đường dẫn lưu
        path_label = ttk.Label(self, text="Lưu vào:")
        path_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        self.path_entry = ttk.Entry(self, width=40)
        self.path_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        browse_button = ttk.Button(self, text="Duyệt", command=self.browse_path)
        browse_button.grid(row=2, column=2, padx=5, pady=5)

        # Nút tải xuống
        download_button = ttk.Button(self, text="Tải xuống", command=self.download_videos)
        download_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10)

        # Nút mở thư mục
        open_button = ttk.Button(self, text="Mở thư mục", command=self.open_output_folder)
        open_button.grid(row=4, column=0, columnspan=3, padx=5, pady=5)

        # Hiển thị trạng thái
        self.status_label = ttk.Label(self, text="")
        self.status_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

        self.console_app = ConsoleApp()

    def download_videos(self):
        url = self.url_entry.get()
        file_format = self.format_combobox.get()
        output_path = self.path_entry.get()

        ydl_opts = {
            'outtmpl': output_path + '/%(title)s.%(ext)s',
            'extract_flat': True,
            'logger': MyLogger(self.console_app),
            'progress_hooks': [self.update_status],
        }

        if file_format == 'mp3 (chỉ âm thanh)':
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        else:
            ydl_opts['format'] = file_format

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        self.status_label.config(text="Tải xuống hoàn tất!")

    def browse_path(self):
        path = filedialog.askdirectory()
        self.path_entry.delete(0, tk.END)
        self.path_entry.insert(0, path)

    def open_output_folder(self):
        output_path = self.path_entry.get()
        if os.path.exists(output_path):
            os.startfile(output_path)
        else:
            self.status_label.config(text="Thư mục không tồn tại!")

    def update_status(self, info_dict):
        if info_dict['status'] == 'finished':
            self.status_label.config(text="Tải xuống hoàn tất!")

class MyLogger:
    def __init__(self, app):
        self.app = app

    def debug(self, msg):
        self.app.append_text(msg + "\n")

    def warning(self, msg):
        self.app.append_text(msg + "\n")

    def error(self, msg):
        self.app.append_text(msg + "\n")

if __name__ == '__main__':
    app = YoutubeDownloader()
    app.console_app.run()
    app.mainloop()
