from tkinter import IntVar, StringVar, Button,\
    Label, filedialog, ttk, font
from tkinter.scrolledtext import ScrolledText
import tkinter as tk
from gtts import gTTS
import gtts
from playsound import playsound
import os

mainWindow = tk.Tk()
mainWindow.title("Notepad")
language = 'en-in'

def open_handler():
    selected_fie_fp = filedialog.askopenfilename(
                                    initialdir="C:\\Users\\111751\\Downloads",
                                    filetypes=(("test file", "*.txt"),
                                               ("PDF FiLeS", "*.pdf")))
    if selected_fie_fp:
        with open(selected_fie_fp, "r") as f:
            textWindow.delete('1.0', "end")
            for line in f.readlines():
                textWindow.insert("insert", line)


openButton = Button(mainWindow, text="Open", command=open_handler)
openButton.place(x=8,y=8)
openButton.config(width=10, height=2)

def save_handler():
    fs = filedialog.asksaveasfile(title="Save a file",
                                    initialdir="C:\\Users\\111751\\Downloads",
                                    filetypes=(("test file", "*.txt"),
                                               ("PDF FiLeS", "*.pdf")),
                                                defaultextension="*.txt")
    if fs:
        content = textWindow.get("1.0","end")
        fs.write(content)

saveButton = Button(mainWindow, text="Save", command=save_handler)
saveButton.place(x=90,y=8)
saveButton.config(width=10, height=2)

selected_language = StringVar()
selected_language.set("Verdana")
selected_font_size = IntVar()
selected_font_size.set(14)

font_family_label = Label(mainWindow, text="Font")
font_family_label.place(x=180,y=8)

def value_changed(event):
    language_set = selected_language.get()
    font_size = selected_font_size.get()
    textWindow.config(font=(language_set,font_size))

font_cb = ttk.Combobox(mainWindow, textvariable=selected_language)
font_cb.bind('<<ComboboxSelected>>', value_changed)

font_families = list(font.families())
font_cb['state'] = 'readonly' #can not type here now.
font_cb['values'] = [m for m in font_families]
font_cb.place(x=180, y=28)
font_cb.config(height=10)

font_family_label = Label(mainWindow, text="Font-size")
font_family_label.place(x=350,y=8)

def value_changed_font_size(event):
    language_set = selected_language.get()
    font_size = selected_font_size.get()
    font_width_value = int(1120/font_size)
    font_height_value = int(252/font_size)
    textWindow.config(font=(language_set, font_size), width=font_width_value, height=font_height_value)

font_size_cb = ttk.Combobox(mainWindow, textvariable=selected_font_size)
font_size_cb.bind('<<ComboboxSelected>>', value_changed_font_size)

font_size_cb['state'] = 'readonly' #can not type here now.
font_size_cb['values'] = [m for m in range(101)]
font_size_cb.place(x=350, y=28)
font_size_cb.config(height=10)

def text_to_speech_handler():
    content = textWindow.get("1.0","end")
    content = content.split("\n")
    # print(gtts.lang.tts_langs())

    if os.path.exists("test.mp3"):
        os.remove("test.mp3")
    for line in content:
        if len(line):
            obj = gTTS(text=line, lang=language, slow=False)
            obj.save("test.mp3")
            playsound("test.mp3")
            if os.path.exists("test.mp3"):
                os.remove("test.mp3")

speakButton = Button(mainWindow, text="Text to Speech", command=text_to_speech_handler)
speakButton.place(x=510,y=8)
speakButton.config(width=15, height=2)

textWindow = ScrolledText(mainWindow, wrap = "word")
textWindow.focus()
textWindow.config(font=(selected_language.get(), selected_font_size.get()))
textWindow.place(x=8,y=60, height = 430, width = 985)

mainWindow.geometry("1000x500")
mainWindow.resizable(False, False)
mainWindow.mainloop()