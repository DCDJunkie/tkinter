from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import ttk
import tkinter as tk
from datetime import datetime

mainWindow = tk.Tk()
mainWindow.title("Live Market Update")

def get_nifty_data_from_weblink():
    nifty_url = "https://www.moneycontrol.com/indian-indices/nifty-50-9.html"
    page = urlopen(nifty_url)
    soup =  BeautifulSoup(page, 'html.parser')
    nifty_val = soup.find_all('div', {'class' : 'stickymcont'})
    nifty_val = nifty_val[0]
    nifty_val = nifty_val.find_all('div')[0:2]
    nifty_val = nifty_val[1].get_text()
    return nifty_val

def get_sensex_data_from_weblink():
    sensex_url = "https://www.moneycontrol.com/indian-indices/sensex-4.html"
    page = urlopen(sensex_url)
    soup =  BeautifulSoup(page, 'html.parser')
    sensex_val = soup.find_all('div', {'class' : 'stickymcont'})
    sensex_val = sensex_val[0]
    sensex_val = sensex_val.find_all('div')[0:2]
    sensex_val = sensex_val[1].get_text()
    return sensex_val

def get_sensex_nifty_data():
    data_list = []
    nifty_val = get_nifty_data_from_weblink()
    sensex_val = get_sensex_data_from_weblink()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")

    data_list.append(nifty_val)
    data_list.append(current_time)
    data_list.append(sensex_val)
    data_list.append(current_time)

    return data_list


current_nifty_data = "0"
current_sensex_data = "0"

def update_data():
    global current_sensex_data, current_nifty_data
    data = get_sensex_nifty_data()
    print(data[0], current_nifty_data, data[2], current_sensex_data)
    if not (data[0] == current_nifty_data and data[2] == current_sensex_data):
        current_nifty_data = data[0]
        current_sensex_data = data[2]

        tree.insert('', tk.END, values=data)
        for column in tree['column']:
            tree.column(column, anchor="center")
    mainWindow.after(5000, update_data)

columns = ('Nifty', 'Nifty_Time', 'Sensex', 'Sensex_Time')
tree = ttk.Treeview(mainWindow, columns=columns, show='headings')
tree.heading('Nifty', text='Nifty')
tree.heading('Nifty_Time', text='Nifty Time')
tree.heading('Sensex', text='Sensex')
tree.heading('Sensex_Time', text='Sensex Time')
tree.place(x=10, y=10)

update_data()

mainWindow.geometry("825x255")
mainWindow.resizable(False, False)
mainWindow.mainloop()