from tkinter import StringVar, Button, Frame
import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Tic Tac Toe Game")

current_data = '1'

btn_1_text = StringVar()
btn_2_text = StringVar()
btn_3_text = StringVar()
btn_4_text = StringVar()
btn_5_text = StringVar()
btn_6_text = StringVar()
btn_7_text = StringVar()
btn_8_text = StringVar()
btn_9_text = StringVar()

btn_11_text = StringVar()
btn_12_text = StringVar()

last_player_played = None
player1_score = 0
player2_score = 0

btn_1_text.set("")
btn_2_text.set("")
btn_3_text.set("")
btn_4_text.set("")
btn_5_text.set("")
btn_6_text.set("")
btn_7_text.set("")
btn_8_text.set("")
btn_9_text.set("")

frame = Frame(mainWindow, relief = 'sunken', bd = 1)
frame.pack(fill = 'both', expand = True,
           padx = 10, pady = 10)

def check_winner():
    global last_player_played
    global player1_score, player2_score
    user_won = False

    if last_player_played == None:
        last_player_played = 1
    elif last_player_played == 1:
        last_player_played = 2
    elif last_player_played == 2:
        last_player_played = 1


    b1 = btn_1_text.get()
    b2 = btn_2_text.get()
    b3 = btn_3_text.get()

    b4 = btn_4_text.get()
    b5 = btn_5_text.get()
    b6 = btn_6_text.get()

    b7 = btn_7_text.get()
    b8 = btn_8_text.get()
    b9 = btn_9_text.get()

    if b1 and b2 and b3:
        if b1 == b2 == b3:
            user_won = True

    if b4 and b5 and b6:
        if b4 == b5 == b6:
            user_won = True

    if b7 and b8 and b9:
        if b7 == b8 == b9:
            user_won = True

    if b1 and b5 and b9:
        if b1 == b5 == b9:
            user_won = True

    if b3 and b5 and b7:
        if b3 == b5 == b7:
            user_won = True

    if b1 and b4 and b7:
        if b1 == b4 == b7:
            user_won = True

    if b2 and b5 and b8:
        if b2 == b5 == b8:
            user_won = True

    if b3 and b6 and b9:
        if b3 == b6 == b9:
            user_won = True

    if user_won == True:
        clear_all_data()
        if last_player_played == 1:
            player1_score += 1
            btn_11_text.set("P1 Score: " + str(player1_score))
        elif last_player_played == 2:
            player2_score += 1
            btn_12_text.set("P2 Score: " + str(player2_score))

def get_data():
    global current_data
    if current_data == '0':
        current_data = "X"
    else:
        current_data = "0"
    return current_data

def btn1_handler():
    data = get_data()
    btn_1_text.set(data)
    check_winner()
    btn_1.config(state="disabled")

btn_1 = Button(frame, textvariable=btn_1_text, width=14, height=7, command=btn1_handler)
btn_1.grid(row=0, column=0)

def btn2_handler():
    data = get_data()
    btn_2_text.set(data)
    check_winner()
    btn_2.config(state="disabled")

btn_2 = Button(frame, textvariable=btn_2_text, width=14, height=7, command=btn2_handler)
btn_2.grid(row=0, column=1)

def btn3_handler():
    data = get_data()
    btn_3_text.set(data)
    check_winner()
    btn_3.config(state="disabled")

btn_3 = Button(frame, textvariable=btn_3_text, width=14, height=7, command=btn3_handler)
btn_3.grid(row=0, column=2)


def btn4_handler():
    data = get_data()
    btn_4_text.set(data)
    check_winner()
    btn_4.config(state="disabled")

btn_4 = Button(frame, textvariable=btn_4_text, width=14, height=7, command=btn4_handler)
btn_4.grid(row=1, column=0)

def btn5_handler():
    data = get_data()
    btn_5_text.set(data)
    check_winner()
    btn_5.config(state="disabled")

btn_5 = Button(frame, textvariable=btn_5_text, width=14, height=7, command=btn5_handler)
btn_5.grid(row=1, column=1)

def btn6_handler():
    data = get_data()
    btn_6_text.set(data)
    check_winner()
    btn_6.config(state="disabled")

btn_6 = Button(frame, textvariable=btn_6_text, width=14, height=7, command=btn6_handler)
btn_6.grid(row=1, column=2)

def btn7_handler():
    data = get_data()
    btn_7_text.set(data)
    check_winner()
    btn_7.config(state="disabled")

btn_7 = Button(frame, textvariable=btn_7_text, width=14, height=7, command=btn7_handler)
btn_7.grid(row=2, column=0)

def btn8_handler():
    data = get_data()
    btn_8_text.set(data)
    check_winner()
    btn_8.config(state="disabled")

btn_8 = Button(frame, textvariable=btn_8_text, width=14, height=7, command=btn8_handler)
btn_8.grid(row=2, column=1)

def btn9_handler():
    data = get_data()
    btn_9_text.set(data)
    check_winner()
    btn_9.config(state="disabled")

btn_9 = Button(frame, textvariable=btn_9_text, width=14, height=7, command=btn9_handler)
btn_9.grid(row=2, column=2)

def clear_all_data():
    btn_1_text.set("")
    btn_2_text.set("")
    btn_3_text.set("")
    btn_4_text.set("")
    btn_5_text.set("")
    btn_6_text.set("")
    btn_7_text.set("")
    btn_8_text.set("")
    btn_9_text.set("")

    btn_1.config(state="normal")
    btn_2.config(state="normal")
    btn_3.config(state="normal")
    btn_4.config(state="normal")
    btn_5.config(state="normal")
    btn_6.config(state="normal")
    btn_7.config(state="normal")
    btn_8.config(state="normal")
    btn_9.config(state="normal")

btn_10 = Button(frame, text = "Replay", width=14, height=4, command=clear_all_data)
btn_10.grid(row=3, column=0)

def btn11_handler():
    btn_11_text.set("0")

btn_11 = Button(frame, textvariable=btn_11_text, width=14, height=4, command=btn8_handler)
btn_11.grid(row=3, column=1)
btn_11_text.set("P1 Score: 00")

def btn12_handler():
    btn_12_text.set("0")

btn_12 = Button(frame, textvariable=btn_12_text, width=14, height=4, command=btn9_handler)
btn_12.grid(row=3, column=2)
btn_12_text.set("P2 Score: 00")

mainWindow.geometry("348x450")
mainWindow.resizable(False, False)
mainWindow.mainloop()