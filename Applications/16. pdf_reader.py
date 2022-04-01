from tkinter import Button, filedialog
import tkinter as tk
from tkPDFViewer import tkPDFViewer

mainWindow = tk.Tk()
mainWindow.title("PDF Reader")

def open_handler():
    fp = filedialog.askopenfilename(
                                    initialdir=".",
                                    filetypes=(("PDF FiLeS", "*.pdf"),))
    if fp:
        show_obj = tkPDFViewer.ShowPdf()
        show_obj.img_object_li.clear()
        pdf_view = show_obj.pdf_view(mainWindow,
                         pdf_location=fp)
        pdf_view.place(x=10, y=60, width=985, height=520)


openButton = Button(mainWindow, text="Select PDF file", command=open_handler)
openButton.place(x=8,y=8)
openButton.config(width=20, height=2)

mainWindow.geometry("1200x600")
mainWindow.resizable(False, False)
mainWindow.mainloop()