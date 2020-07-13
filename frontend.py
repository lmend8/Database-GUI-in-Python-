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

column_name = Label(win, text="Enter column name to find max: ")
column_name.place(x=70, y=150)
column_input = Entry(win)
column_input.place(x=250, y=150)


def getTable():
    list1.delete(0,END)
    name = table_input.get()
    rows = BDB.get_table(name)
    for i in rows: 
            list1.insert(list1.size()+1,i)
    table_input.delete(0,END)


def deleteTable():
    name = table_input.get()
    BDB.delete_table(name)

def getMax():
    list1.delete(0,END)
    name = table_input.get()
    column = column_input.get()
    max = BDB.retrieve_max(column,name)
    list1.insert(0,max)
    table_input.delete(0,END)
    column_input.delete(0,END)

        



## Buttons for GUI 
showBtn= Button(win ,text="Show", command=getTable)
showBtn.place(x =60, y=280)

singleBtn = Button(win,text ="Insert single")
singleBtn.place(x =120, y=280)

multipleBtn = Button(win,text ="Insert Multiple")
multipleBtn.place(x =210, y=280)

deleteBtn = Button(win,text ="Delete table", command=deleteTable)
deleteBtn.place(x =320, y=280)

loadBtn = Button(win,text ="Load Data")
loadBtn.place(x =410, y=280)

maxBtn = Button(win,text ="Max Value", command=getMax)
maxBtn.place(x =490, y=280)







##for i in rows:

##submit_button = Button(win, text = "Insert new data record to the database", command = submit)
##submit_button.grid(row = 100, column = 20, columnspan = 20, ipadx = 100)



win.mainloop()