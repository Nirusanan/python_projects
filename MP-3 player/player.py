import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer 
import os
from PIL import Image, ImageTk, ImageSequence

root = Tk()
root.title("MP3 Music Player")
root.geometry("520x700+290+10")
root.configure(background="#333333")
root.resizable(False, False)

mixer.init()

frameCount = 30
frames = []

gif = Image.open("player2.gif")

# Resize the frames
for frame in ImageSequence.Iterator(gif):
    frame = frame.resize((520, 400))  
    frame = ImageTk.PhotoImage(frame)
    frames.append(frame)

def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == frameCount:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)

label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)


def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)

        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)


def PlayMusic():
    music_name = Playlist.get(ACTIVE)
    print(music_name)
    mixer.music.load(music_name)
    mixer.music.play()

def SetVolume(val):
    volume = int(val) / 100  
    mixer.music.set_volume(volume)


image_icon = PhotoImage(file="logo.png")
root.iconphoto(False, image_icon)

Menu = PhotoImage(file = "menu.png")
Label(root, image = Menu).place(x=0, y=580, height=100, width=520)

frame_music = Frame(root, bd = 2, relief=RIDGE)
frame_music.place(x=0, y=585, height=100, width=520)

lower_frame = Frame(root, bg = "#FFFFFF", width=520, height=180)
lower_frame.place(x=0, y=400)

# Play Button
try:
    play_image = Image.open("play.png")  
    play_image = play_image.resize((50, 50)) 
    Buttonplay = ImageTk.PhotoImage(play_image)
    play_button = Button(root, image=Buttonplay, bg="#FFFFFF", bd=0, height=60, width=60, command=PlayMusic)
    play_button.place(x=215, y=487)
except Exception as e:
    print("Error loading play button image:", e)
    play_button = Button(root, text="Play Music", width=10, height=2, font=("Times New Roman", 12, "bold"), fg="Black", bg="#FFFFFF", command=PlayMusic)
    play_button.place(x=215, y=487)

# pause Button
pause_image = Image.open("pause.png")  
pause_image = pause_image.resize((50, 50)) 
ButtonPause = ImageTk.PhotoImage(pause_image)
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height=60, width=60, command = mixer.music.pause).place(x=300, y=487)

# Stop Button
stop_image = Image.open("stop.png")  
stop_image = stop_image.resize((50, 50)) 
ButtonStop = ImageTk.PhotoImage(stop_image)
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height=60, width=60, command = mixer.music.stop).place(x=400, y=487)

# Volume 
volume1_image = Image.open("volume.png")  
volume1_image = volume1_image.resize((40, 40)) 
Volume1 = ImageTk.PhotoImage(volume1_image)
pane1= Label(root, image= Volume1).place(x=20, y=495)

# Volume control
volume_scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, bg="#333333", fg="white", highlightbackground="#333333", troughcolor="grey", command=SetVolume)
volume_scale.set(50)  # Set default volume to 50%
volume_scale.place(x=70, y=495)

Button(root, text= "Browse Music", width= 59, height=1, font= ("Times New Roman", 12, "bold"), fg = "Black", bg="#FFFFFF", command=AddMusic).place(x=0, y=550)

Scroll = Scrollbar(frame_music)
Playlist = Listbox(frame_music, width=100, font = ("Times New Roman", 10), bg="#333333", fg = "grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand= Scroll.set)
Scroll.config(command= Playlist.yview)
Scroll.pack(side= RIGHT, fill = Y)
Playlist.pack(side= RIGHT, fill = BOTH)


root.mainloop() 