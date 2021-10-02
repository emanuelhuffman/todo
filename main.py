from tkinter import *
from tkinter import messagebox
import pickle

#todo - add new listbox with dates (when saving, adds new item for todays date, if already created, update dat file for that date)

#-----Core-----
ws = Tk()
#ws.geometry('500x450+500+200')
ws.title('Calorie Counter')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

frame = Frame(ws)
frame.pack(pady=(10, 0), padx=(10, 10))

lb = Listbox(
    frame,
    width=40,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none")

lb.pack(side=LEFT, fill=BOTH)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

cal_var = StringVar()
calorie_label = Label(ws, textvariable=cal_var, bg='#223441', fg="white", pady=10)
calorie_label.pack()

my_entry = Entry(
    ws,
    font=('times', 24),
    width=31
    )

my_entry.pack(pady=(0, 10))

#-----functions-----
def loadTasks():
    tasks = pickle.load(open("tasks.dat", "rb"))
    lb.delete(0, "end")
    for task in tasks:
        lb.insert("end", task)
    cal_var.set("Calories: " + str(calcCals()))

def saveTasks():
    tasks = lb.get(0, lb.size())
    pickle.dump(tasks, open("tasks.dat", "wb"))

def newTask(event):
    task = my_entry.get()
    if task != "":
        try:
            lb.insert(END, task)
            my_entry.delete(0, "end")
            cal_var.set("Calories: " + str(calcCals()))
        except:
            lb.delete(END< task)
            messagebox.showwarning("Error", "Incorrect format. Try: <food> - <calories>. (i.e. smoothie - 300)")
    else:
        messagebox.showwarning("warning", "Please enter some task.")
ws.bind_all('<Return>', newTask)

def deleteTask():
    lb.delete(ANCHOR)
    cal_var.set("Calories: " + str(calcCals()))

def calcCals():
    total_calories = 0
    tasks = lb.get(0, lb.size())
    for task in tasks:
        split_task = task.split()
        total_calories = total_calories + int(split_task[-1])
    return total_calories

#-----buttons-----
top_button_frame = Frame(ws)
top_button_frame.pack()
bottom_button_frame = Frame(ws)
bottom_button_frame.pack(pady=(0, 10))

addTask_btn = Button(
    top_button_frame,
    text='Add Task  ',
    font=('times 14'),
    bg='#c5f776',
    padx=75,
    command=newTask,
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    top_button_frame,
    text='Delete Task',
    font=('times 14'),
    bg='#ff8b61',
    padx=75,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

saveTasks_btn = Button(
    bottom_button_frame,
    text='Save Tasks',
    font=('times 14'),
    bg='#118b61',
    padx=75,
    command=saveTasks
)
saveTasks_btn.pack(fill=BOTH, expand=True, side=LEFT)

loadTasks_btn = Button(
    bottom_button_frame,
    text='Load Tasks',
    font=('times 14'),
    bg='#ff8b02',
    padx=75,
    command=loadTasks
)
loadTasks_btn.pack(fill=BOTH, expand=True, side=LEFT)

#-----Main Loop-----

ws.mainloop()