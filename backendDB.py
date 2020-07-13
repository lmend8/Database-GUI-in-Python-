
import mysql.connector as sqlconn
import csv 
import pandas as pd




## GLOBAL VARIABLES

filename = open("players.csv")
tablename = ""

def insertSingle():
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


def get_table(name):
    mydb = sqlconn.connect(user = 'root', 
                        password = 'bodom987', 
                        host = '127.0.0.1', 
                        database = "nfl_schema")
    mycursor = mydb.cursor()
    query = "SELECT * FROM "+name
    mycursor.execute(query)
    rows = mycursor.fetchall()
    for i in rows:
        print(i)
    return rows
    mydb.close()



def delete_table(name):
    mydb = sqlconn.connect(user = 'root', 
                        password = 'bodom987', 
                        host = '127.0.0.1', 
                        database = "nfl_schema")
    mycursor = mydb.cursor()
    query = "DELETE FROM " + name
    mycursor.execute(query) 
    mydb.commit()
    mydb.close()
    print("teams table cleared")
    
def retrieve_max(column, table):
    mydb = sqlconn.connect(user = 'root', 
                        password = 'bodom987', 
                        host = '127.0.0.1', 
                        database = "nfl_schema")
    mycursor = mydb.cursor()
    query = "SELECT MAX(" + column + ") FROM " + table
    mycursor.execute(query)
    maxVal = mycursor.fetchall()
    print(maxVal)
    return maxVal
    mydb.close()
    


def multi_row_games(filename='games.csv'):
    mydb = sqlconn.connect(user = 'root', 
                        password = 'bodom987', 
                        host = '127.0.0.1', 
                        database = "nfl_schema")
    cursor = mydb.cursor()
    df = pd.read_csv(file_name, sep=',', header=None)
    cols = str(df.columns.values.tolist()).replace('[','').replace(']', '')
    values = list(map(tuple, df.values))
    half = len(values) // 2
    valuesA = values[:half]
    valuesB = values[half:]
    
    query = "INSERT INTO games (GameID, Date, Stadium, Result, Attendance, TicketRevenue) VALUES (%s, %s, %s, %s, %s, %s);"
    try:
        cursor.executemany(sql, valuesA)
    except sqlcon.Error as e:
        return e.msg
    mydb.commit()
    try:
        cursor.executemany(sql, valuesB)
    except sqlcon.Error as e:
        return e.msg
    mydb.commit()
    mydb.close()
    
    
    
def bulk_players(filename='players.csv'):
    mydb = sqlconn.connect(user='root', 
                        password='bodom987', 
                        host='127.0.0.1', 
                        database='nfl_schema', 
                        auth_plugin='mysql_native_password',
                        allow_local_infile=True)
    mycursor = mydb.cursor()
    query = "LOAD DATA LOCAL INFILE \'%s\' INTO TABLE players FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\\r\\n' (PlayerID, TeamID, FirstName, LastName, Position, Touchdowns, TotalYards, Salary)" % (filename)
    try:
        mycursor.execute(query)
    except sqlconn.Error as e:
        return e.msg
    mydb.commit()
    mydb.close()
  

def multi_row_players(filename='players.csv'):
    df = pd.read_csv(filename, sep=',', header=None)
    cols = str(df.columns.values.tolist()).replace('[','').replace(']', '')
    values = list(map(tuple, df.values))
    half = len(values) // 2
    valuesA = values[:half]
    valuesB = values[half:]
    mydb = sqlconn.connect(user = 'root', 
                        password = 'bodom987', 
                        host = '127.0.0.1', 
                        database = "nfl_schema",
                        auth_plugin='mysql_native_password')
    mycursor = mydb.cursor()    
    query = "INSERT INTO players (PlayerID, TeamID, FirstName, LastName, Position, Touchdowns, TotalYards, Salary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
    try:
        mycursor.executemany(query, valuesA)
    except sqlconn.Error as e:
        return e.msg
    mydb.commit()
    try:
        mycursor.executemany(query, valuesB)
    except sqlconn.Error as e:
        return e.msg
    for i in query:
        print(i)
    mydb.commit()
    mydb.close()