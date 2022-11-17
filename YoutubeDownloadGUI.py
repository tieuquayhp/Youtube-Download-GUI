from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
from pytube import Channel
from pytube import Playlist

import shutil, os, threading


#Functions
#Create folder
def createfolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print('Error: Creating directory. '+directory)

#Download by single link
def download_link_c():
    canvas.delete("all")
    screen.title('Download by link')

    def select_path():
        #allow user to select a path from the exporler
        path = filedialog.askdirectory()
        path_label.config(text=path)

    def download_file():
        #get user path
        get_link = link_field.get()
        #get selected path
        user_path = path_label.cget("text")
        progress_label.config(text="Downloading...Please wait...")
        #Download video
        mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
        vid_clip = VideoFileClip(mp4_video)
        vid_clip.close()
        #move to selected directory
        shutil.move(mp4_video, user_path)
        progress_label.config(text="Download complete!")
        progress_bar.stop()
    
    def animation():
        #start progress bar
        progress_bar.start()

    def play():
        #run download & start progress bar loading
        t1 = threading.Thread(target=animation)
        t2 = threading.Thread(target=download_file)
        t1.start()
        t2.start()
    #link field
    link_field = Entry(screen, width=50)
    link_label = Label(screen, text="( 1) Enter Download Link: ", font=('Arial',15))
    

    #Select Path for saving file
    path_label = Label(screen, text="( 2) Select Path For Download", font=('Arial',15))
    select_btn = Button(screen, text="(2) Select", command=select_path)

    #Back btn
    back_btn =Button(screen, text="Back to home page", command=start)

    #Download btns
    download_btn = Button(screen, text="(3) Download File", command=play)

    #Progress Bar
    progress_label = Label(screen, text="...")
    progress_bar = ttk.Progressbar(screen, orient=HORIZONTAL, length=400, mode='indeterminate')
    #create image
    canvas.create_image(250, 80, image = logo_img)
    #Add to window
    canvas.create_window(250, 280, window=path_label)
    canvas.create_window(250, 330, window=select_btn)

    #add widgets to windows
    canvas.create_window(250, 170, window=link_label)
    canvas.create_window(250, 220, window=link_field)

    #add back btn to canvas
    canvas.create_window(250, 450, window=back_btn)
    
    #add download btn to canvas
    canvas.create_window(250, 370, window=download_btn)

    #add Progress Bar
    canvas.create_window(250, 400, window=progress_label)
    canvas.create_window(250, 420, window=progress_bar)

#Download by playlist link
def downloadplaypist_c():
    canvas.delete("all")
    screen.title('Download by playlist')       

    def select_path():
        #allow user to select a path from the exporler
        path = filedialog.askdirectory()
        path_label.config(text=path) 
    def animation():
        progress_bar.start()

    def play():
        t1 = threading.Thread(target=animation)
        t2 = threading.Thread(target=download_file)
        t1.start()
        t2.start()
         
    
    def download_file():
        progress_label.config(text="Downloading...Please wait...")
        #get user path
        get_link = link_field.get()
        get_channel_link = linkchannel_feild.get() 
        user_path = path_label.cget("text")
        # Tạo thư mục có tên kênh   
        try:
            channel = Channel(get_channel_link)
        except:
            messagebox.showwarning("Errors","Connection Errors")

        createfolder(os.path.join(user_path,channel.channel_name))    
        #Download video
        try:
            playlist = Playlist(get_link)
        except:
            messagebox.showwarning("Errors","Connection Errors 1")  

        for video in playlist.videos:
            try:
                mp4_video = video.streams.get_highest_resolution().download()
                vid_clip = VideoFileClip(mp4_video)
                vid_clip.close()
                #move to selected directory
                try:
                    shutil.move(mp4_video, os.path.join(user_path,channel.channel_name))
                except:
                    messagebox.showwarning("Errors","Move errors")
                screen.title('Download Complete '+ video.title)     
            except:
                messagebox.showwarning("Errors","Download Errors 2")   
        
        progress_label.config(text="Download complete!")
        progress_bar.stop()
    #link field
    link_field = Entry(screen, width=50)
    link_label = Label(screen, text="Enter Playlist Download Link: ", font=('Arial',15))  

    #link Channel field
    linkchannel_feild = Entry(screen, width=50)
    linkchannel_label = Label(screen, text="(1) Enter Channel Link: ", font=('Arial',15))

    #Select Path for saving file
    path_label = Label(screen, text="(2) Select Path For Download", font=('Arial',15))
    select_btn = Button(screen, text="(2) Select", command=select_path)

    #Back btn
    back_btn =Button(screen, text="Back to home page", command=start)

    #Download btns
    download_btn = Button(screen, text="(3) Download File", command=play)

    #Progress Bar
    progress_label = Label(screen, text="...")
    progress_bar = ttk.Progressbar(screen, orient=HORIZONTAL, length=400, mode='indeterminate')

    #create image
    canvas.create_image(250, 80, image = logo_img)
    #Add to window
    canvas.create_window(250, 300, window=path_label)
    canvas.create_window(250, 330, window=select_btn)

    #add widgets to windows
    canvas.create_window(250, 170, window=link_label)
    canvas.create_window(250, 200, window=link_field)

    #add widgets to windows
    canvas.create_window(250, 260, window=linkchannel_feild)
    canvas.create_window(250, 230, window=linkchannel_label)

    #add back btn to canvas
    canvas.create_window(250, 450, window=back_btn)
    
    #add download btn to canvas
    canvas.create_window(250, 370, window=download_btn)

    #add Progress Bar
    canvas.create_window(250, 400, window=progress_label)
    canvas.create_window(250, 420, window=progress_bar)

