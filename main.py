from tkinter import *
from tkinter import messagebox
import pickle

task_list = []

def loadTasks():
    tasks = pickle.load(open("tasks.dat", "rb"))
    lb.delete(0, "end")
    for task in tasks:
        lb.insert("end", task)

def saveTasks():
    tasks = lb.get(0, lb.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter some task.")

def deleteTask():
    lb.delete(ANCHOR)

ws = Tk()
#ws.geometry('500x450+500+200')
ws.title('Todo')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack()

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none",)

lb.pack(side=LEFT, fill=BOTH)

for item in task_list:
    lb.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

my_entry = Entry(
    ws,
    font=('times', 24)
    )

my_entry.pack(pady=10, padx=10)

button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('times 14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

saveTasks_btn = Button(
    button_frame,
    text='Save Tasks',
    font=('times 14'),
    bg='#118b61',
    padx=20,
    pady=10,
    command=saveTasks
)
saveTasks_btn.pack(fill=BOTH, expand=True, side=LEFT)

loadTasks_btn = Button(
    button_frame,
    text='Load Tasks',
    font=('times 14'),
    bg='#ff8b02',
    padx=20,
    pady=10,
    command=loadTasks
)
loadTasks_btn.pack(fill=BOTH, expand=True, side=LEFT)

ws.mainloop()