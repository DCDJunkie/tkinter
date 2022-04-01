from tkinter import StringVar, Label, Button, Entry
import tkinter as tk
from ttkwidgets import CheckboxTreeview

mainWindow = tk.Tk()
mainWindow.title("Task Checklist")

tree = CheckboxTreeview(mainWindow)
tree.place(x=10, y=100, width=290)

task_list = []
with open("task_data.txt", "r") as task_data_fp:
    for line in task_data_fp.readlines():
        task_list.append(line)

for index, item in enumerate(task_list):
    data = item.split()
    tree.insert('', tk.END, text=data[0])
    if data[1] == "checked":
        tree._check_ancestor(tree.get_children()[index])


def add_item_handler():
    task = task_str.get()
    if len(task.strip()):
        tree.insert('', tk.END, text=task)
        task_str.set("")

task_label = Label(mainWindow,
                   text="Add a Task",
                   font=("Arial", 12))
task_label.place(x=10, y=10, height=25)


task_str = StringVar()
task_entry = Entry(mainWindow, textvariable=task_str)
task_entry.place(x=100, y=10, height=25, width=200)

add_item_btn = Button(mainWindow, text="Add",
                          command=add_item_handler,
                          pady=6, padx=20)
add_item_btn.place(x=10,y=50, width=140)


def delete_item_handler():
    if len(tree.selection()):
        selected_item = tree.selection()[0]
        tree.delete(selected_item)

delete_btn = Button(mainWindow, text="Delete",
                    pady=6, padx=20, command=delete_item_handler)
delete_btn.place(x=160,y=50, width=140)

def save_item_handler():
    with open("task_data.txt", "w") as task_file_fp:
        for item in tree.get_children():
            isChecked = tree.tag_has('checked', item)
            isCheckedStr = "checked" if isChecked else "unchecked"
            data = tree.item(item).get('text')
            data = data + " " + isCheckedStr
            if data[-1] != "\n":
                task_file_fp.write(data + "\n")
            else:
                task_file_fp.write(data)

save_btn = Button(mainWindow, text="Save",
                    pady=6, padx=20, command=save_item_handler)
save_btn.place(x=10,y=340, width=290)


mainWindow.geometry("315x390")
mainWindow.mainloop()