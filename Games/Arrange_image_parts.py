from tkinter import StringVar, Label, Button, Frame, PhotoImage
import tkinter as tk
import random
from collections import OrderedDict
import math
import pygame

mainWindow = tk.Tk()
mainWindow.title("Arrage Image Game")
pygame.mixer.init()
pygame.mixer.music.load("Resources/tracks/bensound-memories.mp3")

photo_item = None

frame = Frame(mainWindow, relief = 'sunken', bd = 1)
frame.pack(fill = 'both', expand = True,
           padx = 10, pady = 10)

img_obj_list = []
for i in range(9):
    img_obj_list.append(PhotoImage(file='images_9/' + 'image_part_00' + str(i+1) + '.png'))

image_index_list = [x for x in range(9)]
label_obj_list = []
cordinate_of_all_images = [(0,0), (200,0), (400,0), (0,200), (200,200), (400,200), (0,400), (200,400), (400,400)]

def drag_start(event):
    wid = event.widget
    wid.startX = event.x
    wid.startY = event.y

def drag_motion(event):
    wid = event.widget
    x = wid.winfo_x() - wid.startX + event.x
    y = wid.winfo_y() - wid.startY + event.y
    wid.place(x=x,y=y)

arranged_image_count = 0
cordinates_needed_to_win = OrderedDict()

def check_if_game_user_won(cordinate_of_current_images):
    global arranged_image_count
    arranged_image_count = 0
    is_played_for = None
    if len(cordinates_needed_to_win) == 9:
        cordinates_needed_to_win_list = list(cordinates_needed_to_win.values())

        for i in range(9):
            x_value_desired = cordinates_needed_to_win_list[i][0]
            x_value_current = cordinate_of_current_images[i][0]
            y_value_deired = cordinates_needed_to_win_list[i][1]
            y_value_current = cordinate_of_current_images[i][1]
            x_set = math.isclose(x_value_desired, x_value_current, abs_tol = 15)
            y_set = math.isclose(y_value_deired, y_value_current, abs_tol = 15)

            if x_set and y_set:
                arranged_image_count += 1
                arranged_count_str.set("Arranged Images : " + str(arranged_image_count) + "/9")

        if arranged_image_count == 9:
            arranged_count_str.set(arranged_count_str.get() + "\n YOU WON!\n")
            pygame.mixer.music.stop()
            for i in range(9):
                label_obj_list[i][0].config(state="disabled")

def mouse_button_release(event):
    global label_obj_list, cordinate_of_all_images
    cordinate_of_current_images = []
    for i in range(9):
        x = label_obj_list[i][0].winfo_x()
        y = label_obj_list[i][0].winfo_y()
        cordinate_of_current_images.append((x,y))
    check_if_game_user_won(cordinate_of_current_images)

index_mine = 0
for r in range(3):
    for c in range(3):
        label_obj = Label(frame,
                          width=200, height=200)
        label_obj.grid(row=r, column=c)
        label_obj.bind('<Button-1>', drag_start)
        label_obj.bind('<B1-Motion>', drag_motion)
        mainWindow.bind("<ButtonRelease-1>", mouse_button_release)
        label_obj.config(image=img_obj_list[index_mine] ,state="disabled")
        label_obj_list.append((label_obj, cordinate_of_all_images[index_mine]))
        index_mine += 1

def play_handler():
    global image_index_list, label_obj_list
    pygame.mixer.music.play()
    for i in range(9):
        image_index = image_index_list.pop(random.randrange(len(image_index_list)))
        label_obj_list[i][0].config(image=img_obj_list[image_index])
        cordinates_needed_to_win[str(i)] = cordinate_of_all_images[image_index]

    image_index_list = [x for x in range(9)]
    arranged_count_str.set("Let`s arrange now\n")
    for i in range(9):
        label_obj_list[i][0].config(state="normal")

arranged_count_str = StringVar()
arranged_count_str.set("Arranged Images : 9/9")
arragned_label = Label(mainWindow,
                       textvariable=arranged_count_str,
                       font=("Microsoft Himalaya", 20))
arragned_label.place(x=625, y=20)

play_button = Button(mainWindow, text="Play",
                     command=play_handler,
                     padx=30, pady=2,
                     font=("Microsoft Himalaya", 20))
play_button.place(x=625, y=100)

mainWindow.geometry("820x700")
mainWindow.resizable(False, False)
mainWindow.mainloop()