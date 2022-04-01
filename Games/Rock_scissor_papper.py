#!/usr/bin/env python
import random
import time
import tkinter as tk
from tkinter import Button, Label, StringVar, PhotoImage
import pygame
mainWindow = tk.Tk()
mainWindow.title("Rock Paper Scissor")

user_won_count = 0
computer_won_count = 0

def get_winner(your_choice, computer_choice):
    is_user_won = False
    if your_choice == computer_choice:
        is_user_won = "Tie"
    elif your_choice == "rock" and computer_choice == "scissor":
            is_user_won = True
    elif your_choice == "paper" and computer_choice == "rock":
            is_user_won = True
    elif your_choice == "scissor" and computer_choice == "paper":
            is_user_won = True
    return is_user_won

rock_big_image =  PhotoImage(file="Resources/images/rock_big.png")
paper_big_image = PhotoImage(file="Resources/images/paper_big.png")
scissor_big_image =  PhotoImage(file="Resources/images/scissor_big.png")

rock_small_image = PhotoImage(file='Resources/images/rock_small.png')
paper_small_image = PhotoImage(file='Resources/images/paper_small.png')
scissor_small_image = PhotoImage(file='Resources/images/scissor_small.png')

options = [
            {'rock'     : rock_big_image},
            {'scissor'  : scissor_big_image},
            {'paper'    : paper_big_image}
           ]


player_main_label = Label(mainWindow,
                          image="",
                          relief="raised",
                          bd=2)
player_main_label.place(x=10, y=10, width=256, height=381)

pygame.mixer.init()
pygame.mixer.music.load('Resources/tracks/rock_paper_scissor.mp3')

def play_and_check_who_won(player_selected_choice):
    global user_won_count, computer_won_count
    status_str.set("")
    pygame.mixer.music.play()
    for selected in options:
        if player_selected_choice in selected:
            player_main_label.config(image=list(selected.values())[0])

    for i in range(3):
        computer_choice = random.choice(options)
        image_to_set = list(computer_choice.values())[0]
        computer_main_label.config(image=image_to_set)
        time.sleep(1.5)
        mainWindow.update_idletasks()

    choosen_computer_choice = list(computer_choice.keys())[0]

    ans = get_winner(player_selected_choice, choosen_computer_choice)
    if ans == "Tie":
        status_str.set("TIE!")
    elif ans == False:
        computer_won_count += 1
        computer_score_str.set("Computer Score : " + str(computer_won_count))
        status_str.set("Computer Won!")
    elif ans == True:
        user_won_count += 1
        player_score_str.set("Player Score : " + str(user_won_count))
        status_str.set("You Won!")

def rock_control_handler():
    play_and_check_who_won(player_selected_choice='rock')

player_choice_1 =  Button(mainWindow,
                          image=rock_small_image, command=rock_control_handler)
player_choice_1.place(x=10,y=395, height=100, width=85)

def paper_control_handler():
    play_and_check_who_won(player_selected_choice='paper')

player_choice_2 =  Button(mainWindow,
                          image=paper_small_image, command=paper_control_handler)
player_choice_2.place(x=96,y=395, height=100, width=85)


def scissor_control_handler():
    play_and_check_who_won(player_selected_choice='scissor')

player_choice_3 =  Button(mainWindow,
                          image=scissor_small_image, command=scissor_control_handler)
player_choice_3.place(x=182,y=395, height=100, width=85)
player_score_str= StringVar()
player_score_str.set("Player Score : " + str(user_won_count))
player_score_label = Label(mainWindow, textvariable=player_score_str,
                           font=(None, 12))
player_score_label.place(x=10, y=500, width=255, height=25)


computer_main_label = Label(mainWindow,
                          image="",
                          relief="raised",
                          bd=2)
computer_main_label.place(x=270, y=10, width=256, height=381)

computer_choice_1 =  Button(mainWindow,
                          image=rock_small_image)
computer_choice_1.place(x=270,y=395, height=100, width=85)
computer_choice_1.config(state="disabled")

computer_choice_2 =  Button(mainWindow,
                          image=paper_small_image)
computer_choice_2.place(x=356,y=395, height=100, width=85)
computer_choice_2.config(state="disabled")

computer_choice_3 =  Button(mainWindow,
                          image=scissor_small_image)
computer_choice_3.place(x=442,y=395, height=100, width=85)
computer_choice_3.config(state="disabled")

computer_score_str= StringVar()
computer_score_str.set("Computer Score : " + str(computer_won_count))
computer_score_label = Label(mainWindow, textvariable=computer_score_str,
                             font=(None,12))
computer_score_label.place(x=270, y=500, width=255, height=25)

status_str = StringVar()
status_str.set("WELCOME TO ROCK PAPER SCISSOR GAME!")
status_label = Label(mainWindow, textvariable=status_str,
                     relief="raised",
                     font=(None,16),
                     bd=2)
status_label.place(x=10, y=530, width=516, height=40)

mainWindow.geometry("538x600")
mainWindow.resizable(False, False)
mainWindow.mainloop()