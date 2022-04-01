#!/usr/bin/env python
import tkinter as tk
from tkinter import Button, Entry, Label, PhotoImage, StringVar, Toplevel
mainWindow = tk.Tk()
mainWindow.title("Marse Code Translation")

morse_code_dict = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ' ' : '|'}


def str_to_marse_code(input_str):
    marse_str = ""
    for index, i in enumerate(input_str):
        if i.upper() in morse_code_dict.keys():
            marse_str += morse_code_dict[i.upper()]
            if index != len(input_str)-1:
                marse_str += " "
    return marse_str

def marse_code_to_str(input_marse_str):
    morse_str_dict = {morse_pattern:letter for letter,morse_pattern in morse_code_dict.items()}
    out_str = ""
    input_marse_str = input_marse_str.split()
    for pattern in input_marse_str:
        if pattern in morse_str_dict.keys():
            out_str += morse_str_dict[pattern]
    return out_str

marse_out_str = StringVar()
info_label = Label(mainWindow, text="Enter message here:")
info_label.pack()
info_label.config(pady=15)

input_entry = Entry(mainWindow,
                  relief="raised",
                  bd=2,
                  font=("Arial", 15))
input_entry.pack(fill="x", padx=50, pady=10)

def marse_code_hand():
    input_str = input_entry.get()
    output_str = str_to_marse_code(input_str)
    marse_out_str.set(output_str)

generate_marse_code_from_str_btn = Button(mainWindow, text="String to Morse Code", command=marse_code_hand)
generate_marse_code_from_str_btn.config(padx=10,pady=10)
generate_marse_code_from_str_btn.pack()

def str_code_hand():
    input_str = input_entry.get()
    output_str = marse_code_to_str(input_str)
    marse_out_str.set(output_str)

generate_str_from_marse_code_btn = Button(mainWindow, text="Marse Code to String", command=str_code_hand)
generate_str_from_marse_code_btn.config(padx=10,pady=10)
generate_str_from_marse_code_btn.pack(padx=10,pady=10)

output_label = Label(mainWindow, textvariable=marse_out_str)
output_label.pack(fill="x", padx=20, pady=10)
output_label.config(relief="raised", bd="2", height=3, font=("Arial", 24))

def marse_code_format_handler():
    global morse_code_dict
    newWind = Toplevel(mainWindow)

    morse_code_image_label = Label(newWind)
    morse_code_image = PhotoImage(file="morse_Codes_data.png")
    morse_code_image_label.place(x=10, y=10, width=360, height=495)
    morse_code_image_label.config(image=morse_code_image)

    newWind.title('Morse Code Lookup')
    morse_code_image_label.pack()
    newWind.geometry("380x505")
    newWind.resizable(False, False)
    newWind.mainloop()


marse_code_format_btn = Button(mainWindow, text="Marse codes", command=marse_code_format_handler)
marse_code_format_btn.config(padx=10,pady=10)
marse_code_format_btn.pack()

mainWindow.geometry("800x500")
mainWindow.resizable(False, False)
mainWindow.mainloop()