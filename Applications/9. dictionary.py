#!/usr/bin/env python
import tkinter as tk
from tkinter import Button, Entry, Label, StringVar
from urllib.request import urlopen
from bs4 import BeautifulSoup

mainWindow = tk.Tk()
mainWindow.title("Dictionary")

word_info = StringVar()
def get_dict_data_from_weblink():
    my_dict = {}
    nifty_url = "https://ielts.com.au/australia/prepare/article-100-new-english-words-and-phrases-updated-2020"
    page = urlopen(nifty_url)
    soup =  BeautifulSoup(page, 'html.parser')
    dict_val = soup.find_all('div', {'class' : 'article-wrapper'})
    all_words = dict_val[0].findAll('td')

    index = 0
    for i in range(1,len(all_words),2):
        my_dict[all_words[index].get_text().strip().lower()] = all_words[i].get_text()
        index += 1
    return my_dict

words = get_dict_data_from_weblink()
for i in words.items():
    print(i)
input_entry = Entry(mainWindow,
                  relief="raised",
                  bd=2,
                  font=("Arial", 15))
input_entry.config(width="55")
input_entry.place(x=10, y=10)

def search_handler():
    global words
    selected_word = input_entry.get()
    if selected_word.lower() in words.keys():
        word_info.set(words[selected_word.lower()])
    else:
        word_info.set(selected_word + " is not found in the dictionary")


search_button = Button(mainWindow, text="Search", pady=2, padx=20, command=search_handler)
search_button.place(x=630, y=10)


word_label = Label(mainWindow, text="Word: ", font=("Arial", 14))
word_label.place(x=10, y=50)
word_entry_str = StringVar()
word_entry = Entry(mainWindow,
                   textvariable=word_entry_str,
                   relief="raised",
                   bd=2,
                   font=("Arial", 15))
word_entry.place(x=80, y=50)

word_def_label = Label(mainWindow, text="Define: ", font=("Arial", 14))
word_def_label.place(x=320, y=50)
word_def_str = StringVar()
word_def_entry = Entry(mainWindow,
                       textvariable=word_def_str,
                       relief="raised",
                       bd=2,
                       font=("Arial", 15))
word_def_entry.place(x=395, y=50)

def add_handler():
    global words
    word_info.set("")
    word = word_entry.get()
    definition = word_def_entry.get()
    if word != "" and definition != "":
        words[word.lower()] = definition
        word_info.set("New word " + word + " is added.")
        word_entry_str.set("")
        word_def_str.set("")

add_button = Button(mainWindow, text="Add", pady=2, padx=26, command=add_handler)
add_button.place(x=630, y=50)

info_label = Label(mainWindow, textvariable=word_info, font=("Arial", 16), wraplength=500)
info_label.place(x=10, y=90)
info_label.config(relief="raised", bd="2", width=58, height=5)

mainWindow.geometry("730x255")
mainWindow.resizable(False, False)
mainWindow.mainloop()