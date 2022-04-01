#!/usr/bin/env python
import tkinter as tk
from tkinter import Button, Entry, Label, PhotoImage
import qrcode
from PIL import Image
mainWindow = tk.Tk()
mainWindow.title("QR Code Generator")

qr_image = None
def generate_qr_code():
    global qr_image
    data = input_entry.get()
    img = qrcode.make(data)
    img.save('MyQRCode1.png')

    image = Image.open('MyQRCode1.png')
    image.thumbnail((200, 200))
    image.save('MyQRCode1.png')

    qr_image = PhotoImage(file="MyQRCode1.png")
    qr_code_label.config(image = qr_image)


info_label = Label(mainWindow, text="Enter message here to generate QR Code:")
info_label.pack()
info_label.config(pady=15)

input_entry = Entry(mainWindow,
                  relief="raised",
                  bd=2,
                  font=("Arial", 15))
input_entry.pack(fill="x", padx=50, pady=10)

generate_btn = Button(mainWindow, text="Generate QR Code", command=generate_qr_code)
generate_btn.config(padx=10,pady=10)
generate_btn.pack()

qr_code_label = Label(mainWindow)
qr_code_label.place(x=300, y=160, width=200, height=200)

mainWindow.geometry("800x380")
mainWindow.resizable(False, False)
mainWindow.mainloop()