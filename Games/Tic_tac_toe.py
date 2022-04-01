from tkinter import Button, Label
import tkinter as tk
import time
import random
import pygame

available_options = []
marked_options = {}
btn_obj_list = []

mainWindow = tk.Tk()
mainWindow.title("Tic Tac Toe Game")

user_score = 0
computer_score = 0

def mouse_button_release(event):
    global available_options, marked_options, user_won
    wid = event.widget
    state = wid.cget("state")
    if state == "active":
        wid.config(text="0", state="disabled", bg="red")
        mainWindow.update_idletasks()
        pygame.mixer.music.load("Resources/tracks/selected_one.mp3")
        pygame.mixer.music.play()
        available_options.remove(wid)

        marked_options[str(wid)[2:]]  = wid
        check_winner(marked_options, "user")
        if user_won or len(available_options) == 9:
            user_won = False
            return

        time.sleep(1)

        if len(available_options):
            marked_move = random.choice(available_options)
            marked_move.config(text="X",  state="disabled", bg="green")
            mainWindow.update_idletasks()
            pygame.mixer.music.load("Resources/tracks/selected_two.mp3")
            pygame.mixer.music.play()
            available_options.remove(marked_move)
            marked_options[str(marked_move)[2:]] = marked_move
            check_winner(marked_options, "computer")
            if user_won:
                user_won = False
                return

def init_game():
    global btn_obj_list
    for r in range(3):
        for c in range(3):
            btn_obj = Button(mainWindow,
                              width=3,  font=("Arial", 50), bg="#eee")
            btn_obj.bind("<ButtonRelease-1>", mouse_button_release)
            btn_obj.grid(row=r, column=c)
            available_options.append(btn_obj)
            btn_obj_list.append(btn_obj)


init_game()

l1 = Label(mainWindow, text="User: 0",
           relief="raised", bd=2,
           font=(None, 20),
           width=12, height=2)
l1.place(x=400, y=60)

l2 = Label(mainWindow, text="Computer: 0",
           relief="raised", bd=2,
           font=(None, 20),
           width=12, height=2)
l2.place(x=400, y=160)

def replay_handler():
    clear_all_data()

reply_btn = Button(mainWindow, text="Replay",
           font=(None, 20),
           width=12, height=2, command=replay_handler)
reply_btn.place(x=400, y=260)


user_won = False

def clear_all_data():
    global available_options, marked_options, btn_obj_list, user_score, computer_score
    for btn in btn_obj_list:
        btn.config(state="active", bg="#eee")
        btn.config(text="")
        marked_options = {}
        available_options = []
        for i in btn_obj_list:
            available_options.append(i)

    l1.config(text="User: " + str(user_score))
    l2.config(text="Computer: " + str(computer_score))


def play_win_animation(b1, b2, b3):
    for i in range(3):
        pygame.mixer.music.load("Resources/tracks/chime_win.mp3")
        pygame.mixer.music.play()
        b1.config(text="")
        b2.config(text="")
        b3.config(text="")
        mainWindow.update_idletasks()
        time.sleep(0.25)
        b1.config(text="0")
        b2.config(text="0")
        b3.config(text="0")
        mainWindow.update_idletasks()
        time.sleep(0.25)

def check_winner(marked_options, user):
    global user_won, user_score, computer_score, available_options
    b1 = marked_options.get('button', False)
    b2 = marked_options.get('button2', False)
    b3 = marked_options.get('button3', False)
    b4 = marked_options.get('button4', False)
    b5 = marked_options.get('button5', False)
    b6 = marked_options.get('button6', False)
    b7 = marked_options.get('button7', False)
    b8 = marked_options.get('button8', False)
    b9 = marked_options.get('button9', False)

    b1 = b1.cget("text") if b1 else False
    b2 = b2.cget("text") if b2 else False
    b3 = b3.cget("text") if b3 else False
    b4 = b4.cget("text") if b4 else False
    b5 = b5.cget("text") if b5 else False
    b6 = b6.cget("text") if b6 else False
    b7 = b7.cget("text") if b7 else False
    b8 = b8.cget("text") if b8 else False
    b9 = b9.cget("text") if b9 else False


    if b1 and b2 and b3:
        if b1 == b2 == b3:
            b1 = marked_options.get('button', False)
            b2 = marked_options.get('button2', False)
            b3 = marked_options.get('button3', False)
            play_win_animation(b1, b2, b3)
            user_won = True

    if b4 and b5 and b6:
        if b4 == b5 == b6:
            b4 = marked_options.get('button4', False)
            b5 = marked_options.get('button5', False)
            b6 = marked_options.get('button6', False)
            play_win_animation(b4, b5, b6)
            user_won = True

    if b7 and b8 and b9:
        if b7 == b8 == b9:
            b7 = marked_options.get('button7', False)
            b8 = marked_options.get('button8', False)
            b9 = marked_options.get('button9', False)
            play_win_animation(b7, b8, b9)
            user_won = True

    if b1 and b5 and b9:
        if b1 == b5 == b9:
            b1 = marked_options.get('button', False)
            b5 = marked_options.get('button5', False)
            b9 = marked_options.get('button9', False)
            play_win_animation(b1, b5, b9)
            user_won = True

    if b3 and b5 and b7:
        if b3 == b5 == b7:
            b3 = marked_options.get('button3', False)
            b5 = marked_options.get('button5', False)
            b7 = marked_options.get('button7', False)
            play_win_animation(b3, b5, b7)
            user_won = True

    if b1 and b4 and b7:
        if b1 == b4 == b7:
            b1 = marked_options.get('button', False)
            b4 = marked_options.get('button4', False)
            b7 = marked_options.get('button7', False)
            play_win_animation(b1, b4, b7)
            user_won = True

    if b2 and b5 and b8:
        if b2 == b5 == b8:
            b2 = marked_options.get('button2', False)
            b5 = marked_options.get('button5', False)
            b8 = marked_options.get('button8', False)
            play_win_animation(b2, b5, b8)
            user_won = True

    if b3 and b6 and b9:
        if b3 == b6 == b9:
            b3 = marked_options.get('button3', False)
            b6 = marked_options.get('button6', False)
            b9 = marked_options.get('button9', False)
            play_win_animation(b3, b6, b9)
            user_won = True

    if user_won:
        if user == "user":
            user_score += 1
        if user == "computer":
            computer_score += 1

    if user_won  or len(available_options) == 0:
        clear_all_data()

pygame.mixer.init()

mainWindow.config(padx=10, pady=10, bg="#ddd")
mainWindow.geometry("620x415")
mainWindow.resizable(False, False)
mainWindow.mainloop()