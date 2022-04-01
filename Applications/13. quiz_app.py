from tkinter import StringVar, Label, Button, Radiobutton
import tkinter as tk
import pandas as pd
import random

ans_btn_positions = [[10, 120],[10, 170],[10, 220],[10, 270]]

mainWindow = tk.Tk()
mainWindow.title("Quiz App")

question_str = StringVar()
question_label = Label(mainWindow,
                       textvariable=question_str,
                       relief="raised",
                       font=(None, 18))
question_label.place(x=10, y=50, width=653, height=50)

score_count = 0
score_str = StringVar()
score_label = Label(mainWindow,
                       textvariable=score_str,
                       relief="raised",
                       font=(None, 18),
                        state="disabled")
score_label.place(x=670, y=50, width=170, height=50)
score_str.set("SCORE: 0%")
user_selected_ans = {}

answer_select_str = StringVar()
correct_ans_data = []
df = pd.read_csv('Resources/csv_files/quiz_app_data.csv')
total_no_of_question = len(df.index)
current_question_index = 0

data = list(df.iloc[current_question_index])
question_str.set(data[0])
correct_ans_data.append(data[1])

radio_btn_obj = []
for index in range(4):
    r = Radiobutton(mainWindow, text=data[index+1], value=data[index+1], variable=answer_select_str)
    r.config(indicatoron=0, width=46,
             relief="raised",
             font=(None, 18))
    btn_cordinate = ans_btn_positions.pop(random.randrange(len(ans_btn_positions)))
    r.place(x=btn_cordinate[0], y=btn_cordinate[1])
    radio_btn_obj.append(r)
ans_btn_positions = [[10, 120],[10, 170],[10, 220],[10, 270]]

answer_select_str.set("None")

def question_changed_handler():
    data = list(df.iloc[current_question_index])
    question_str.set(data[0])
    if data[1] not in correct_ans_data:
        correct_ans_data.append(data[1])

    for index in range(4):
        radio_btn_obj[index].config(text=data[index + 1], value=data[index + 1])
        btn_cordinate = ans_btn_positions.pop(random.randrange(len(ans_btn_positions)))
        radio_btn_obj[index].place(x=btn_cordinate[0], y=btn_cordinate[1])

        if str(current_question_index) in list(user_selected_ans.keys()):
            radio_btn_obj[index].config(state="disabled")
            lock_ans_btn.config(state="disabled")
            answer_select_str.set(user_selected_ans[str(current_question_index)])
        else:
            radio_btn_obj[index].config(state="normal")
            lock_ans_btn.config(state="normal")
            answer_select_str.set("None")
    if score_str.get() != 'SCORE: 0%':
        ans_desc_str.set("Correct Answer : " + correct_ans_data[current_question_index])

def prev_btn_handler():
    global current_question_index, ans_btn_positions, user_selected_ans, correct_ans_data
    if (current_question_index != 0):
        current_question_index -= 1
        question_changed_handler()
    ans_btn_positions = [[10, 120], [10, 170], [10, 220], [10, 270]]

prev_question_btn = Button(mainWindow,
                           text="PREVIOUS",
                           height=1,
                           font=(None,18),
                           command=prev_btn_handler)
prev_question_btn.place(x=10, y=323, width=210)

def lock_ans_btn_handler():
    global current_question_index
    selected_ans = answer_select_str.get()
    if selected_ans and selected_ans != 'None':
        for btn in range(4):
            radio_btn_obj[btn].config(state="disabled")
        user_selected_ans[str(current_question_index)] = answer_select_str.get()
        lock_ans_btn.config(state="disabled")

    if len(user_selected_ans) == total_no_of_question:
        submit_btn.config(state="normal")

lock_ans_btn = Button(mainWindow,
                           text="LOCK",
                           height=1,
                           font=(None,18),
                           command=lock_ans_btn_handler)
lock_ans_btn.place(x=232, y=323, width=210)

def next_btn_handler():
    global current_question_index, ans_btn_positions, user_selected_ans, correct_ans_data
    if not(current_question_index >= total_no_of_question-1):
        current_question_index += 1
        question_changed_handler()
    ans_btn_positions = [[10, 120], [10, 170], [10, 220], [10, 270]]

next_question_btn = Button(mainWindow,
                           text="NEXT",
                           height=1,
                           font=(None,18),
                           command=next_btn_handler)
next_question_btn.place(x=453, y=323, width=210)

def submit_btn_handler():
    ans_count = 0
    for ans in list(user_selected_ans.values()):
        if ans in correct_ans_data:
            ans_count += 1

    scored_percentage = int((ans_count * 100)/total_no_of_question)
    score_str.set("SCORE: " + str(scored_percentage) + "%")
    ans_desc_str.set("Correct Answer : " + correct_ans_data[current_question_index])

submit_btn = Button(mainWindow,
                           text="SUBMIT",
                           font=(None,22),
                           command=submit_btn_handler)

submit_btn.place(x=670, y=170, height=90, width=170)
submit_btn.config(state="disabled")

ans_desc_str = StringVar()
ans_descr_label = Label(mainWindow,
                        textvariable=ans_desc_str,
                        font=(None, 16))
ans_descr_label.config(relief="raised")
ans_descr_label.place(x=10, y=380, width=652, height=40)

mainWindow.config(relief="raised",
                  borderwidth=2)
mainWindow.geometry("860x470")
mainWindow.mainloop()