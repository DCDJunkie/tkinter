from tkinter import StringVar, Label, Scale
import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("Color Picker")

color_hex_code = StringVar()
red_percentage_value = StringVar()
green_percentage_value = StringVar()
blue_percentage_value = StringVar()

result_label = Label(mainWindow, padx=5, pady=5, textvariable=color_hex_code,
                     fg="white",
                     font=("arial", 43))

color_hex_code.set("#000")
result_label.config(bg=color_hex_code.get())
result_label.place(x=5,y=5, width=490, height=280)

def get_str_from_num(value):
    color_data = {}
    color_val = str(hex(int(value))).split("x")[1]
    if len(color_val) < 2:
        color_val = "0" + color_val

    percentage_value = "0 %"
    color_percent_value = int(value)
    if color_percent_value > 0:
        color_percent_value = str(int((float(color_percent_value) * 100)/255))
        if len(color_percent_value) < 2:
            color_percent_value = "0" + color_percent_value
        percentage_value = color_percent_value + " %"

    color_data['hex'] = color_val.upper()
    color_data['percentage'] = percentage_value
    return color_data

def get_hex_color_value():
    color_info_dict = {}

    red_value = get_str_from_num(scroller_red.get())
    green_value = get_str_from_num(scroller_green.get())
    blue_value = get_str_from_num(scroller_blue.get())

    color_info_dict['red_hex'] = red_value['hex']
    color_info_dict['red_percentage'] = red_value['percentage']

    color_info_dict['green_hex'] = green_value['hex']
    color_info_dict['green_percentage'] = green_value['percentage']

    color_info_dict['blue_hex'] = blue_value['hex']
    color_info_dict['blue_percentage'] = blue_value['percentage']

    return color_info_dict

def update_values():
    color_values = get_hex_color_value()

    color_hex_value = "#" + color_values['red_hex'] + color_values['green_hex'] + color_values['blue_hex']
    color_hex_code.set(color_hex_value)
    result_label.config(bg=color_hex_code.get())

    red_percentage_value.set(color_values['red_percentage'])
    green_percentage_value.set(color_values['green_percentage'])
    blue_percentage_value.set(color_values['blue_percentage'])

def scroller_red_handler(value):
    update_values()

def scroller_green_handler(value):
    update_values()

def scroller_blue_handler(value):
    update_values()

scroller_red = Scale(mainWindow, from_=0, to=255, command=scroller_red_handler)
scroller_red.config(length="447", orient="horizontal", troughcolor="red", fg="red")
scroller_red.set(0)
scroller_red.place(x=0, y=300)

red_label = Label(mainWindow,textvariable=red_percentage_value, fg="red")
red_percentage_value.set("0 %")
red_label.place(x=455, y=319)

scroller_green = Scale(mainWindow, from_=0, to=255, command=scroller_green_handler)
scroller_green.config(length="447", orient="horizontal", troughcolor="green",fg="green")
scroller_green.set(0)
scroller_green.place(x=0, y=350)

green_label = Label(mainWindow,textvariable=green_percentage_value, fg="green")
green_percentage_value.set("0 %")
green_label.place(x=455, y=369)

scroller_blue = Scale(mainWindow, from_=0, to=255, command=scroller_blue_handler)
scroller_blue.config(length="447", orient="horizontal", troughcolor="blue", fg="blue")
scroller_blue.set(0)
scroller_blue.place(x=0, y=400)

blue_label = Label(mainWindow,textvariable=blue_percentage_value, fg="blue")
blue_percentage_value.set("0 %")
blue_label.place(x=455, y=419)

mainWindow.geometry("500x475")
mainWindow.resizable(False, False)
mainWindow.mainloop()