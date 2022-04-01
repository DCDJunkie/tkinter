import smtplib
from tkinter import StringVar, Button, Label, filedialog,  \
    ttk, PhotoImage, Scale, Entry
import tkinter as tk
from tkinter.scrolledtext import ScrolledText

mainWindow = tk.Tk()
mainWindow.title("Email Sender")

smtp_server = None
is_login_success = False

def login_with_credential(login_id, password):
    global smtp_server, is_login_success
    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(login_id, password)
        status_str.set("Logged in Successfully! Welcome : " + login_id)
        is_login_success = True
    except smtplib.SMTPAuthenticationError:
        status_str.set("Username/Password is not accepted")
    except Exception as e:
        status_str.set("Connection Rejected, Try again...")

def send_email(sent_from, send_to_list, email_subject, email_body):
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
        status_str.set("Email to " + send_to_list[0] + " was successfully sent.")
        subject_entry_str.set("")
        send_to_entry_str.set("")
        textWindow.delete('1.0', "end")
        send_status = True
    except Exception as ex:
        send_status = False
        status_str.set("Error : ", str(ex))
    return send_status

def enable_disable_on_login(enable_state):
    set_state = "normal" if enable_state else "disabled"
    send_to_entry.config(state=set_state)
    subject_entry.config(state=set_state)
    textWindow.config(state=set_state)
    send_button.config(state=set_state)


email_id_label = Label(mainWindow, text="Email ID:", font=("Arial", 14))
email_id_label.place(x=10, y=12)
email_id_str = StringVar()
email_id_entry = Entry(mainWindow,
                   textvariable=email_id_str,
                   relief="raised",
                   bd=2,
                   font=("Arial", 12))
email_id_entry.place(x=95, y=10, height=34)

def email_id_handler(event):
    email_id = email_id_str.get()
    if len(email_id.strip()) != 0 and "@" in email_id and ".com" in email_id:
        password_entry.config(state="normal")
    else:
        password_entry.config(state="disabled")

email_id_entry.bind("<KeyRelease>", email_id_handler)

password_label = Label(mainWindow, text="Password:", font=("Arial", 14))
password_label.place(x=308, y=12)
password_entry_str = StringVar()
password_entry = Entry(mainWindow,
                       textvariable=password_entry_str,
                       relief="raised",
                       bd=2,
                       font=("Arial", 12),
                       show="*")
password_entry.place(x=405, y=10, height=34)
password_entry.config(state="disabled")

def password_handler(event):
    password = password_entry_str.get()
    if len(password.strip()) >= 4:
        login_button.config(state="normal")
    else:
        login_button.config(state="disabled")

password_entry.bind("<KeyRelease>", password_handler)


def login_handler():
    global smtp_server
    if login_logout_str.get() == "Login":
        login_id = email_id_str.get()
        password = password_entry_str.get()
        login_with_credential(login_id, password)
        if is_login_success:
            enable_disable_on_login(enable_state=is_login_success)
            password_entry.config(state="disabled")
            email_id_entry.config(state="disabled")
            email_id_str.set("")
            password_entry_str.set("")
            login_logout_str.set("Logout")
    elif login_logout_str.get() == "Logout":
        login_logout_str.set("Login")
        smtp_server.close()
        email_id_str.set("")
        password_entry.config(state="normal")
        email_id_entry.config(state="normal")
        password_entry_str.set("")
        subject_entry_str.set("")
        send_to_entry_str.set("")
        textWindow.delete('1.0', "end")
        status_str.set("")
        enable_disable_on_login(enable_state=False)

login_logout_str = StringVar()
login_logout_str.set("Login")
login_button = Button(mainWindow, textvariable=login_logout_str, pady=2, padx=26,
                    font=("Arial", 12),
                    command=login_handler)
login_button.place(x=605, y=10)
login_button.config(state="disabled")

status_str = StringVar()
status_label = Label(mainWindow,
                     textvariable=status_str,
                     relief="raised",
                     bd=1)
status_label.place(x=95,y=50, width=615 , height=25)

send_to_entry_str = StringVar()
send_to_label = Label(mainWindow, text="Send to:",
                      font=("Arial", 12))
send_to_label.place(x=10, y=82)
send_to_entry = Entry(mainWindow,
                       textvariable=send_to_entry_str,
                       relief="raised",
                       bd=2,
                       font=("Arial", 12))
send_to_entry.place(x=95, y=80, height=34, width=615)

subject_entry_str = StringVar()
subject_label = Label(mainWindow, text="Subject:",
                      font=("Arial", 12))
subject_label.place(x=10, y=122)
subject_entry = Entry(mainWindow,
                       textvariable=subject_entry_str,
                       relief="raised",
                       bd=2,
                       font=("Arial", 12))
subject_entry.place(x=95, y=120, height=34, width=615)

message_label = Label(mainWindow, text="Message:",
                      font=("Arial", 12))
message_label.place(x=10, y=162)
textWindow = ScrolledText(mainWindow, wrap = "word",
                          font=("Arial", 12))
textWindow.focus()
textWindow.place(x=95,y=160, height = 200, width = 615)

def send_handler():
    login_id = email_id_entry.get()
    send_to = send_to_entry_str.get()
    send_to_list = send_to.split(",")
    subject = subject_entry_str.get()
    email_body = textWindow.get("1.0", "end")

    send_email(login_id, send_to_list, subject, email_body)

send_button = Button(mainWindow, text="Send", pady=12, padx=282,
                    font=("Arial", 12),
                    command=send_handler)
send_button.place(x=95, y=370)

enable_disable_on_login(enable_state=False)

mainWindow.geometry("730x446")
mainWindow.resizable(False, False)
mainWindow.mainloop()