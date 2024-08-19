import tkinter as tk
from tkinter import ttk, filedialog
import yt_dlp
import os
#Create folder
def createfolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. '+directory)
def select_file():
        #allow user to select a path from the exporler
        path = filedialog.askopenfilename(
            title="Chọn file dữ liệu",
            filetypes=[("Tệp dữ liệu", "*.txt"), ("Tất cả các tệp", "*.*")])
            
        selectfile_entry.insert(0,path)

def download_video():
    file_input = selectfile_entry.get()
    video_link = open(file_input, 'r')
    file_format = format_combobox.get()
    output_path = path_entry.get()
    for url in video_link:
        ydl_opts = {
            'outtmpl': output_path + '/%(title)s.%(ext)s',
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

    status_label.config(text="Tải xuống hoàn tất!")
    
def browse_path():
    path = filedialog.askdirectory()
    path_entry.delete(0, tk.END)
    path_entry.insert(0, path)
def open_output_folder():
    output_path = path_entry.get()
    if os.path.exists(output_path):
        os.startfile(output_path)
    else:
        status_label.config(text="Thư mục không tồn tại!")
# Tạo cửa sổ chính
window = tk.Tk()
window.title("YouTube Downloader")

# URL video
selectfile_label = ttk.Label(window, text="Select file:")
selectfile_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
selectfile_entry = ttk.Entry(window, width=50)
selectfile_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
browsefile_button = ttk.Button(window, text="Duyệt", command=select_file)
browsefile_button.grid(row=0, column=2, padx=5, pady=5)

# Định dạng file
format_label = ttk.Label(window, text="Định dạng:")
format_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
format_combobox = ttk.Combobox(window, values=["mp4", "webm", "mkv", "mp3 (chỉ âm thanh)"])
format_combobox.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

# Đường dẫn lưu
path_label = ttk.Label(window, text="Lưu vào:")
path_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
path_entry = ttk.Entry(window, width=40)
path_entry.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
browse_button = ttk.Button(window, text="Duyệt", command=browse_path)
browse_button.grid(row=2, column=2, padx=5, pady=5)

# Nút tải xuống
download_button = ttk.Button(window, text="Tải xuống", command=download_video)
download_button.grid(row=3, column=0, columnspan=3, padx=5, pady=10)
#Nút mở thư mục
download_button = ttk.Button(window, text="Mở thư mục tải xuống", command=open_output_folder)
download_button.grid(row=4, column=0, columnspan=3, padx=5, pady=10) 

# Hiển thị trạng thái
status_label = ttk.Label(window, text="")
status_label.grid(row=5, column=0, columnspan=3, padx=5, pady=5)

window.mainloop()
