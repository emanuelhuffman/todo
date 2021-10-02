from tkinter import *
from tkinter import messagebox
from datetime import date
from os import walk
import pickle

#global vars
todayDat = str(date.today()) + ".dat"

#-----Core-----
ws = Tk()
ws.title('Food List')
ws.config(bg='#223441')
ws.resizable(width=False, height=False)

lbFrame = Frame(ws)
lbFrame.pack(pady=(10, 0), padx=(10, 10), side=TOP, fill=X, expand=False)
lbFrame.config(bg='#223441')

frame = Frame(lbFrame)
frame.pack(side=LEFT, fill=Y, expand=False)

frame2 = Frame(lbFrame)
frame2.pack(side=RIGHT, fill=Y, expand=False, padx=10)

utilityFrame = Frame(ws)
utilityFrame.pack(pady=(10, 0), padx=(10, 10), side=LEFT, fill=BOTH, expand=False)
utilityFrame.config(bg='#223441')

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
lb.pack(fill=None, expand=False, side=LEFT)

sb = Scrollbar(frame)
sb.pack(side=LEFT, fill=BOTH)

lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)

dateLb = Listbox(
    frame2,
    width=20,
    height=8,
    font=('Times', 18),
    bd=0,
    fg='#464646',
    highlightthickness=0,
    selectbackground='#a6a6a6',
    activestyle="none")
dateLb.pack(fill=None, expand=False, side=RIGHT)

sb = Scrollbar(frame2)
sb.pack(side=RIGHT, fill=Y)

dateLb.config(yscrollcommand=sb.set)
sb.config(command=dateLb.yview)

cal_var = StringVar()
calorie_label = Label(utilityFrame, textvariable=cal_var, bg='#223441', fg="white", pady=10)
calorie_label.pack()

my_entry = Entry(
    utilityFrame,
    font=('times', 24),
    width=31
    )

my_entry.pack(pady=(0, 10))

#-----functions-----
def selected_food():
    selection = dateLb.curselection()
    if not selection:
        return str(date.today())
    return dateLb.get(selection)

def loadFoods():
    file = selected_food() + ".dat"
    try:
        foods = pickle.load(open("lists/" + file, "rb"))
    except:
        messagebox.showwarning("warning", "No file to load.")
    lb.delete(0, "end")
    for food in foods:
        lb.insert("end", food)
    cal_var.set("Calories: " + str(calcCals()))

def saveFoods():
    #save food list
    foods = lb.get(0, lb.size())
    pickle.dump(foods, open("lists/" + todayDat, "wb"))

    #reload dates
    loadDates()
    
def loadDates():
    dateLb.delete(0, "end")
    fileList = []
    for (dirpath, dirnames, filenames) in walk("lists/"):
        fileList.extend(filenames)
    for fileName in reversed(fileList):
        dateLb.insert(END, fileName[0:-4])
    
def newTask(event=None):
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, END)
        cal_var.set("Calories: " + str(calcCals()))
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
        try:
            total_calories = total_calories + int(split_task[-1])
        except:
            lb.delete(END)
            messagebox.showwarning("Error", "Incorrect format. Try: <food> - <calories>. (i.e. smoothie - 300)")
    return total_calories

#-----buttons-----
top_button_frame = Frame(utilityFrame)
top_button_frame.pack()
bottom_button_frame = Frame(utilityFrame)
bottom_button_frame.pack(pady=(0, 10))

addFood_btn = Button(
    top_button_frame,
    text=' Add Food',
    font=('times 14'),
    bg='#c5f776',
    padx=75,
    command=newTask,
)
addFood_btn.pack(fill=BOTH, expand=True, side=LEFT)

delFood_btn = Button(
    top_button_frame,
    text='Delete Food',
    font=('times 14'),
    bg='#ff8b61',
    padx=75,
    command=deleteTask
)
delFood_btn.pack(fill=BOTH, expand=True, side=LEFT)

saveFood_btn = Button(
    bottom_button_frame,
    text='Save Food',
    font=('times 14'),
    bg='#118b61',
    padx=75,
    command=saveFoods
)
saveFood_btn.pack(fill=BOTH, expand=True, side=LEFT)

loadFood_btn = Button(
    bottom_button_frame,
    text='  Load Food',
    font=('times 14'),
    bg='#ff8b02',
    padx=75,
    command=loadFoods
)
loadFood_btn.pack(fill=BOTH, expand=True, side=LEFT)

#load dates
loadDates()

#-----Main Loop-----
ws.mainloop()