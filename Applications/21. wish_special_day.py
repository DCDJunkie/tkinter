from tkinter import StringVar, Label, \
    ttk, Button, Radiobutton, Entry
import tkinter as tk
from datetime import datetime, timedelta
import pandas as pd

from tkcalendar import Calendar
import smtplib
smtp_server = None

mail_sent_list = []
name_list = []
email_list = []
event_list = []
date_list = []

def login_with_credential(login_id, password):
    global smtp_server, is_login_success
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(login_id, password)
        is_login_success = True
        status_str.set("Logged in Successfully! Welcome : " + login_id)
    except smtplib.SMTPAuthenticationError:
        status_str.set("Username/Password is not accepted")
    except Exception as e:
        status_str.set("Connection Rejected, Try again...")

def send_email(sent_from, send_to_list, email_subject, email_body):
    global mail_sent_list
    send_status = False
    global smtp_server
    sent_from = sent_from
    send_to_list = send_to_list
    subject = email_subject
    body = email_body

    if not(len(send_to_list[0].strip()) != 0 and "@" in send_to_list[0] and ".com" in send_to_list[0]):
        send_status = False
        return send_status

    try:
        email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(send_to_list), subject, body)
        smtp_server.sendmail(sent_from, send_to_list, email_text)
        # status_str.set("Email to " + send_to_list[0] + " was successfully sent.")
        send_status = True
    except Exception as e:
        print("Error : ", e)
    return send_status


# send_to_list = []
# subject = "Rohit is wishing..."
# email_body = ""
#
# send_email('rohit.eceng@gmail.com', send_to_list, subject, email_body)

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

csv_month_dict = {"Jan" : "January",
              "Feb" : "February",
              "Mar" : "March",
              "Apr" : "April",
              "May" : "May",
              "Jun" : "June",
              "Jul" : "July",
              "Aug" : "August",
              "Sep" : "September",
              "Oct" : "October",
              "Nov" : "November",
              "Dec" : "December"}

current_time = datetime.now()
day = current_time.strftime('%d')
month = current_time.strftime('%m')
year = current_time.strftime('%Y')

mainWindow = tk.Tk()
mainWindow.title("Wish A Special Day")


cal = Calendar(mainWindow, selectmode='day',
               year=int(year), month=int(month),
               day=int(day))

cal.pack(pady=20)

wish_select_str = StringVar()
def rb_hand():
    pass

wish_select_str.set("None")
wishes_option = ["Birthday", "Marriage Anniversary", "Engagement Anniversary"]

name_label = Label(mainWindow,
                   text="Name",
                   font=("Arial", 12))
name_label.place(x=10, y=220, height=25)

name_str = StringVar()
name_entry = Entry(mainWindow, textvariable=name_str)
name_entry.place(x=65, y=220, height=25)

email_label = Label(mainWindow,
                   text="Email",
                   font=("Arial", 12))
email_label.place(x=10, y=270, height=25)

email_str = StringVar()
email_entry = Entry(mainWindow, textvariable=email_str)
email_entry.place(x=65, y=270, height=25, width=200)


val = 0
radio_btn_obj = []
for wish in wishes_option:
    r = Radiobutton(mainWindow, text=wish, value=wish, variable=wish_select_str)
    r.config(padx=20,
             indicatoron=1, width=20, command=rb_hand,
             relief="raised", justify="left")
    r.place(x=200+val, y=220)
    radio_btn_obj.append(r)
    val = val+220



# name, email ,event, date]
def set_reminer_handler():
    name = name_str.get()
    email = email_str.get()
    other_wish = other_wish_str.get()

    if not len(name.strip()):
        status_str.set("Name can not be empty")
        return
    if not(len(email.strip()) != 0 and "@" in email and ".com" in email):
        status_str.set("Invalid email id")
        return

    event = wish_select_str.get()
    if not(event in wishes_option):
        event = other_wish
        if len(other_wish.strip()) == 0:
            status_str.set("Either select wish from radiobutton, or enter in other wish")
            return

    day_month = cal.get_date().split("/")
    day = day_month[1]
    month = month_dict[day_month[0]]
    date = month + " " + day

    data = [name, email ,event, date]

    name_list.append(name)
    email_list.append(email)
    event_list.append(event)
    date_list.append(date)

    dict = {'Name': name_list, 'Email': email_list,
            'EventTpe': event_list, 'Date' : date_list}

    df = pd.DataFrame(dict)
    df.to_csv('wish_data.csv', index=False)

    wish_table.insert('', tk.END, values=data)
    for column in wish_table['column']:
        wish_table.column(column, anchor="center")

    name_str.set("")
    email_str.set("")
    wish_select_str.set("None")
    other_wish_str.set("")
    wish_to_person()
    for obj in radio_btn_obj:
        obj.config(state="normal")

