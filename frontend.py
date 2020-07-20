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
list1.place(x=60, y=340)


options = [
    "players",
    "games",
    "teams",
    "play"
]


playersColumns = [
    "PlayerID",
    "FirstName",
    "LastName",
    "TeamID",
    "Position", 
    "Touchdown",
    "TotalYards",
    "Salary"
]

teamsColumns = [
    "TeamID",
    "TeamName",
    "City",
]

gamesColumns = [
    "GameID",
    "Dates",
    "Stadium",
    "Result",
    "Attendance", 
    "TicketRevenue"
]

playColumns = [
    "PlayerID",
    "GameID"
]





clicked = StringVar()
drop = OptionMenu(win,clicked, *options)
clicked.set(options[0])
drop.place(x=210, y=100)


##for columns
clicked2 = StringVar()
"""
drop2 = OptionMenu(win,clicked2,*playersColumns)
drop2.place(x=250, y=150)
"""

##input boxes
table_name = Label(win, text="Please Select Table name: ")
table_name.place(x=70, y=100)

##choose column name
column_name = Label(win, text="Select column name to find max: ")
column_name.place(x=70, y=150)


def refreshColumns ():
    name = clicked.get()
    if(name == "players"):
        drop2 = OptionMenu(win,clicked2,*playersColumns)
        clicked2.set(playersColumns[0])
        drop2.place(x=250, y=150)
    elif(name =="games" ):
        drop2 = OptionMenu(win,clicked2,*gamesColumns)
        clicked2.set(gamesColumns[0])
        drop2.place(x=250,y=150)
    elif(name == "play"):
        drop2 = OptionMenu(win,clicked2,*playColumns)
        clicked2.set(playColumns[0])
        drop2.place(x=250,y=150)
    elif(name == "teams"):
        drop2 = OptionMenu(win,clicked2,*teamsColumns)
        clicked2.set(teamsColumns[0])
        drop2.place(x=250,y=150)



def getTable():
    list1.delete(0,END)
    name = clicked.get()
    rows = BDB.get_table(name)
    for i in rows: 
            list1.insert(list1.size()+1,i)


def deleteTable():
    list1.delete(0,END)
    name = clicked.get()
    BDB.delete_table(name)
    display = "Table has been deleted"
    list1.insert(0,display)

def getMax():
    list1.delete(0,END)
    name = clicked.get()
    max = BDB.retrieve_max(clicked2.get(),name)
    list1.insert(0,max)

 
def insertSingleRow():
    list1.delete(0,END)
    filename = clicked.get()+".csv"
    BDB.insertSingle(filename)
    display = "Data has been inserted using INSERT INTO"
    list1.insert(0,display)

def loadData():
    list1.delete(0,END)
    filename = clicked.get()+".csv"
    BDB.bulk_data(filename)
    display = "Data has been inserted using LOAD DATA"
    list1.insert(0,display)
    
def multipleRow():
    list1.delete(0,END)
    filename = clicked.get()+".csv"
    BDB.multi_row_table(filename)
    display = "Data has been inserted using MULTIPLE ROWS"
    list1.insert(0,display)


## Buttons for GUI 
showBtn= Button(win ,text="Retrive All", command=getTable)
showBtn.place(x =60, y=280)

singleBtn = Button(win,text ="Single Insert", command=insertSingleRow)
singleBtn.place(x =140, y=280)

multipleBtn = Button(win,text ="Multiple-row")
multipleBtn.place(x =220, y=280)

deleteBtn = Button(win,text ="Delete table", command=deleteTable)
deleteBtn.place(x =320, y=280)

loadBtn = Button(win,text ="Load Data", command=loadData)
loadBtn.place(x =410, y=280)

maxBtn = Button(win,text ="Max Value", command=getMax)
maxBtn.place(x =490, y=280)

refreshBtn = Button(win,text="Show/Refresh Column", command=refreshColumns)
refreshBtn.place(x =350, y=150)





win.mainloop()