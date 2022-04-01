from tkinter import StringVar, Button, Label, filedialog,  \
    ttk, PhotoImage
import tkinter as tk
import pygame
from tinytag import TinyTag
import arrow
from datetime import datetime

mainWindow = tk.Tk()
mainWindow.title("Music Player")

current_volume = 10
pb_value = 0.0
is_paused = False
actutal_track_duration = ""
audio_property = {}
track_meta_info_str = StringVar()
pause_resume_text = StringVar()
progress_played = StringVar()
volume_str = StringVar()

def get_time_in_str(time_val):
    enter = arrow.get("05:30:00", 'HH:mm:ss')

    time_in_str = datetime.fromtimestamp(time_val).strftime('%H:%M:%S')
    time_in_str = arrow.get(time_in_str, 'HH:mm:ss')
    time_in_str = time_in_str - enter

    time_in_str = str(time_in_str)
    hour_digit = int(time_in_str.split(":")[0])
    hour_str = ""
    if hour_digit < 10:
        hour_str = "0" + str(hour_digit)

    return hour_str + time_in_str[1:]

def get_audio_metadata(file):
    global audio_property
    audio = TinyTag.get(file)
    data = vars(audio)
    audio_property = {}
    for key, value in data.items():
        if not key.startswith('_') and key != 'extra' and value:
            audio_property[key] = value

    audio_property['duration_ms'] = audio_property['duration']
    track_duration = audio_property['duration']
    track_duration = int(track_duration)
    track_duration = get_time_in_str(track_duration)

    audio_property['duration'] = track_duration
    audio_property['file'] = file.split("/")[-1]
    return audio_property

def fd_hand():
    global pb_value, actutal_track_duration
    global audio_property

    media_file = filedialog.askopenfilename(title="Select a file",
                                    initialdir=".",
                                    filetypes=(("MP3 files", "*.mp3"),))
    if media_file:
        stop_hand()
        audio_property = {}
        pb_value = 0.0
        pb['value'] = pb_value
        meta_data  = get_audio_metadata(media_file)
        actutal_track_duration = meta_data['duration']
        pygame.mixer.init()
        pygame.mixer.music.load(media_file)

        played_duration_seconds = int(pygame.mixer.music.get_pos() / 1000)
        played_duration = get_time_in_str(played_duration_seconds)
        track_duration_in_seconds = int(audio_property['duration_ms'])

        progress_played.set("00:00:00" + "/" + actutal_track_duration)
        mainWindow.update_idletasks()

        vol_to_set = current_volume/100
        pygame.mixer.music.set_volume(vol_to_set)
        meta_str = ""
        for key,val in audio_property.items():
            if len(key) < 9:
                meta_str = meta_str + key.capitalize() + "\t\t: " + str(val) + "\n"
            else:
                meta_str = meta_str + key.capitalize() + "\t: " + str(val) + "\n"
        track_meta_info_str.set(meta_str)

infoLabel = Label(mainWindow)
infoLabel.config(bg="black", fg="white", width=70, height=20, textvariable=track_meta_info_str,
                 justify='left', padx=10, pady=10,
                 anchor="nw",
                 font=("Microsoft Himalaya","20"))
infoLabel.place(x=0,y=0)

openPhoto = PhotoImage(file="open.png")
openButton = Button(mainWindow, text="Open", command=fd_hand, image=openPhoto,compound="top")
openButton.config(width=50, height=65)
openButton.place(x=2, y=330)

def update_time_display():
    global pb_value, actutal_track_duration

    if pygame.mixer.get_init():
        played_duration_seconds = int(pygame.mixer.music.get_pos()/1000)
        played_duration = get_time_in_str(played_duration_seconds)

        track_duration_in_seconds = int(audio_property['duration_ms'])

        pb_value = int((100*played_duration_seconds)/track_duration_in_seconds)
        if pb_value != pb['value']:
            pb['value'] = pb_value
            progress_played.set(played_duration + "/" +  actutal_track_duration)
            mainWindow.update_idletasks()
        mainWindow.after(1000,update_time_display)

