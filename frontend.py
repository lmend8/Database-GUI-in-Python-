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



##Data for dropdowns
file = [
    "players10000",
    "players100000",
    "players1000000",
    "players",
    "games",
    "play",
    "teams"
]
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

#dropmenu for files
fileClicked = StringVar()
filedrop = OptionMenu(win, fileClicked, *file)
fileClicked.set(file[0])
filedrop.place(x=210,y=50)

#dropmenu for tables
clicked = StringVar()
drop = OptionMenu(win,clicked, *options)
clicked.set(options[0])
drop.place(x=210, y=100)


##for columns
clicked2 = StringVar()


file_name = Label(win, text="Please Select file name: ")
file_name.place(x=70, y=50)

introFile = Label(win,text="(NOTE:Use the correct file for the corresponding table e.g. file games = games table)")
introFile.place(x=345, y=50)


##input boxes
table_name = Label(win, text="Please Select Table name: ")
table_name.place(x=70, y=100)

##choose column name
column_name = Label(win, text="Select column name to find max: ")
column_name.place(x=70, y=150)

#method to show the columns of tables
def refreshColumns ():
    name = clicked.get()
    if(name == "players" or name == "players10000" or name == "players100000" or name == "players1000000"):
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


# retrive all
def getTable():
    list1.delete(0,END)
    name = clicked.get()
    rows = BDB.get_table(name)
    for i in rows: 
            list1.insert(list1.size()+1,i)

#delete
def deleteTable():
    list1.delete(0,END)
    name = clicked.get()
    BDB.delete_table(name)
    display = "Table has been deleted"
    list1.insert(0,display)

#get max of the column specify
def getMax():
    list1.delete(0,END)
    name = clicked.get()
    max = BDB.retrieve_max(clicked2.get(),name)
    list1.insert(0,max)

#INSERT INTO technique
def insertSingleRow():
    list1.delete(0,END)
    filename = fileClicked.get()+".csv"
    query = BDB.insertSingle(filename)
    list1.insert(0,query)

#LOAD DATA technique
def loadData():
    list1.delete(0,END)
    filename = fileClicked.get()+".csv"
    query = BDB.bulk_data(filename)
    list1.insert(0,query)
#MULIT ROW tehnique 
def multipleRow():
    list1.delete(0,END)
    filename = fileClicked.get()+".csv"
    query = BDB.multi_row_table(filename)
    list1.insert(0,query)


## Buttons for GUI 
showBtn= Button(win ,text="Retrive All", command=getTable)
showBtn.place(x =60, y=280)

singleBtn = Button(win,text ="Single Insert", command=insertSingleRow)
singleBtn.place(x =140, y=280)

multipleBtn = Button(win,text ="Multiple-row", command=multipleRow)
multipleBtn.place(x =220, y=280)

deleteBtn = Button(win,text ="Delete table", command=deleteTable)
deleteBtn.place(x =320, y=280)

loadBtn = Button(win,text ="Load Data", command=loadData)
loadBtn.place(x =410, y=280)

maxBtn = Button(win,text ="Max Value", command=getMax)
maxBtn.place(x =490, y=280)

refreshBtn = Button(win,text="Show/Refresh Column", command=refreshColumns)
refreshBtn.place(x =350, y=150)


#loop to run the program
win.mainloop()