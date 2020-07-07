
import mysql.connector as sqlconn
import csv 




def submit():
    mydb = sqlconn.connect(user = 'root', 
                        password = 'bodom987', 
                        host = '127.0.0.1', 
                        database = "nfl_schema")
    
    
    """
    sql = "INSERT INTO passengers (PassID, FirstName, LastName, Birthdate, Address, Email, PhoneNumber, RewardPoints, Citizenship, Gender) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data_sql = (492662290, 'Cloud', 'strife', '1981-6-19', '7830 State Street Saint Charles IL 60174', 'Dewitt@gmail.com', '9158226642', 3643, 'Mexico', 'f')
    
    cursor.execute("show databases")
    
    for i in mycursor:
        print(i)
    
    """
    cursor = mydb.cursor()
    cursor.execute(sql, data_sql)
    mydb.commit()
    mydb.close()


def get_team():
    mydb = sqlconn.connect(user = 'root', 
                        password = 'bodom987', 
                        host = '127.0.0.1', 
                        database = "nfl_schema")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM teams")
    rows = mycursor.fetchall()
    for i in rows:
        print(i)
    mydb.close()


def get_play():
    mydb = sqlconn.connect(user = 'root', 
                        password = 'bodom987', 
                        host = '127.0.0.1', 
                        database = "nfl_schema")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM play")
    rows = mycursor.fetchall()
    for i in rows:
        print(i)
    mydb.close()
    
    
def get_players():
    mydb = sqlconn.connect(user = 'root', 
                        password = 'bodom987', 
                        host = '127.0.0.1', 
                        database = "nfl_schema")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM players")
    rows = mycursor.fetchall()
    for i in rows:
        print(i)
    mydb.close()

def get_players():
    mydb = sqlconn.connect(user = 'root', 
                        password = 'bodom987', 
                        host = '127.0.0.1', 
                        database = "nfl_schema")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM players")
    rows = mycursor.fetchall()
    for i in rows:
        print(i)
    mydb.close()


def get_games():
    mydb = sqlconn.connect(user = 'root', 
                        password = 'bodom987', 
                        host = '127.0.0.1', 
                        database = "nfl_schema")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM games")
    rows = mycursor.fetchall()
    for i in rows:
        print(i)
    mydb.close()
