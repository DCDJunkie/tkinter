#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
from tkinter import StringVar, Label, Button, PhotoImage
import pygame
from threading import Timer

mainWindow = tk.Tk()
mainWindow.title("Digital Clock with Alarm")
date_time_str = StringVar()

def update_date_time():
    day = datetime.today().strftime('%A')
    month = datetime.today().strftime('%B')
    year = datetime.today().strftime('%G')
    time = datetime.today().strftime('%X')
    date = datetime.today().strftime('%d')
    date_time_full_str = month + " " + date + " " + year + "\n" \
                         + day + " " + time

    date_time_str.set(date_time_full_str)
    date_time_label.config(font=("Agency FB", "40"))
    date_time_label.after(1000,update_date_time)

pygame.mixer.init()
media_file = "Resources/tracks/alarm.mp3"
pygame.mixer.music.load(media_file)

date_time_label = Label(mainWindow, textvariable=date_time_str,
                        width="60",
                        height="3",
                        bg="black",
                        fg = "white",
                        font=("Gabriola",40))
date_time_label.pack(anchor="center")
update_date_time()

hour_label = Label(mainWindow, text="Hour:")
hour_label.place(x=10, y=220)

selected_hour = StringVar()
hour_cb = ttk.Combobox(mainWindow, textvariable=selected_hour)
hour_cb['state'] = 'readonly'
hour_cb['values'] = [m for m in range(0, 13)]
hour_cb.place(x=50, y=220)

minute_label = Label(mainWindow, text="Minute:")
minute_label.place(x=200, y=220)

selected_min = StringVar()
min_cb = ttk.Combobox(mainWindow, textvariable=selected_min)
min_cb['state'] = 'readonly'
min_cb['values'] = [m for m in range(0, 60)]
min_cb.place(x=250, y=220)

second_label = Label(mainWindow, text="Second:")
second_label.place(x=400, y=220)

selected_sec = StringVar()
sec_cb = ttk.Combobox(mainWindow, textvariable=selected_sec)
sec_cb['state'] = 'readonly'
sec_cb['values'] = [m for m in range(0, 60)]
sec_cb.place(x=450, y=220)

current_time = datetime.now()
hh = current_time.strftime("%H")
mm = current_time.strftime("%M")
ss = current_time.strftime("%S")
hour_cb.set(int(hh))
min_cb.set(int(mm))
sec_cb.set(int(ss))

def convert(date_time):
    format = '%Y-%m-%d %H:%M:%S'
    datetime_str = datetime.strptime(date_time, format)
    return datetime_str

currently_playing_alarm = None
alarm_image = None
frameCount = 352
frames = [PhotoImage(file='Resources/images/Alarm_clock_GIF_image.gif',format = 'gif -index %i' %(i)) for i in range(0, frameCount, 3)]
frame_index = 0

def run_animation():
    if pygame.mixer.get_init() and pygame.mixer.music.get_busy():
        global alarm_image, frames, frame_index
        if frame_index >= (frameCount/3):
            frame_index = 0
        current_frame = frames[frame_index]
        alarm_label.config(image=current_frame)
        frame_index += 1
        mainWindow.after(25, run_animation)


def start_alarm():
    global currently_playing_alarm, alarm_image
    if pygame.mixer.get_init() and not pygame.mixer.music.get_busy():
        pygame.mixer.music.play()
        stop_button.config(state="normal")
        currently_playing_alarm = datetime.now()
        run_animation()
        # alarm_image = PhotoImage(file="Alarm_Clock_GIF_Image.gif")
        # alarm_label.config(image=alarm_image)

def stop_alarm():
    global currently_playing_alarm
    if currently_playing_alarm:
        for item in alarm_table.get_children():
            value = alarm_table.item(item)['values'][1]
            value = convert(value)
            time_diff = abs(value - currently_playing_alarm)
            time_diff = int(time_diff.total_seconds())
            if time_diff <= 2:
                alarm_table.delete(item)

        if pygame.mixer.get_init() and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
            stop_button.config(state="disabled")

        alarm_label.config(image="")

        alarm_time_list = [alarm_table.item(item)['values'][1] for item in alarm_table.get_children()]

        for item in alarm_table.get_children():
            alarm_table.delete(item)

        for index in range(len(alarm_time_list)):
            data = [index+1, alarm_time_list[index]]
            alarm_table.insert('', tk.END, values=data)

def set_alarm_handler():
    day = datetime.today().strftime('%d')
    month = datetime.today().strftime('%m')
    year = datetime.today().strftime('%Y')
    hh = selected_hour.get()
    mm = selected_min.get()
    ss = selected_sec.get()
    current_time = datetime.now()

    time_str = year + "-" + month + "-" + day + " " + hh + ":" + mm + ":" + ss
    alarm_set_time = convert(time_str)

    if alarm_set_time < current_time:
        alarm_set_time = alarm_set_time + timedelta(hours=24)

    alarm_to_be_start_after = alarm_set_time - current_time
    alarm_to_be_start_after = alarm_to_be_start_after.total_seconds()

    for item in alarm_table.get_children():
        value =  alarm_table.item(item)['values'][1]
        if convert(value)  == alarm_set_time:
            return

    data = [len(alarm_table.get_children())+1, alarm_set_time]
    alarm_table.insert('', tk.END, values=data)
    for column in alarm_table['column']:
        alarm_table.column(column, anchor="center")

    t = Timer(alarm_to_be_start_after, start_alarm)
    t.start()

set_button = Button(mainWindow, text="Set", width=8, pady=3, command=set_alarm_handler)
set_button.place(x=600, y=215)

stop_button = Button(mainWindow, text="Stop", pady=3, width=8, command=stop_alarm)
stop_button.place(x=680, y=215)
stop_button.config(state="disabled")

columns = ('AlarmNumber', 'AlarmTime')
alarm_table = ttk.Treeview(mainWindow, columns=columns, show='headings')

alarm_table.heading('AlarmNumber', text='Alarm Number')
alarm_table.heading('AlarmTime', text='Alarm Time')
alarm_table.config(height=15)
alarm_table.place(x=10, y=260)

alarm_label = Label(mainWindow)
alarm_label.place(x=450, y=260, width=400, height=317)


mainWindow.geometry("850x610")
mainWindow.resizable(False, False)
mainWindow.mainloop()