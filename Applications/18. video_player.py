import time

import vlc
import arrow
from datetime import datetime

from tkinter import StringVar, Button, Label, filedialog,  \
    ttk, PhotoImage, Scale
import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Video Player")

current_volume = 10
pb_value = 0.0

pause_resume_text = StringVar()
progress_played = StringVar()
volume_str = StringVar()
media_player = None

infoLabel = Label(mainWindow)
infoLabel.config(width=71, height=20)
infoLabel.place(x=0,y=0)

def fd_hand():
    global pb_value
    global media_player
    media_file = filedialog.askopenfilename(title="Select a file",
                                    initialdir="D:/rohit/my_pro/",
                                    filetypes=(("MP4 files", "*.mp4"),
                                               ("MP3 files", "*.mp3")))
    if media_file:
        selected_media_file = media_file.split("/")[-1]
        current_playing_media.set("Media file : " + selected_media_file)
        stop_hand()
        scroller.set(0)

        pb_value = 0
        pb['value'] = pb_value
        media_player = vlc.MediaPlayer(media_file)
        media_player.set_hwnd(infoLabel.winfo_id())
        progress_played.set("00:00:00/00:00:00")
        media_player.audio_set_volume(current_volume * 2)
        mainWindow.update_idletasks()

openPhoto = PhotoImage(file="open.png")
openButton = Button(mainWindow, text="Open", command=fd_hand, image=openPhoto,compound="top")
openButton.config(width=50, height=65)
openButton.place(x=2, y=370)

def update_time_display():
    global pb_value
    global media_player
    if media_player:
        played_duration = get_time_in_str(media_player.get_time())
        full_length = get_time_in_str(media_player.get_length())

        progress_played.set(str(played_duration) + "/" + str(full_length))
        pb_value = media_player.get_position()
        pb_value = int(pb_value * 100)
        pb['value'] = pb_value
        mainWindow.update_idletasks()
        mainWindow.after(1000,update_time_display)

def get_time_in_str(time_val):
    global media_player
    if media_player:
        enter = arrow.get("05:30:00", 'HH:mm:ss')
        try:
            time_in_str = datetime.fromtimestamp(time_val / 1000).strftime('%H:%M:%S')
            time_in_str = arrow.get(time_in_str, 'HH:mm:ss')
            time_in_str = time_in_str - enter

            time_in_str = str(time_in_str)
            hour_digit = int(time_in_str.split(":")[0])
            hour_str = ""
            if hour_digit < 10:
                hour_str = "0" + str(hour_digit)
        except Exception as e:
            return "00:00:00"

        return hour_str + time_in_str[1:]

def play_hand():
    if media_player:
        media_player.play()
        if pause_resume_text.get():
            pause_resume_text.set("Pause")
        update_time_display()

playPhoto = PhotoImage(file="play.png")
playButton = Button(mainWindow, text="Play", command=play_hand, image=playPhoto, compound="top")
playButton.config(width=50, height=65)
playButton.place(x=62, y=370)

def pause_resume_hand():
    if media_player:
        media_player.pause()
        if pause_resume_text.get() == "Pause":
            pause_resume_text.set("Resume")
        else:
            pause_resume_text.set("Pause")

pause_resume_Photo = PhotoImage(file="pause.png")
pause_resume_text.set("Pause")
pauseResumeButton = Button(mainWindow, textvariable=pause_resume_text, command=pause_resume_hand,
                           image=pause_resume_Photo, compound="top")
pauseResumeButton.config(width=50, height=65)
pauseResumeButton.place(x=122, y=370)

def stop_hand():
    global media_player
    if media_player:
        media_player.stop()
    progress_played.set("00:00:00/00:00:00")
    pb_value = 0
    pb['value'] = pb_value

stop_photo = PhotoImage(file="stop.png")
stopButton = Button(mainWindow, text="Stop", command=stop_hand,image=stop_photo, compound="top")
stopButton.config(width=50, height=65)
stopButton.place(x=182, y=370)

def vol_minus_hand():
    global current_volume
    if media_player:
        if current_volume > 0:
            current_volume -= 10
        media_player.audio_set_volume(current_volume * 2)
        volume_str.set(str(current_volume))

volminusPhoto = PhotoImage(file="volume_minus.png")
volMinus = Button(mainWindow, text="Vol -", command=vol_minus_hand, image=volminusPhoto,compound="top")
volMinus.config(width=50, height=65)
volMinus.place(x=242, y=370)

def vol_plus_hand():
    global current_volume
    if media_player:
        if current_volume < 100:
            current_volume += 10
        media_player.audio_set_volume(current_volume * 2)
        volume_str.set(str(current_volume))

volPusPhoto = PhotoImage(file="volume_plus.png")
volPlus = Button(mainWindow, text="Vol +", command=vol_plus_hand, image=volPusPhoto,compound="top")
volPlus.config(width=50, height=65)
volPlus.place(x=302, y=370)

volume_label = Label(mainWindow, textvariable=volume_str)
volume_label.place(x=362,y=372)
volume_str.set(str(current_volume))
volume_label.config(bg="black",fg="white", width="5",
                    justify='center', font=("Impact","40"))

s = ttk.Style()
s.theme_use('clam')
s.configure("white.Horizontal.TProgressbar", foreground='white', background='black')
pb = ttk.Progressbar(mainWindow, orient="horizontal",style="white.Horizontal.TProgressbar",)
pb.config(length=400)
pb.place(x=0, y=308)

def scale_hand(value):
    value = int(value)/100
    if media_player:
        media_player.set_position(value)

scroller = Scale(mainWindow, from_=0, to=100, command=scale_hand)
scroller.config(length="492", orient="horizontal",
         troughcolor="black", bg="white", fg="white")
scroller.set(0)
scroller.place(x=2,y=328)

duration_label = Label(mainWindow, textvariable=progress_played)
duration_label.config(fg="black", bd=0.5, relief="sunken")
duration_label.place(x=402,y=308)

current_playing_media = StringVar()
currnet_playing_media_label = Label(mainWindow, textvariable=current_playing_media)
currnet_playing_media_label.config(bd=1, relief="groove",
                                   width=69)
currnet_playing_media_label.place(x=6,y=330)

progress_played.set("00:00:00/00:00:00")

mainWindow.geometry("500x446")
mainWindow.resizable(False, False)
mainWindow.mainloop()