def play_hand():
    global is_paused
    if pygame.mixer.get_init():
        if is_paused == True:
            pygame.mixer.music.unpause()
            pause_resume_text.set("Pause")
            is_paused = False
        elif not pygame.mixer.music.get_busy():
            pygame.mixer.music.play()
        update_time_display()

playPhoto = PhotoImage(file="play.png")
playButton = Button(mainWindow, text="Play", command=play_hand, image=playPhoto, compound="top")
playButton.config(width=50, height=65)
playButton.place(x=62, y=330)

def pause_resume_hand():
    global is_paused
    if pygame.mixer.get_init():
        if is_paused == False and pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
            pause_resume_text.set("Resume")
            is_paused = True
        elif is_paused == True:
            pygame.mixer.music.unpause()
            pause_resume_text.set("Pause")
            is_paused = False

pause_resume_Photo = PhotoImage(file="pause.png")
pause_resume_text.set("Pause")
pauseResumeButton = Button(mainWindow, textvariable=pause_resume_text, command=pause_resume_hand,
                           image=pause_resume_Photo, compound="top")
pauseResumeButton.config(width=50, height=65)
pauseResumeButton.place(x=122, y=330)

def stop_hand():
    global is_paused
    if pygame.mixer.get_init():
        progress_played.set("00:00:00/" + "00:00:00")
        global pb_value
        pygame.mixer.music.stop()
        pb_value = 0
        pb['value'] = pb_value
        if is_paused == True:
            pause_resume_text.set("Pause")
            is_paused = False

stop_photo = PhotoImage(file="stop.png")
stopButton = Button(mainWindow, text="Stop", command=stop_hand,image=stop_photo, compound="top")
stopButton.config(width=50, height=65)
stopButton.place(x=182, y=330)

def vol_plus_hand():
    global current_volume
    if pygame.mixer.get_init():
        if current_volume < 100:
            current_volume += 10
        vol_to_set = current_volume/100
        pygame.mixer.music.set_volume(vol_to_set)
        volume_str.set(str(current_volume))

volPusPhoto = PhotoImage(file="volume_plus.png")
volPlus = Button(mainWindow, text="Vol +", command=vol_plus_hand, image=volPusPhoto,compound="top")
volPlus.config(width=50, height=65)
volPlus.place(x=242, y=330)

def vol_minus_hand():
    global current_volume
    if pygame.mixer.get_init():
        if current_volume > 0:
            current_volume -= 10
        vol_to_set = current_volume / 100
        pygame.mixer.music.set_volume(vol_to_set)
        volume_str.set(str(current_volume))

volminusPhoto = PhotoImage(file="volume_minus.png")
volMinus = Button(mainWindow, text="Vol -", command=vol_minus_hand, image=volminusPhoto,compound="top")
volMinus.config(width=50, height=65)
volMinus.place(x=302, y=330)

volume_label = Label(mainWindow, textvariable=volume_str)
volume_label.place(x=362,y=332)
volume_str.set(str(current_volume))
volume_label.config(bg="black",fg="white", width="5",
                    justify='center', font=("Impact","40"))

s = ttk.Style()
s.theme_use('clam')
s.configure("white.Horizontal.TProgressbar", foreground='white', background='black')
pb = ttk.Progressbar(mainWindow, orient="horizontal",style="white.Horizontal.TProgressbar",)
pb.config(length=400)
pb.place(x=0, y=308)

duration_label = Label(mainWindow, textvariable=progress_played)
duration_label.config(fg="black", bd=0.5, relief="sunken")
duration_label.place(x=402,y=308)
progress_played.set("00:00:00/00:00:00")

mainWindow.geometry("500x406")
mainWindow.resizable(False, False)
mainWindow.mainloop()