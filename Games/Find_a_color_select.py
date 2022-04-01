import time
from tkinter import StringVar, Label, Button, Canvas
import tkinter as tk
import random
import pygame

mainWindow = tk.Tk()
mainWindow.title("Choose a Color Game")
score_count = 0
score_str = StringVar()
scrole_label = Label(mainWindow,
                     textvariable=score_str,
                     font=(None,22),
                     relief="raised")
scrole_label.place(x=250, y=10, width=240, height=50)
score_str.set("SCORE: " + str(score_count))

color_color_on_obj = None
can = Canvas(mainWindow, height=400, width=475, relief="raised", bd=2)
can.place(x=10, y=60)

cir_eval = None
color_list = ["red", "green", "blue","white", "orange", "yellow", "pink", "magenta", "black", "cyan"]
total_count = 0
is_game_stated = False
def create_oval_at_random_position():
    global is_game_stated
    if is_game_stated == False:
        for item in ["Starting in 3", "Starting in 2", "Starting in 1", "GO"]:
            score_str.set(item)
            mainWindow.update_idletasks()
            time.sleep(1)
        is_game_stated = True
        if pygame.mixer.get_init():
            pygame.mixer.music.play()

    global color_color_on_obj, score_count, total_count
    total_count += 1
    x_position = random.randrange(425)
    y_position = random.randrange(350)
    color = color_list[random.randrange(len(color_list))]
    color_color_on_obj = color
    score_str.set("SCORE: " + str(score_count) +"/" + str(total_count))
    global cir_eval
    if cir_eval:
        can.delete(cir_eval)
    cir_eval = can.create_oval(x_position, y_position, x_position+50, y_position+50, fill=color)
    if total_count >= 75:
        if pygame.mixer.get_init() and pygame.mixer.music.get_busy():
            pygame.mixer.music.stop()
        return
    if score_count <= 5:
        mainWindow.after(2000, create_oval_at_random_position)
    elif score_count <= 10:
        mainWindow.after(1000, create_oval_at_random_position)
    elif score_count <= 20:
        mainWindow.after(750, create_oval_at_random_position)
    else:
        mainWindow.after(500, create_oval_at_random_position)


def mouse_button_release(event):
    global color_color_on_obj, score_count, cir_eval
    wid = event.widget
    color = wid.cget("bg")
    if color_color_on_obj == color and cir_eval:
        score_count += 1
        can.delete(cir_eval)
        cir_eval = None
        score_str.set("SCORE: " + str(score_count) +"/" + str(total_count))



y_value = 480
x_value = 120
color_index = 0

for row in range(2):
    x_value = 120
    for column in range(5):
        btn = Button(mainWindow, bg=color_list[color_index])
        btn.place(x=x_value, y=y_value, height=40,width=40)
        x_value += 55
        color_index += 1
    y_value += 55

def start_game():
    global total_count
    global is_game_stated
    total_count = 0
    is_game_stated = False
    global cir_eval
    if cir_eval:
        can.delete(cir_eval)
    score_str.set("SCORE: 00")
    create_oval_at_random_position()

start_button = Button(mainWindow, text="Start", command=start_game,
                      font=(None, 20))
start_button.place(x=10, y=10, width=240, height=50)


pygame.mixer.init()
pygame.mixer.music.load("Resources/tracks/bensound-memories.mp3")

mainWindow.bind("<ButtonRelease-1>", mouse_button_release)
mainWindow.geometry("500x600")
mainWindow.resizable(False, False)
mainWindow.mainloop()