#!/usr/bin/env python
import tkinter as tk
from tkinter import StringVar, Button, Entry

mainWindow = tk.Tk()
mainWindow.title("Calculator")

ans = StringVar()
ans_entry = Entry(mainWindow,
                  relief="raised",
                  bd=5, width=20,
                  font=("Arial", 15))
ans_entry.grid(row=0, column=0, columnspan=4)
ans_entry.config(bg="green", fg="white")
# ans_entry.config(state="disabled")

ans_eval_dict = {}

def disable_op():
    btn_div.config(state="disabled")
    btn_plus.config(state="disable")
    btn_sub.config(state="disable")
    btn_mul.config(state="disable")


def enable_op():
    btn_div.config(state="normal")
    btn_plus.config(state="normal")
    btn_sub.config(state="normal")
    btn_mul.config(state="normal")


# ------------------------------------------------------
def one_hand():
    global ans
    ans = "1"
    ans_entry.insert(len(ans_entry.get()), ans)


btn_1 = Button(mainWindow, text="1", padx=20, pady=10, command=one_hand)
btn_1.grid(row=1, column=0)


def two_hand():
    global ans
    ans = "2"
    ans_entry.insert(len(ans_entry.get()), ans)


btn_2 = Button(mainWindow, text="2", padx=20, pady=10, command=two_hand)
btn_2.grid(row=1, column=1)


def three_hand():
    global ans
    ans = "3"
    ans_entry.insert(len(ans_entry.get()), ans)


btn_3 = Button(mainWindow, text="3", padx=20, pady=10, command=three_hand)
btn_3.grid(row=1, column=2)


def div_hand():
    global ans
    ans_eval_dict['val1'] = float(ans_entry.get())
    ans_entry.delete(0, "end")
    ans_eval_dict['op'] = "/"
    disable_op()


btn_div = Button(mainWindow, text="/", padx=20, pady=10, command=div_hand)
btn_div.grid(row=1, column=3)


# ------------------------------------------------------

def four_hand():
    global ans
    ans = "4"
    ans_entry.insert(len(ans_entry.get()), ans)


btn_4 = Button(mainWindow, text="4", padx=20, pady=10, command=four_hand)
btn_4.grid(row=2, column=0)


def five_hand():
    global ans
    ans = "5"
    ans_entry.insert(len(ans_entry.get()), ans)


btn_5 = Button(mainWindow, text="5", padx=20, pady=10, command=five_hand)
btn_5.grid(row=2, column=1)


def six_hand():
    global ans
    ans = "6"
    ans_entry.insert(len(ans_entry.get()), ans)


btn_6 = Button(mainWindow, text="6", padx=20, pady=10, command=six_hand)
btn_6.grid(row=2, column=2)


def mul_hand():
    global ans
    ans_eval_dict['val1'] = float(ans_entry.get())
    ans_entry.delete(0, "end")
    ans_eval_dict['op'] = "*"
    disable_op()


btn_mul = Button(mainWindow, text="*", padx=20, pady=10, command=mul_hand)
btn_mul.grid(row=2, column=3)


# ------------------------------------------------------

# ------------------------------------------------------
def seven_hand():
    global ans
    ans = "7"
    ans_entry.insert(len(ans_entry.get()), ans)


btn_7 = Button(mainWindow, text="7", padx=20, pady=10, command=seven_hand)
btn_7.grid(row=3, column=0)


def eight_hand():
    global ans
    ans = "8"
    ans_entry.insert(len(ans_entry.get()), ans)


btn_8 = Button(mainWindow, text="8", padx=20, pady=10, command=eight_hand)
btn_8.grid(row=3, column=1)


def nine_hand():
    global ans
    ans = "9"
    ans_entry.insert(len(ans_entry.get()), ans)


btn_9 = Button(mainWindow, text="9", padx=20, pady=10, command=nine_hand)
btn_9.grid(row=3, column=2)


def sub_hand():
    global ans
    ans_eval_dict['val1'] = float(ans_entry.get())
    ans_entry.delete(0, "end")
    ans_eval_dict['op'] = "-"
    disable_op()


btn_sub = Button(mainWindow, text="-", padx=20, pady=10, command=sub_hand)
btn_sub.grid(row=3, column=3)


# ------------------------------------------------------
def clr_hand():
    ans_entry.delete(0, "end")
    enable_op()


btn_clear = Button(mainWindow, text="C", padx=20, pady=10, command=clr_hand)
btn_clear.grid(row=4, column=0)


def zero_hand():
    global ans
    ans = "0"
    ans_entry.insert(len(ans_entry.get()), ans)


btn_0 = Button(mainWindow, text="0", padx=20, pady=10, command=zero_hand)
btn_0.grid(row=4, column=1)


def ans_hand():
    ans_eval_dict['val2'] = float(ans_entry.get())
    ans_entry.delete(0, "end")
    calculation_ans = 0.0
    if ans_eval_dict['op'] == '/':
        calculation_ans = ans_eval_dict['val1'] / ans_eval_dict['val2']
    elif ans_eval_dict['op'] == '+':
        calculation_ans = ans_eval_dict['val1'] + ans_eval_dict['val2']
    elif ans_eval_dict['op'] == '-':
        calculation_ans = ans_eval_dict['val1'] - ans_eval_dict['val2']
    elif ans_eval_dict['op'] == '*':
        calculation_ans = ans_eval_dict['val1'] * ans_eval_dict['val2']
    elif ans_eval_dict['op'] == '%':
        calculation_ans = ans_eval_dict['val1'] % ans_eval_dict['val2']

    ans_entry.insert(0, calculation_ans)
    ans_eval_dict.clear()
    enable_op()


btn_ans = Button(mainWindow, text="=", padx=20, pady=10, command=ans_hand)
btn_ans.grid(row=4, column=2)


def plus_hand():
    global ans
    ans_eval_dict['val1'] = float(ans_entry.get())
    ans_entry.delete(0, "end")
    ans_eval_dict['op'] = "+"
    disable_op()


btn_plus = Button(mainWindow, text="+", padx=20, pady=10, command=plus_hand)
btn_plus.grid(row=4, column=3)


# ------------------------------------------------------
def oct_hand():
    octal_numer = oct(int(float(ans_entry.get())))
    octal_numer = octal_numer[2:]
    ans_entry.delete(0, "end")
    ans_entry.insert(0, str(octal_numer))
    disable_op()


btn_oct = Button(mainWindow, text="Oct", padx=15, pady=10, command=oct_hand)
btn_oct.grid(row=5, column=0)


def hex_hand():
    hex_numer = hex(int(float(ans_entry.get())))
    ans_entry.delete(0, "end")
    ans_entry.insert(0, str(hex_numer))
    disable_op()


btn_hex = Button(mainWindow, text="Hexa", padx=10, pady=10, command=hex_hand)
btn_hex.grid(row=5, column=1)


def dot_hand():
    global ans
    ans = "."
    ans_entry.insert(len(ans_entry.get()), ans)


btn_dot = Button(mainWindow, text=".", padx=22, pady=10, command=dot_hand)
btn_dot.grid(row=5, column=2)


def mod_hand():
    global ans
    ans_eval_dict['val1'] = int(ans_entry.get())
    ans_entry.delete(0, "end")
    ans_eval_dict['op'] = "%"
    disable_op()


btn_mod = Button(mainWindow, text="Mod", padx=12, pady=10, command=mod_hand)
btn_mod.grid(row=5, column=3)

mainWindow.mainloop()