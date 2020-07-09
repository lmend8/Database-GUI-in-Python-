import backendDB as BDB
import tkinter as tk
from tkinter import *
from tkinter import ttk


## UI INTERFACE using tkinter


win = Tk()
win.title("Database GUI")
win.geometry("800x600")

frm = Frame(win)
frm.pack(side=tk.TOP, padx=20)


btn = Button(frm ,text="Show",command = BDB.bulk_players("players.csv"))
btn.pack(side = tk.BOTTOM, padx =100 )


tv = ttk.Treeview(frm, columns=(1,2,3), )
tv.pack()

##for i in rows:

##submit_button = Button(win, text = "Insert new data record to the database", command = submit)
##submit_button.grid(row = 100, column = 20, columnspan = 20, ipadx = 100)



win.mainloop()