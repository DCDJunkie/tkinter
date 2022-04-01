#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk
from tkinter import StringVar, Button, filedialog, Entry
from zipfile import ZipFile
import os
from tkinter.scrolledtext import ScrolledText

mainWindow = tk.Tk()
mainWindow.title("Zip Files")

directory_ptr = None
files_ptr = None
file_paths = []

def get_all_file_paths(directory):
    global file_paths
    file_paths = []
    for current_dir, sub_dir, files in os.walk(directory):
        for file in files:
            filepath = os.path.join(current_dir, file)
            file_paths.append(filepath)


def create_zip_for_files(files, folderName="result.zip"):
    zip_creted = False
    with ZipFile(folderName, 'w') as zip:
        textWindow.config(state="normal")
        textWindow.delete('1.0', "end")
        total_files = len(files)
        files = [file.split("/")[-1] for file in files]

        for index, file in enumerate(files):
            zip.write(file)
            textWindow.insert("insert", "Zipping of " + file + " is done.\n")
            current_progress = int(((index+1)*100)/total_files)
            zip_progress['value'] = current_progress
            textWindow.update_idletasks()
        else:
            textWindow.config(state="disabled")
            zip_creted = True

    return zip_creted

def open_dir_handler():
    global directory_ptr, file_paths
    directory_ptr = filedialog.askdirectory(initialdir="./../")

    if directory_ptr:
        save_file_button.config(state="normal")
        file_name_entry.config(state="normal")
        save_file_name_str.set("result.zip")
        zip_progress['value'] = 0
        get_all_file_paths(directory_ptr)

        textWindow.config(state="normal")
        textWindow.delete('1.0', "end")
        textWindow.insert("insert", "Total " + str(len(file_paths)) + " files are selected to zip.\n")

        for index, file in enumerate(file_paths):
            textWindow.insert("insert","(" + str(index+1) + ") " + file + "\n")
        textWindow.config(state="disabled")


    
open_dir_button = Button(mainWindow, text="Select Directory", pady=2, padx=5,
                    font=("Arial", 12),
                    command=open_dir_handler)
open_dir_button.place(x=10, y=10)

def open_file_handler():
    global files_ptr, file_paths
    files_ptr = filedialog.askopenfilenames(initialdir=".")

    if files_ptr:
        save_file_button.config(state="normal")
        file_paths = list(files_ptr)
        file_name_entry.config(state="normal")
        zip_progress['value'] = 0
        save_file_name_str.set("result.zip")

        textWindow.config(state="normal")
        textWindow.delete('1.0', "end")
        textWindow.insert("insert", "Total " + str(len(file_paths)) + " files are selected to zip.\n")

        for index, file in enumerate(file_paths):
            textWindow.insert("insert", "(" + str(index + 1) + ") " + file + "\n")
        textWindow.config(state="disabled")

open_file_button = Button(mainWindow, text="Select Files", pady=2, padx=5,
                    font=("Arial", 12),
                    command=open_file_handler)
open_file_button.place(x=148, y=10)

save_file_name_str = StringVar()
file_name_entry = Entry(mainWindow, textvariable=save_file_name_str,
                        font=("Arial", 12))
file_name_entry.place(x=260, y=10, height=35)
file_name_entry.config(state="disabled")

def save_file_handler():
    global file_paths
    zip_file_name = save_file_name_str.get()
    if zip_file_name != "" and len(zip_file_name.strip()):
        zip_success = create_zip_for_files(file_paths, zip_file_name)

        if zip_success:
            file_paths = []
            textWindow.config(state="normal")
            textWindow.insert("insert", "\nZip file " + file_name_entry.get() +"  is successfully created.")
            textWindow.config(state="disabled")


save_file_button = Button(mainWindow, text="Save Zip file", pady=2, padx=5,
                    font=("Arial", 12),
                    command=save_file_handler)
save_file_button.config(state="disabled")
save_file_button.place(x=452, y=10)

zip_file_ptr = None
def select_zip_file_handler():
    global zip_file_ptr
    zip_file_ptr = filedialog.askopenfilename(title="Select a zip file",
                                           initialdir=".",
                                           filetypes=(("Zip files", "*.zip"),))

    if zip_file_ptr:
        extract_file_button.config(state="normal")
        zip_progress['value'] = 0
        textWindow.config(state="normal")
        textWindow.delete('1.0', "end")
        textWindow.update_idletasks()
        textWindow.config(state="disabled")


select_zip_file_button = Button(mainWindow, text="Select Zip file", pady=2, padx=5,
                    font=("Arial", 12),
                    command=select_zip_file_handler)

select_zip_file_button.place(x=565, y=10)

def extract_files_handler():
    global zip_file_ptr

    if zip_file_ptr:
        with ZipFile(zip_file_ptr, 'r') as zip:
            textWindow.config(state="normal")
            textWindow.delete('1.0', "end")
            zip.printdir()
            zip.extractall("extract_result")
            textWindow.insert("insert", "\nAll files are succeffuly extracted.\n")
            textWindow.update_idletasks()
            textWindow.config(state="disabled")
            zip_progress['value'] = 100


extract_file_button = Button(mainWindow, text="Extract Zip file", pady=2, padx=5,
                    font=("Arial", 12),
                    command=extract_files_handler)
extract_file_button.config(state="disabled")
extract_file_button.place(x=685, y=10)

textWindow = ScrolledText(mainWindow, wrap = "word")
textWindow.config(font=("Microsoft Himalaya", 20), state="disabled")
textWindow.place(x=10,y=60, height = 450, width = 800)

zip_progress = ttk.Progressbar(mainWindow, orient="horizontal")
zip_progress.config(length=800)
zip_progress.place(x=10, y=520)

mainWindow.geometry("815x550")
# mainWindow.resizable(False, False)
mainWindow.mainloop()

