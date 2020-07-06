import tkinter as tk
import mysql.connector as sqlconn
from mysql.connector import (connection)
from tkinter import *




def submit():
    db = connection.MySQLConnection(user = 'root', 
                        password = 'bodom987',
                        port = 3306,
                        host = '127.0.0.1', 
                        database = 'my database')
    
    sql = "INSERT INTO passengers (PassID, FirstName, LastName, Birthdate, Address, Email, PhoneNumber, Citizenship, Gender) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    db.close()

win = Tk()
win.title("Database GUI")
win.geometry("700x500")

teamID = Label(win, text = "Title")
teamID.grid(row = 0, column = 0, padx = 20)
teamName = Label(win, text = "Title")
teamName.grid(row = 1, column = 0, padx = 20)
cityName = Label(win, text = "Title")
cityName.grid(row = 2, column = 0, padx = 20)



submit_button = Button(win, text = "Insert new data record to the database", command = submit)
submit_button.grid(row = 4, column = 0, columnspan = 2, ipadx = 100)



win.mainloop()