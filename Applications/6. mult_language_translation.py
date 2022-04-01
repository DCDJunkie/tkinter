#!/usr/bin/env python
from translate import Translator
from tkinter import StringVar, Label, ttk, Button, Entry
import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Multi Language Translator")

def eng_to_other_language_translation(selected_lang, input_str):
    translator = Translator(to_lang=selected_lang)
    translation_str = translator.translate(input_str)
    return translation_str

output_str = StringVar()
info_label = Label(mainWindow, text="Enter message here:")
info_label.pack()
info_label.config(pady=15)

input_entry = Entry(mainWindow,
                  relief="raised",
                  bd=2,
                  font=("Arial", 15))
input_entry.pack(fill="x", padx=15, pady=10)

def translate_handler():
    lang = selected_lang.get()
    input_str = input_entry.get()
    output_str.set(eng_to_other_language_translation(lang, input_str))


selected_lang = StringVar()
lang_cb = ttk.Combobox(mainWindow, textvariable=selected_lang)
lang_cb['state'] = 'readonly'
languages = ['Gujarati', 'Hindi', 'German', 'Spanish', 'Chinese']
lang_cb['values'] = [m for m in languages]
lang_cb.set('Gujarati')
lang_cb.pack()

translate_btn = Button(mainWindow, text="Translate", command=translate_handler)
translate_btn.config(padx=43, pady=10)
translate_btn.pack(pady=10)

output_label = Label(mainWindow, textvariable=output_str)
output_label.pack(fill="x", padx=20, pady=10)
output_label.config(relief="raised", bd="2", height=6, font=("Arial", 24))

mainWindow.geometry("800x450")
mainWindow.resizable(False, False)
mainWindow.mainloop()