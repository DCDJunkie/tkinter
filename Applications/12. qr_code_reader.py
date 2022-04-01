#!/usr/bin/env python
import tkinter as tk
from tkinter import Button, Label, PhotoImage, filedialog, StringVar
from PIL import Image
mainWindow = tk.Tk()
mainWindow.title("QR Code Reader")
mainWindow.config(pady=20)

qr_image = None
qr_info = StringVar()
qr_file_ptr = None

def select_qr_code():
    global qr_image, qr_file_ptr
    qr_file_ptr = filedialog.askopenfilename(
                                    initialdir=".",
                                    filetypes=(("PNG Files", "*.png"),))

    if qr_file_ptr:
        qr_info.set("")
        image = Image.open(qr_file_ptr)
        image.thumbnail((200, 200))
        image.save(qr_file_ptr)
        qr_image = PhotoImage(file=qr_file_ptr)
        qr_code_label.config(image=qr_image, pady=10)


select_btn = Button(mainWindow, text="Select a QR code to read", command=select_qr_code)
select_btn.config(padx=10,pady=10)
select_btn.pack()

def read_qr_code():
    import cv2
    img = cv2.imread(qr_file_ptr)
    det = cv2.QRCodeDetector()
    val, pts, st_code = det.detectAndDecode(img)
    qr_info.set(val)


qr_code_label = Label(mainWindow)
qr_code_label.pack(pady=10)

read_btn = Button(mainWindow, text="Read QR code", command=read_qr_code)
read_btn.config(padx=10,pady=10)
read_btn.pack()


info_label = Label(mainWindow, textvariable=qr_info)
info_label.pack(fill="x", padx=20, pady=10)
info_label.config(relief="raised", bd="2", height=3)

mainWindow.geometry("800x450")
mainWindow.resizable(False, False)
mainWindow.mainloop()