set_reminder_btn = Button(mainWindow, text="Add Wish",
                          command=set_reminer_handler,
                          pady=10, padx=20)
set_reminder_btn.place(x=282,y=260, width=125)



other_label = Label(mainWindow,
                   text="Other wish",
                   font=("Arial", 12))
other_label.place(x=550, y=270, height=25)

other_wish_str = StringVar()
def other_wish_handler(event):
    other_wish = other_wish_str.get()
    if len(other_wish.strip()) != 0:
        wish_select_str.set("None")
        for obj in radio_btn_obj:
            obj.config(state="disabled")
    else:
        for obj in radio_btn_obj:
            obj.config(state="normal")

other_wish_entry = Entry(mainWindow, textvariable=other_wish_str)
other_wish_entry.place(x=640, y=270, height=25, width=205)

other_wish_entry.bind("<KeyRelease>", other_wish_handler)


status_str = StringVar()

status_label = Label(mainWindow,
                     textvariable=status_str,
                     relief="raised",
                     bd=1)
status_label.place(x=10,y=320, width=600 , height=25)

columns = ('Name', 'Email', 'WishTpye', 'WishDate')
wish_table = ttk.Treeview(mainWindow, columns=columns, show='headings')

wish_table.heading('Name', text='Name')
wish_table.heading('Email', text='Email')
wish_table.heading('WishTpye', text='Wish Event')
wish_table.heading('WishDate', text='Wish Date')
wish_table.config(height=10)
wish_table.place(x=10, y=350)

def delete_wish():
    selected_item = wish_table.selection()[0]
    myData = wish_table.item(selected_item)['values']
    name_list.remove(myData[0])
    email_list.remove(myData[1])
    event_list.remove(myData[2])
    date_list.remove(myData[3])
    wish_table.delete(selected_item)

    dict = {'Name': name_list, 'Email': email_list,
            'EventTpe': event_list, 'Date': date_list}

    df = pd.DataFrame(dict)
    df.to_csv('Resources/csv_files/wish_data.csv', index=False)

delete_btn = Button(mainWindow, text="Delete Wish",
                    pady=10, padx=20, command=delete_wish)
delete_btn.place(x=420,y=260, width=125)

df = pd.read_csv('Resources/csv_files/wish_data.csv')
rows = len(df.index)
print(rows)
for row in range(rows):
    data = list(df.iloc[row])
    date_month = data[3].split("-")
    if len(date_month[0]) == 3:
        date_month = csv_month_dict[date_month[0]] + " " + date_month[1]
    else:
        date_month = date_month[0].split()
        date_month = date_month[0] + " " + date_month[1]

    data = [data[0], data[1], data[2], date_month]

    name_list.append(data[0])
    email_list.append(data[1])
    event_list.append(data[2])
    date_list.append(date_month)

    wish_table.insert('', tk.END, values=data)

for column in wish_table['column']:
    wish_table.column(column, anchor="center")

login_with_credential(login_id="email id",
                      password="password")

def wish_to_person():
    global mail_sent_list
    current_time = datetime.now()
    day = int(current_time.strftime('%d'))
    month = int(current_time.strftime('%m'))

    month_str_dict = {month_word: int(month_digit) for month_digit, month_word in month_dict.items()}

    for item in wish_table.get_children():
        wish_details = wish_table.item(item)['values']
        name_to_wish = wish_details[0]
        email = wish_details[1]
        wish_type = wish_details[2]
        month_day_to_wish = wish_details[3].split()
        month_to_wish = int(month_str_dict[month_day_to_wish[0]])
        day_to_wish = int(month_day_to_wish[1])

        if day_to_wish == day and month_to_wish == month:
            send_to_list = [email]
            subject = wish_type.upper()
            email_body = "Happy " + wish_type + " " + name_to_wish

            if smtp_server:
                if send_to_list not in mail_sent_list:
                    if send_email('rohit.eceng@gmail.com', send_to_list, subject, email_body):
                        mail_sent_list.append(send_to_list)
                        status_str.set("Wished " + name_to_wish + " Happy " + wish_type)

wish_to_person()

mainWindow.geometry("860x600")
mainWindow.mainloop()