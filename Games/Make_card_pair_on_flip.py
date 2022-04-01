import time
from tkinter import StringVar, Label, Button
import tkinter as tk
import random


mainWindow = tk.Tk()
mainWindow.title("Flip a Card Game")

open_card_with_btn_obj = {}

x_postions_list = [10, 95, 180, 265, 350, 435, 520, 605, 690, 775, 860, 945, 1030]
y_poitions_list = [50, 165, 280, 395]

card_positions_list = []

for y_pos in y_poitions_list:
    for x_pos in x_postions_list:
        card_positions_list.append([x_pos, y_pos])

game_score = {
    'user_1' : 0,
    'user_2' : 0
}

current_user = 1
user_1_won = False
user_2_won = False
user_won = None

def get_current_user():
    global current_user
    if current_user == 1:
        current_user = 2
    elif current_user == 2:
        current_user =1

def on_user_won(btn1, btn2, current_user):
    global user_won
    if current_user == 1:
        user_won = 1
    elif current_user == 2:
        user_won = 2
    game_score['user_{}'.format(user_won)] = game_score['user_{}'.format(user_won)] + 1
    time.sleep(0.5)
    btn1.destroy()
    btn2.destroy()

########################################################################################333

def btn_1_clicked():
    global current_user, card_positions_list, card_positions_list
    btn_1.config(state="disabled", text="A",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_1.update_idletasks()
    if "A" in open_card_with_btn_obj:
        on_user_won(btn_1, open_card_with_btn_obj["A"], current_user)
        del open_card_with_btn_obj["A"]
    else:
        open_card_with_btn_obj["A"] = btn_1
        get_current_user()


btn_1= Button(mainWindow, command=btn_1_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_1.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_2_clicked():
    global current_user, card_positions_list
    btn_2.config(state="disabled", text="2",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_2.update_idletasks()
    if "2" in open_card_with_btn_obj:
        on_user_won(btn_2, open_card_with_btn_obj["2"], current_user)
        del open_card_with_btn_obj["2"]
    else:
        open_card_with_btn_obj["2"] = btn_2
        get_current_user()


btn_2 = Button(mainWindow, command=btn_2_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_2.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_3_clicked():
    global current_user, card_positions_list
    btn_3.config(state="disabled", text="3",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_3.update_idletasks()
    if "3" in open_card_with_btn_obj:
        on_user_won(btn_3, open_card_with_btn_obj["3"], current_user)
        del open_card_with_btn_obj["3"]
    else:
        open_card_with_btn_obj["3"] = btn_3
        get_current_user()


btn_3 = Button(mainWindow, command=btn_3_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_3.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_4_clicked():
    global current_user, card_positions_list
    btn_4.config(state="disabled", text="4",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_4.update_idletasks()
    if "4" in open_card_with_btn_obj:
        on_user_won(btn_4, open_card_with_btn_obj["4"], current_user)
        del open_card_with_btn_obj["4"]
    else:
        open_card_with_btn_obj["4"] = btn_4
        get_current_user()


btn_4 = Button(mainWindow, command=btn_4_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_4.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_5_clicked():
    global current_user, card_positions_list
    btn_5.config(state="disabled", text="5",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_5.update_idletasks()
    if "5" in open_card_with_btn_obj:
        on_user_won(btn_5, open_card_with_btn_obj["5"], current_user)
        del open_card_with_btn_obj["5"]
    else:
        open_card_with_btn_obj["5"] = btn_5
        get_current_user()


btn_5 = Button(mainWindow, command=btn_5_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_5.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_6_clicked():
    global current_user, card_positions_list
    btn_6.config(state="disabled", text="6",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_6.update_idletasks()
    if "6" in open_card_with_btn_obj:
        on_user_won(btn_6, open_card_with_btn_obj["6"], current_user)
        del open_card_with_btn_obj["6"]
    else:
        open_card_with_btn_obj["6"] = btn_6
        get_current_user()


btn_6 = Button(mainWindow, command=btn_6_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_6.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_7_clicked():
    global current_user, card_positions_list
    btn_7.config(state="disabled", text="7",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_7.update_idletasks()
    if "7" in open_card_with_btn_obj:
        on_user_won(btn_7, open_card_with_btn_obj["7"], current_user)
        del open_card_with_btn_obj["7"]
    else:
        open_card_with_btn_obj["7"] = btn_7
        get_current_user()


btn_7 = Button(mainWindow, command=btn_7_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_7.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_8_clicked():
    global current_user, card_positions_list
    btn_8.config(state="disabled", text="8",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_8.update_idletasks()
    if "8" in open_card_with_btn_obj:
        on_user_won(btn_8, open_card_with_btn_obj["8"], current_user)
        del open_card_with_btn_obj["8"]
    else:
        open_card_with_btn_obj["8"] = btn_8
        get_current_user()


btn_8 = Button(mainWindow, command=btn_8_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_8.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_9_clicked():
    global current_user, card_positions_list
    btn_9.config(state="disabled", text="9",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_9.update_idletasks()
    if "9" in open_card_with_btn_obj:
        on_user_won(btn_9, open_card_with_btn_obj["9"], current_user)
        del open_card_with_btn_obj["9"]
    else:
        open_card_with_btn_obj["9"] = btn_9
        get_current_user()


btn_9 = Button(mainWindow, command=btn_9_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_9.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_10_clicked():
    global current_user, card_positions_list
    btn_10.config(state="disabled", text="10",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_10.update_idletasks()
    if "10" in open_card_with_btn_obj:
        on_user_won(btn_10, open_card_with_btn_obj["10"], current_user)
        del open_card_with_btn_obj["10"]
    else:
        open_card_with_btn_obj["10"] = btn_10
        get_current_user()


btn_10 = Button(mainWindow, command=btn_10_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_10.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_11_clicked():
    global current_user, card_positions_list
    btn_11.config(state="disabled", text="J",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_11.update_idletasks()
    if "J" in open_card_with_btn_obj:
        on_user_won(btn_11, open_card_with_btn_obj["J"], current_user)
        del open_card_with_btn_obj["J"]
    else:
        open_card_with_btn_obj["J"] = btn_11
        get_current_user()


btn_11 = Button(mainWindow, command=btn_11_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_11.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_12_clicked():
    global current_user, card_positions_list
    btn_12.config(state="disabled", text="Q",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_12.update_idletasks()
    if "Q" in open_card_with_btn_obj:
        on_user_won(btn_12, open_card_with_btn_obj["Q"], current_user)
        del open_card_with_btn_obj["Q"]
    else:
        open_card_with_btn_obj["Q"] = btn_12
        get_current_user()


btn_12 = Button(mainWindow, command=btn_12_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_12.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_13_clicked():
    global current_user, card_positions_list
    btn_13.config(state="disabled", text="K",
                  bg="red", fg="white",
                 font=(None, 50))
    btn_13.update_idletasks()
    if "K" in open_card_with_btn_obj:
        on_user_won(btn_13, open_card_with_btn_obj["K"], current_user)
        del open_card_with_btn_obj["K"]
    else:
        open_card_with_btn_obj["K"] = btn_13
        get_current_user()


btn_13 = Button(mainWindow, command=btn_13_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_13.place(x=card_positions[0], y=card_positions[1], width=80, height=110)
########################################################################################


def btn_14_clicked():
    global current_user, card_positions_list
    btn_14.config(state="disabled", text="A",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_14.update_idletasks()
    if "A" in open_card_with_btn_obj:
        on_user_won(btn_14, open_card_with_btn_obj["A"], current_user)
        del open_card_with_btn_obj["A"]
    else:
        open_card_with_btn_obj["A"] = btn_14
        get_current_user()

btn_14 = Button(mainWindow, command=btn_14_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_14.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_15_clicked():
    global current_user, card_positions_list
    btn_15.config(state="disabled", text="2",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_15.update_idletasks()
    if "2" in open_card_with_btn_obj:
        on_user_won(btn_15, open_card_with_btn_obj["2"], current_user)
        del open_card_with_btn_obj["2"]
    else:
        open_card_with_btn_obj["2"] = btn_15
        get_current_user()


btn_15 = Button(mainWindow, command=btn_15_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_15.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_16_clicked():
    global current_user, card_positions_list
    btn_16.config(state="disabled", text="3",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_16.update_idletasks()
    if "3" in open_card_with_btn_obj:
        on_user_won(btn_16, open_card_with_btn_obj["3"], current_user)
        del open_card_with_btn_obj["3"]
    else:
        open_card_with_btn_obj["3"] = btn_16
        get_current_user()


btn_16 = Button(mainWindow, command=btn_16_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_16.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_17_clicked():
    global current_user, card_positions_list
    btn_17.config(state="disabled", text="4",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_17.update_idletasks()
    if "4" in open_card_with_btn_obj:
        on_user_won(btn_17, open_card_with_btn_obj["4"], current_user)
        del open_card_with_btn_obj["4"]
    else:
        open_card_with_btn_obj["4"] = btn_17
        get_current_user()


btn_17 = Button(mainWindow, command=btn_17_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_17.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_18_clicked():
    global current_user, card_positions_list
    btn_18.config(state="disabled", text="5",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_18.update_idletasks()
    if "5" in open_card_with_btn_obj:
        on_user_won(btn_18, open_card_with_btn_obj["5"], current_user)
        del open_card_with_btn_obj["5"]
    else:
        open_card_with_btn_obj["5"] = btn_18
        get_current_user()


btn_18 = Button(mainWindow, command=btn_18_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_18.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_19_clicked():
    global current_user, card_positions_list
    btn_19.config(state="disabled", text="6",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_19.update_idletasks()
    if "6" in open_card_with_btn_obj:
        on_user_won(btn_19, open_card_with_btn_obj["6"], current_user)
        del open_card_with_btn_obj["6"]
    else:
        open_card_with_btn_obj["6"] = btn_19
        get_current_user()


btn_19 = Button(mainWindow, command=btn_19_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_19.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_20_clicked():
    global current_user, card_positions_list
    btn_20.config(state="disabled", text="7",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_20.update_idletasks()
    if "7" in open_card_with_btn_obj:
        on_user_won(btn_20, open_card_with_btn_obj["7"], current_user)
        del open_card_with_btn_obj["7"]
    else:
        open_card_with_btn_obj["7"] = btn_20
        get_current_user()


btn_20 = Button(mainWindow, command=btn_20_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_20.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_21_clicked():
    global current_user, card_positions_list
    btn_21.config(state="disabled", text="8",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_21.update_idletasks()
    if "8" in open_card_with_btn_obj:
        on_user_won(btn_21, open_card_with_btn_obj["8"], current_user)
        del open_card_with_btn_obj["8"]
    else:
        open_card_with_btn_obj["8"] = btn_21
        get_current_user()


btn_21 = Button(mainWindow, command=btn_21_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_21.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_22_clicked():
    global current_user, card_positions_list
    btn_22.config(state="disabled", text="9",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_22.update_idletasks()
    if "9" in open_card_with_btn_obj:
        on_user_won(btn_22, open_card_with_btn_obj["9"], current_user)
        del open_card_with_btn_obj["9"]
    else:
        open_card_with_btn_obj["9"] = btn_22
        get_current_user()


btn_22 = Button(mainWindow, command=btn_22_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_22.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_23_clicked():
    global current_user, card_positions_list
    btn_23.config(state="disabled", text="10",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_23.update_idletasks()
    if "10" in open_card_with_btn_obj:
        on_user_won(btn_23, open_card_with_btn_obj["10"], current_user)
        del open_card_with_btn_obj["10"]
    else:
        open_card_with_btn_obj["10"] = btn_23
        get_current_user()


btn_23 = Button(mainWindow, command=btn_23_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_23.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_24_clicked():
    global current_user, card_positions_list
    btn_24.config(state="disabled", text="J",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_24.update_idletasks()
    if "J" in open_card_with_btn_obj:
        on_user_won(btn_24, open_card_with_btn_obj["J"], current_user)
        del open_card_with_btn_obj["J"]
    else:
        open_card_with_btn_obj["J"] = btn_24
        get_current_user()


btn_24 = Button(mainWindow, command=btn_24_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_24.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_25_clicked():
    global current_user, card_positions_list
    btn_25.config(state="disabled", text="Q",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_25.update_idletasks()
    if "Q" in open_card_with_btn_obj:
        on_user_won(btn_25, open_card_with_btn_obj["Q"], current_user)
        del open_card_with_btn_obj["Q"]
    else:
        open_card_with_btn_obj["Q"] = btn_25
        get_current_user()


btn_25 = Button(mainWindow, command=btn_25_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_25.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_26_clicked():
    global current_user, card_positions_list
    btn_26.config(state="disabled", text="K",
                  bg="green", fg="white",
                 font=(None, 50))
    btn_26.update_idletasks()
    if "K" in open_card_with_btn_obj:
        on_user_won(btn_26, open_card_with_btn_obj["K"], current_user)
        del open_card_with_btn_obj["K"]
    else:
        open_card_with_btn_obj["K"] = btn_26
        get_current_user()

btn_26 = Button(mainWindow, command=btn_26_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_26.place(x=card_positions[0], y=card_positions[1], width=80, height=110)
########################################################################################

def btn_27_clicked():
    global current_user, card_positions_list
    btn_27.config(state="disabled", text="A",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_27.update_idletasks()
    if "A" in open_card_with_btn_obj:
        on_user_won(btn_27, open_card_with_btn_obj["A"], current_user)
        del open_card_with_btn_obj["A"]
    else:
        open_card_with_btn_obj["A"] = btn_27
        get_current_user()


btn_27 = Button(mainWindow, command=btn_27_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_27.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_28_clicked():
    global current_user, card_positions_list
    btn_28.config(state="disabled", text="2",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_28.update_idletasks()
    if "2" in open_card_with_btn_obj:
        on_user_won(btn_28, open_card_with_btn_obj["2"], current_user)
        del open_card_with_btn_obj["2"]
    else:
        open_card_with_btn_obj["2"] = btn_28
        get_current_user()


btn_28 = Button(mainWindow, command=btn_28_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_28.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_29_clicked():
    global current_user, card_positions_list
    btn_29.config(state="disabled", text="3",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_29.update_idletasks()
    if "3" in open_card_with_btn_obj:
        on_user_won(btn_29, open_card_with_btn_obj["3"], current_user)
        del open_card_with_btn_obj["3"]
    else:
        open_card_with_btn_obj["3"] = btn_29
        get_current_user()


btn_29 = Button(mainWindow, command=btn_29_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_29.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_30_clicked():
    global current_user, card_positions_list
    btn_30.config(state="disabled", text="4",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_30.update_idletasks()
    if "4" in open_card_with_btn_obj:
        on_user_won(btn_30, open_card_with_btn_obj["4"], current_user)
        del open_card_with_btn_obj["4"]
    else:
        open_card_with_btn_obj["4"] = btn_30
        get_current_user()


btn_30 = Button(mainWindow, command=btn_30_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_30.place(x=card_positions[0], y=card_positions[1], width=80, height=110)


def btn_31_clicked():
    global current_user, card_positions_list
    btn_31.config(state="disabled", text="5",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_31.update_idletasks()
    if "5" in open_card_with_btn_obj:
        on_user_won(btn_31, open_card_with_btn_obj["5"], current_user)
        del open_card_with_btn_obj["5"]
    else:
        open_card_with_btn_obj["5"] = btn_31
        get_current_user()


btn_31 = Button(mainWindow, command=btn_31_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_31.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_32_clicked():
    global current_user, card_positions_list
    btn_32.config(state="disabled", text="6",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_32.update_idletasks()
    if "6" in open_card_with_btn_obj:
        on_user_won(btn_32, open_card_with_btn_obj["6"], current_user)
        del open_card_with_btn_obj["6"]
    else:
        open_card_with_btn_obj["6"] = btn_32
        get_current_user()


btn_32 = Button(mainWindow, command=btn_32_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_32.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_33_clicked():
    global current_user, card_positions_list
    btn_33.config(state="disabled", text="7",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_33.update_idletasks()
    if "7" in open_card_with_btn_obj:
        on_user_won(btn_33, open_card_with_btn_obj["7"], current_user)
        del open_card_with_btn_obj["7"]
    else:
        open_card_with_btn_obj["7"] = btn_33
        get_current_user()


btn_33 = Button(mainWindow, command=btn_33_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_33.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_34_clicked():
    global current_user, card_positions_list
    btn_34.config(state="disabled", text="8",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_34.update_idletasks()
    if "8" in open_card_with_btn_obj:
        on_user_won(btn_34, open_card_with_btn_obj["8"], current_user)
        del open_card_with_btn_obj["8"]
    else:
        open_card_with_btn_obj["8"] = btn_34
        get_current_user()


btn_34 = Button(mainWindow, command=btn_34_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_34.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_35_clicked():
    global current_user, card_positions_list
    btn_35.config(state="disabled", text="9",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_35.update_idletasks()
    if "9" in open_card_with_btn_obj:
        on_user_won(btn_35, open_card_with_btn_obj["9"], current_user)
        del open_card_with_btn_obj["9"]
    else:
        open_card_with_btn_obj["9"] = btn_35
        get_current_user()


btn_35 = Button(mainWindow, command=btn_35_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_35.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_36_clicked():
    global current_user, card_positions_list
    btn_36.config(state="disabled", text="10",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_36.update_idletasks()
    if "10" in open_card_with_btn_obj:
        on_user_won(btn_36, open_card_with_btn_obj["10"], current_user)
        del open_card_with_btn_obj["10"]
    else:
        open_card_with_btn_obj["10"] = btn_36
        get_current_user()


btn_36 = Button(mainWindow, command=btn_36_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_36.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_37_clicked():
    global current_user, card_positions_list
    btn_37.config(state="disabled", text="J",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_37.update_idletasks()
    if "J" in open_card_with_btn_obj:
        on_user_won(btn_37, open_card_with_btn_obj["J"], current_user)
        del open_card_with_btn_obj["J"]
    else:
        open_card_with_btn_obj["J"] = btn_37
        get_current_user()


btn_37 = Button(mainWindow, command=btn_37_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_37.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_38_clicked():
    global current_user, card_positions_list
    btn_38.config(state="disabled", text="Q",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_38.update_idletasks()
    if "Q" in open_card_with_btn_obj:
        on_user_won(btn_38, open_card_with_btn_obj["Q"], current_user)
        del open_card_with_btn_obj["Q"]
    else:
        open_card_with_btn_obj["Q"] = btn_38
        get_current_user()


btn_38 = Button(mainWindow, command=btn_38_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_38.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_39_clicked():
    global current_user, card_positions_list
    btn_39.config(state="disabled", text="K",
                  bg="blue", fg="white",
                 font=(None, 50))
    btn_39.update_idletasks()
    if "K" in open_card_with_btn_obj:
        on_user_won(btn_39, open_card_with_btn_obj["K"], current_user)
        del open_card_with_btn_obj["K"]
    else:
        open_card_with_btn_obj["K"] = btn_39
        get_current_user()


btn_39 = Button(mainWindow, command=btn_39_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_39.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

########################################################################################

def btn_40_clicked():
    global current_user, card_positions_list
    btn_40.config(state="disabled", text="A",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_40.update_idletasks()
    if "A" in open_card_with_btn_obj:
        on_user_won(btn_40, open_card_with_btn_obj["A"], current_user)
        del open_card_with_btn_obj["A"]
    else:
        open_card_with_btn_obj["A"] = btn_40
        get_current_user()


btn_40 = Button(mainWindow, command=btn_40_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_40.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_41_clicked():
    global current_user, card_positions_list
    btn_41.config(state="disabled", text="2",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_41.update_idletasks()
    if "2" in open_card_with_btn_obj:
        on_user_won(btn_41, open_card_with_btn_obj["2"], current_user)
        del open_card_with_btn_obj["2"]
    else:
        open_card_with_btn_obj["2"] = btn_41
        get_current_user()


btn_41 = Button(mainWindow, command=btn_41_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_41.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_42_clicked():
    global current_user, card_positions_list
    btn_42.config(state="disabled", text="3",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_42.update_idletasks()
    if "3" in open_card_with_btn_obj:
        on_user_won(btn_42, open_card_with_btn_obj["3"], current_user)
        del open_card_with_btn_obj["3"]
    else:
        open_card_with_btn_obj["3"] = btn_42
        get_current_user()


btn_42 = Button(mainWindow, command=btn_42_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_42.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_43_clicked():
    global current_user, card_positions_list
    btn_43.config(state="disabled", text="4",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_43.update_idletasks()
    if "4" in open_card_with_btn_obj:
        on_user_won(btn_43, open_card_with_btn_obj["4"], current_user)
        del open_card_with_btn_obj["4"]
    else:
        open_card_with_btn_obj["4"] = btn_43
        get_current_user()


btn_43 = Button(mainWindow, command=btn_43_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_43.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_44_clicked():
    global current_user, card_positions_list
    btn_44.config(state="disabled", text="5",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_44.update_idletasks()
    if "5" in open_card_with_btn_obj:
        on_user_won(btn_44, open_card_with_btn_obj["5"], current_user)
        del open_card_with_btn_obj["5"]
    else:
        open_card_with_btn_obj["5"] = btn_44
        get_current_user()


btn_44 = Button(mainWindow, command=btn_44_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_44.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_45_clicked():
    global current_user, card_positions_list
    btn_45.config(state="disabled", text="6",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_45.update_idletasks()
    if "6" in open_card_with_btn_obj:
        on_user_won(btn_45, open_card_with_btn_obj["6"], current_user)
        del open_card_with_btn_obj["6"]
    else:
        open_card_with_btn_obj["6"] = btn_45
        get_current_user()


btn_45 = Button(mainWindow, command=btn_45_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_45.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_46_clicked():
    global current_user, card_positions_list
    btn_46.config(state="disabled", text="7",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_46.update_idletasks()
    if "7" in open_card_with_btn_obj:
        on_user_won(btn_46, open_card_with_btn_obj["7"], current_user)
        del open_card_with_btn_obj["7"]
    else:
        open_card_with_btn_obj["7"] = btn_46
        get_current_user()


btn_46 = Button(mainWindow, command=btn_46_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_46.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_47_clicked():
    global current_user, card_positions_list
    btn_47.config(state="disabled", text="8",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_47.update_idletasks()
    if "8" in open_card_with_btn_obj:
        on_user_won(btn_47, open_card_with_btn_obj["8"], current_user)
        del open_card_with_btn_obj["8"]
    else:
        open_card_with_btn_obj["8"] = btn_47
        get_current_user()


btn_47 = Button(mainWindow, command=btn_47_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_47.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_48_clicked():
    global current_user, card_positions_list
    btn_48.config(state="disabled", text="9",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_48.update_idletasks()
    if "9" in open_card_with_btn_obj:
        on_user_won(btn_48, open_card_with_btn_obj["9"], current_user)
        del open_card_with_btn_obj["9"]
    else:
        open_card_with_btn_obj["9"] = btn_48
        get_current_user()


btn_48 = Button(mainWindow, command=btn_48_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_48.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_49_clicked():
    global current_user, card_positions_list
    btn_49.config(state="disabled", text="10",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_49.update_idletasks()
    if "10" in open_card_with_btn_obj:
        on_user_won(btn_49, open_card_with_btn_obj["10"], current_user)
        del open_card_with_btn_obj["10"]
    else:
        open_card_with_btn_obj["10"] = btn_49
        get_current_user()


btn_49 = Button(mainWindow, command=btn_49_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_49.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_50_clicked():
    global current_user, card_positions_list
    btn_50.config(state="disabled", text="J",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_50.update_idletasks()
    if "J" in open_card_with_btn_obj:
        on_user_won(btn_50, open_card_with_btn_obj["J"], current_user)
        del open_card_with_btn_obj["J"]
    else:
        open_card_with_btn_obj["J"] = btn_50
        get_current_user()


btn_50 = Button(mainWindow, command=btn_50_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_50.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_51_clicked():
    global current_user, card_positions_list
    btn_51.config(state="disabled", text="Q",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_51.update_idletasks()
    if "Q" in open_card_with_btn_obj:
        on_user_won(btn_51, open_card_with_btn_obj["Q"], current_user)
        del open_card_with_btn_obj["Q"]
    else:
        open_card_with_btn_obj["Q"] = btn_51
        get_current_user()


btn_51 = Button(mainWindow, command=btn_51_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_51.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

def btn_52_clicked():
    global current_user, card_positions_list
    btn_52.config(state="disabled", text="K",
                  bg="orange", fg="white",
                 font=(None, 50))
    btn_52.update_idletasks()
    if "K" in open_card_with_btn_obj:
        on_user_won(btn_52, open_card_with_btn_obj["K"], current_user)
        del open_card_with_btn_obj["K"]
    else:
        open_card_with_btn_obj["K"] = btn_52
        get_current_user()


btn_52 = Button(mainWindow, command=btn_52_clicked, bg="pink")
card_positions = card_positions_list.pop(random.randrange(len(card_positions_list)))
btn_52.place(x=card_positions[0], y=card_positions[1], width=80, height=110)

########################################################################################

whose_tunr_str = StringVar()
whose_turn_label = Label(mainWindow, textvariable=whose_tunr_str,
                         font=(None, 14), relief="raised", bd=2)
whose_turn_label.place(x=10, y=10, width=1100)

def who_is_current_user():
    print("current_user:",current_user, game_score)
    whose_tunr_str.set("Turn : " + str(current_user) + "\tPlayer1 Score: " + str(game_score['user_1'])
                       + "\tPlayer2 Score: " + str(game_score['user_2']))
    mainWindow.after(1000, who_is_current_user)

who_is_current_user()

mainWindow.geometry("1125x535")
mainWindow.resizable(False, False)
mainWindow.mainloop()