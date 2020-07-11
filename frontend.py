import backendDB as BDB
import tkinter as tk
from tkinter import *
from tkinter import ttk


## UI INTERFACE using tkinter
win = Tk()
win.title("Database GUI")
win.geometry("800x600")

## frame to show the database 
list1 = Listbox(win,width=100, height=14)
list1.place(x=70, y=340)



##input boxes
table_name = Label(win, text="Please Enter Table name: ")
table_name.place(x=70, y=100)
table_input = Entry(win)
table_input.place(x=210, y=100)


def getName():
    name = table_input.get()
    if(name == "team"):
        rows = BDB.get_team()
        print(rows)
        list1.insert(list1.size()+1,rows)
        



## Buttons for GUI 
showBtn= Button(win ,text="Show", command=getName)
showBtn.command = BDB.get_team
showBtn.place(x =60, y=280)

singleBtn = Button(win,text ="Insert single", command=getName)
singleBtn.place(x =120, y=280)

multipleBtn = Button(win,text ="Insert Multiple")
multipleBtn.place(x =210, y=280)

singleBtn = Button(win,text ="Insert single")
singleBtn.place(x =320, y=280)

loadBtn = Button(win,text ="Load Data")
loadBtn.place(x =410, y=280)

maxBtn = Button(win,text ="Max Value")
maxBtn.place(x =490, y=280)







##for i in rows:

##submit_button = Button(win, text = "Insert new data record to the database", command = submit)
##submit_button.grid(row = 100, column = 20, columnspan = 20, ipadx = 100)



win.mainloop()