from tkinter import StringVar, Label, Button, PhotoImage, Entry, filedialog
from PIL import Image
import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Image Viewer")
data_image = None
image_fp = None

def open_handler():
    global data_image, image_fp
    image_fp = filedialog.askopenfilename(
        initialdir=".",
        filetypes=(("PNG Files", "*.png"),))

    if image_fp:
        data_image = PhotoImage(file=image_fp)
        image_label.config(image=data_image)

open_button = Button(mainWindow, text="Open", pady=2, padx=26,
                    font=("Arial", 12),
                    command=open_handler)
open_button.place(x=10, y=10)

width_label = Label(mainWindow, text="Width: ", font=("Arial", 14))
width_label.place(x=120, y=12)

def width_modified(event):
    global image_fp
    if image_fp:
        w = width_entry_str.get()
        if w != "" and w.isdigit():
            w = int(w)

            image = Image.open(image_fp)
            image_width = image.width
            image_height = image.height

            width_percentage = int((w * 100) / image_width)
            multiply_value = width_percentage/100

            height_set_to = int(image_height * multiply_value)
            height_entry_str.set(height_set_to)


width_entry_str = StringVar()
width_entry = Entry(mainWindow,
                   textvariable=width_entry_str,
                   relief="raised",
                   bd=2,
                   font=("Arial", 12))
width_entry.place(x=190, y=10, height=34)
width_entry.bind("<KeyRelease>", width_modified)

def height_modified(event):
    global image_fp
    if image_fp:
        h = height_entry_str.get()
        if h != "" and h.isdigit():
            h = int(h)

            image = Image.open(image_fp)
            image_width = image.width
            image_height = image.height

            height_percentage = int((h * 100) / image_height)
            multiply_value = height_percentage / 100

            width_set_to = int(image_width * multiply_value)
            width_entry_str.set(width_set_to)

height_label = Label(mainWindow, text="Height: ", font=("Arial", 14))
height_label.place(x=385, y=12)
height_entry_str = StringVar()
height_entry = Entry(mainWindow,
                       textvariable=height_entry_str,
                       relief="raised",
                       bd=2,
                       font=("Arial", 12))
height_entry.place(x=460, y=10, height=34)
height_entry.bind("<KeyRelease>", height_modified)

photo_image = None

def resize_handler():
    global image_fp, photo_image
    if image_fp:
        w = width_entry_str.get()
        h = height_entry_str.get()
        if w != "" and w.isdigit() and h != "" and h.isdigit():
            w = int(w)
            h = int(h)
            image = Image.open(image_fp)
            image.thumbnail((w, h), Image.ANTIALIAS)
            image.save('Sample.png')
            photo_image = PhotoImage(file="Sample.png")
            image_label.config(image=photo_image)

resize_button = Button(mainWindow, text="Resize", pady=2, padx=26,
                    font=("Arial", 12),
                    command=resize_handler)
resize_button.place(x=655, y=10)

def save_handler():
    global image_fp, photo_image
    if image_fp:
        image_save_fp = filedialog.asksaveasfile(
            initialdir=".",
            filetypes=(("PNG Files", "*.png"),),
            defaultextension="*.png")

        if image_save_fp:
            w = width_entry_str.get()
            h = height_entry_str.get()
            if w != "" and w.isdigit() and h != "" and h.isdigit():
                w = int(w)
                h = int(h)
                image = Image.open(image_fp)
                image.thumbnail((w, h), Image.ANTIALIAS)
                image.save(image_save_fp.name)


save_button = Button(mainWindow, text="Save", pady=2, padx=26,
                    font=("Arial", 12),
                    command=save_handler)
save_button.place(x=775, y=10)

image_label = Label(mainWindow)
image_label.config(image="")
image_label.pack(fill="both", pady=50, padx=10)

mainWindow.geometry("890x600")
mainWindow.resizable(False, False)
mainWindow.mainloop()