#Download by file input.txt
def downloadfile_c(): 
    canvas.delete("all")
    screen.title('Download by playlist')       

    def select_path():
        #allow user to select a path from the exporler
        path = filedialog.askdirectory()
        path_label.config(text=path) 
    def select_file():
        #allow user to select a path from the exporler
        path = filedialog.askopenfilename()
        selectfile_label.config(text=path) 
    def animation():
        progress_bar.start()

    def play():
        t1 = threading.Thread(target=animation)
        t2 = threading.Thread(target=download_file)
        t1.start()
        t2.start()     
    
    def download_file():
        progress_label.config(text="Downloading...Please wait...")
        file_input = selectfile_label.cget("text")
        #get user path
        get_channel_link = linkchannel_feild.get() 
        user_path = path_label.cget("text")
        video_link = open(file_input, 'r')
        # Tạo thư mục có tên kênh   
        try:
            channel = Channel(get_channel_link)
        except:
            messagebox.showwarning("Errors","Connection Errors")

        createfolder(os.path.join(user_path,channel.channel_name))    
        #Download video
        for video in video_link:
            try:
                yt = YouTube(video)
            except:
                messagebox.showwarning("Errors","Connection Errors 1")  
            try:
                mp4_video = yt.streams.get_highest_resolution().download()
                vid_clip = VideoFileClip(mp4_video)
                vid_clip.close()
                #move to selected directory
                try:
                    shutil.move(mp4_video, os.path.join(user_path,channel.channel_name))
                except:
                    messagebox.showwarning("Errors","Move errors")
            except:
                messagebox.showwarning("Errors","Download Errors 2")   
            
        progress_label.config(text="Download complete!")
        progress_bar.stop()
    #link field
    selectfile_btn = Button(screen, text="(1) Select File", command=select_file)
    selectfile_label = Label(screen, text="(1) Select File Input: ", font=('Arial',15))  

    #link Channel field
    linkchannel_feild = Entry(screen, width=50)
    linkchannel_label = Label(screen, text="(2) Enter Channel Link: ", font=('Arial',15))

    #Select Path for saving file
    path_label = Label(screen, text="(3) Select Path For Download", font=('Arial',15))
    select_btn = Button(screen, text="(3) Select", command=select_path)

    #Back btn
    back_btn =Button(screen, text="Back to home page", command=start)

    #Download btns
    download_btn = Button(screen, text="(4) Download File", command=play)

    #Progress Bar
    progress_label = Label(screen, text="...")
    progress_bar = ttk.Progressbar(screen, orient=HORIZONTAL, length=400, mode='indeterminate')

    #create image
    canvas.create_image(250, 80, image = logo_img)
    #Add to window
    canvas.create_window(250, 300, window=path_label)
    canvas.create_window(250, 330, window=select_btn)

    #add widgets to windows
    canvas.create_window(250, 170, window=selectfile_label)
    canvas.create_window(250, 200, window=selectfile_btn)

    #add widgets to windows
    canvas.create_window(250, 260, window=linkchannel_feild)
    canvas.create_window(250, 230, window=linkchannel_label)

    #add back btn to canvas
    canvas.create_window(250, 450, window=back_btn)
    
    #add download btn to canvas
    canvas.create_window(250, 370, window=download_btn)

    #add Progress Bar
    canvas.create_window(250, 400, window=progress_label)
    canvas.create_window(250, 420, window=progress_bar)

