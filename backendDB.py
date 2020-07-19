
import mysql.connector as sqlconn
import csv 
import pandas as pd
import dotenv
import os


dotenv.load_dotenv()

## GLOBAL VARIABLES

def insertSingle(filename):
    dataDB = []
    with open(filename) as f:   
        read = csv.reader(f, delimiter=',')
        for row in read:
            dataDB.append(tuple(row))
        mydb = sqlconn.connect(user = 'root', 
                            password = os.getenv('DB_PASSWORD'), 
                            host = '127.0.0.1', 
                            database = "nfl_schema")
        mycursor = mydb.cursor()
        for row in dataDB:
            if(filename == "players.csv"):                   
                query = "INSERT INTO players(PlayerID,FirstName,LastName,TeamID,Position,Touchdowns,TotalYards,Salary) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"
            elif(filename == "teams.csv"):
                query = "INSERT INTO teams(TeamID,TeamName,City) VALUES (%s,%s,%s)"
            elif(filename =="play.csv"):
                query = "INSERT INTO play(PlayerID,GameID) VALUES (%s,%s)"
            elif(filename == "games.csv"):
                query = "INSERT INTO games(GameID,Dates,Stadium,Result,Attendance,TicketRevenue) VALUES (%s,%s,%s,%s,%s,%s)"
            mycursor.execute(query,row)
        mydb.commit()
        mydb.close()


def get_table(name):
    mydb = sqlconn.connect(user = 'root', 
                       password = os.getenv('DB_PASSWORD'), 
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
                        password = os.getenv('DB_PASSWORD'), 
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
                        password = os.getenv('DB_PASSWORD'), 
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
                        password = os.getenv('DB_PASSWORD'), 
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
    
    
    
def bulk_data(filename):
    mydb = sqlconn.connect(user='root', 
                        password = os.getenv('DB_PASSWORD'), 
                        host='127.0.0.1', 
                        database='nfl_schema', 
                        auth_plugin='mysql_native_password',
                        allow_local_infile=True)
    mycursor = mydb.cursor()
    query = "LOAD DATA LOCAL INFILE \'%s\' INTO TABLE players FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\\r\\n' (PlayerID, FirstName, LastName,TeamID, Position, Touchdowns, TotalYards, Salary)" % (filename)
    mycursor.execute(query)
    
    mydb.commit()
    mydb.close()
  