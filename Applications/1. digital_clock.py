#!/usr/bin/env python
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import StringVar, Label, font, Button
import calendar

mainWindow = tk.Tk()
mainWindow.title("Digial Calender")

date_time_str = StringVar()
font_index = 0
font_families = list(font.families())

month_dict = {"1" : "January",
              "2" : "February",
              "3" : "March",
              "4" : "April",
              "5" : "May",
              "6" : "June",
              "7" : "July",
              "8" : "August",
              "9" : "September",
              "10" : "October",
              "11" : "November",
              "12" : "December"}

def update_date_time():
    global font_index
    day = datetime.today().strftime('%A')
    month = datetime.today().strftime('%B')
    year = datetime.today().strftime('%G')
    time = datetime.today().strftime('%X')
    date = datetime.today().strftime('%d')

    date_time_full_str = month + " " + date + " " + year + "\n" \
                         + day + " " + time

    date_time_str.set(date_time_full_str)
    date_time_label.config(font=("Agency FB", "40"))

    font_index = font_index+1

    date_time_label.after(1000,update_date_time)

current_month = int(datetime.today().strftime('%m'))
current_year = int(datetime.today().strftime('%Y'))

def get_list_for_month_year(month, year):
    date_data_list = []
    cal = calendar.monthcalendar(year, month)
    for n in range(len(cal)):
        dateItems = [" " if x == 0 else x for x in cal[n]]
        dateItems = ["0" + str(x) if x != " " and int(x) < 10 else x for x in dateItems  ]
        date_data_list.append(dateItems)
    return date_data_list

date_time_label = Label(mainWindow, textvariable=date_time_str,
                        width="60",
                        height="3",
                        bg="black",
                        fg = "white",
                        font=("Gabriola",40))
date_time_label.pack(anchor="center")
update_date_time()

def update_calender_month_data_in_table(data):
    global current_month,current_year
    for item in tree.get_children():
        tree.delete(item)
    for day in data:
        tree.insert('', tk.END, values=day)
    data_str = month_dict[str(current_month)] + "/" + str(current_year)
    cur_date_str.set(data_str)

def prev_hand():
    global current_month, current_year, month_dict
    if current_month == 1:
        current_month = 12
        current_year -= 1
    else:
        current_month -= 1
    data = get_list_for_month_year(current_month, current_year)
    update_calender_month_data_in_table(data)

prev_str = StringVar()
prev_btn = Button(mainWindow, textvariable=prev_str, command=prev_hand)
prev_btn.config(bg="black",
                fg="white",
                font=("Gabriola",14),
                height=1,
                padx=3, width=15)
prev_btn.place(x=60,y=300)
prev_str.set("Previous Month")

def next_hand():
    global current_month, current_year
    if current_month == 12:
        current_month = 1
        current_year += 1
    else:
        current_month += 1
    data = get_list_for_month_year(current_month, current_year)
    update_calender_month_data_in_table(data)

next_str = StringVar()
next_btn = Button(mainWindow, textvariable=next_str, command=next_hand)
next_btn.config(bg="black",
                fg="white",
                font=("Gabriola",14),
                height=1,
                padx=3,width=15)
next_btn.place(x=620,y=300)
next_str.set("Next Month")

cur_date_str = StringVar()
cur_date_label = Label(mainWindow, textvariable=cur_date_str)
cur_date_label.place(x=230,y=200)
cur_date_label.config(bg="black",
                fg="white",
                font=("Gabriola",20),
                height=1,
                padx=3,
                width=31)
cur_date_str.set(month_dict[str(current_month)] + "/" + str(current_year))

columns = ('SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT')
tree = ttk.Treeview(mainWindow, columns=columns, show='headings')
tree.column("# 1", width="50",  anchor="center")
tree.column("# 2", width="50",  anchor="center")
tree.column("# 3", width="50",  anchor="center")
tree.column("# 4", width="50",  anchor="center")
tree.column("# 5", width="50",  anchor="center")
tree.column("# 6", width="50",  anchor="center")
tree.column("# 7", width="50",  anchor="center")

tree.heading('SUN', text='SUN')
tree.heading('MON', text='MON')
tree.heading('TUE', text='TUE')
tree.heading('WED', text='WED')
tree.heading('THU', text='THU')
tree.heading('FRI', text='FRI')
tree.heading('SAT', text='SAT')
tree.config(height=6)

calendar.setfirstweekday(calendar.SUNDAY)
for day in get_list_for_month_year(current_month, current_year):
    tree.insert('', tk.END, values=day)

tree.place(x=230,y=258)

blank_label= Label(mainWindow)
blank_label.place(x=230,y=407)
blank_label.config(bg="black",
                fg="white",
                padx=3,
                width=49,height=2)

mainWindow.geometry("800x460")
mainWindow.resizable(False, False)
mainWindow.mainloop()