#Download by channel link( Still notworking cause of pytube)
def downloadchannel_c():
    canvas.delete("all")
    screen.title('Download by Channel')
    def select_path():
        #allow user to select a path from the exporler
        path = filedialog.askdirectory()
        path_label.config(text=path)
       
    
    def download_file():
        screen.title('Downloading...')
        #get user path
        get_link = link_field.get()
        user_path = path_label.cget("text")
        # Tạo thư mục có tên kênh   
        print(get_link)
        try:
            channel = Channel(get_link)
        except:
            messagebox.showwarning("Errors","Connection Errors ChanneL")

        createfolder(os.path.join(user_path,channel.channel_name))    
        #Download video 

        for video in channel.videos[:3]:
            print(video)
            try:
                mp4_video = video.streams.get_highest_resolution().download()
                vid_clip = VideoFileClip(mp4_video)
                vid_clip.close()
                #move to selected directory
                try:
                    shutil.move(mp4_video, os.path.join(user_path,channel.channel_name))
                except:
                    messagebox.showwarning("Errors","Move errors")
                screen.title('Download Complete '+ video.title)     
            except:
                messagebox.showwarning("Errors","Download Errors 2")   
    messagebox.showinfo("Done", "Download Complete")
    screen.title('Download Complete! Download Another File...')
    #link field
    link_field = Entry(screen, width=50)
    link_label = Label(screen, text="Enter Channel Download Link: ", font=('Arial',15))  

    #Select Path for saving file
    path_label = Label(screen, text="Select Path For Download", font=('Arial',15))
    select_btn = Button(screen, text="Select", command=select_path)

    #Back btn
    back_btn =Button(screen, text="Back to home page", command=start)

    #Download btns
    download_btn = Button(screen, text="Download File", command=download_file)

    #create image
    canvas.create_image(250, 80, image = logo_img)
    #Add to window
    canvas.create_window(250, 280, window=path_label)
    canvas.create_window(250, 330, window=select_btn)

    #add widgets to windows
    canvas.create_window(250, 170, window=link_label)
    canvas.create_window(250, 220, window=link_field)

    #add back btn to canvas
    canvas.create_window(250, 450, window=back_btn)
    
    #add download btn to canvas
    canvas.create_window(250, 390, window=download_btn)

#Run Radian btn choise
def clicked(value):
    match value:
        case 1:
            download_link_c()
        case 2:
            downloadplaypist_c()
        case 3:
            downloadfile_c()
        case 4:
            downloadchannel_c()

#Create main GUI
def start():
    
    r = IntVar()
    r.set("1")
    canvas.delete("all")
    # Radio btn choise
    downloadlink_choise = Radiobutton(screen, text="Download by link", variable=r, value=1)
    downloadplaylist_choise = Radiobutton(screen, text="Download by playlist link", variable=r, value=2)
    downloadfile_choise = Radiobutton(screen, text="Download by file", variable=r, value=3)
    downloadchannnel_choise = Radiobutton(screen, text="Download by channel( Still Fail)", variable=r, value=4, fg="red", state=DISABLED)
    #button choise
    choise_btn = Button(screen, text="Select this choise", command=lambda: clicked(r.get()))    
    #create radio btn
    canvas.create_window(150, 200, window=downloadlink_choise)
    canvas.create_window(350, 200, window=downloadplaylist_choise)
    canvas.create_window(150, 250, window=downloadfile_choise)
    canvas.create_window(350, 250, window=downloadchannnel_choise)
    #create button choise
    canvas.create_window(250, 300, window=choise_btn)
    #create image
    canvas.create_image(250, 80, image = logo_img)
screen = Tk()
tittle = screen.title("Youtube Download made by quangpt")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()
#Create icon
screen.iconbitmap('./yt.ico')
#image logo
logo_img = PhotoImage(file='./yt.png')
#resize image
logo_img = logo_img.subsample(10,10)
#create image
canvas.create_image(250, 80, image = logo_img)
start()
screen.mainloop()