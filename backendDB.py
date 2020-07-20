
import mysql.connector as sqlconn
import csv 
import pandas as pd
import random 
from random import randint
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
    


def multi_row_table(filename):
    mydb = sqlconn.connect(user = 'root', 
                        password = os.getenv('DB_PASSWORD'), 
                        host = '127.0.0.1', 
                        database = "nfl_schema")
    cursor = mydb.cursor()
    df = pd.read_csv(filename, sep=',', header=None)
    cols = str(df.columns.values.tolist()).replace('[','').replace(']', '')
    values = list(map(tuple, df.values))
    half = len(values) // 2
    valuesA = values[:half]
    valuesB = values[half:]
    
    query = "INSERT INTO games (GameID, Dates, Stadium, Result, Attendance, TicketRevenue) VALUES (%s, %s, %s, %s, %s, %s);"
    cursor.executemany(sql, valuesA)
    mydb.commit()
    cursor.executemany(sql, valuesB)
    mydb.commit()
    mydb.close()
    
    
    
def bulk_data(filename):
    mydb = sqlconn.connect(user='root', 
                        password = os.getenv('DB_PASSWORD'), 
                        host='127.0.0.1', 
                        database='nfl_schema', 
                        allow_local_infile=True)
    mycursor = mydb.cursor()
    if(filename == "players.csv"):
        query = "LOAD DATA LOCAL INFILE \'%s\' INTO TABLE players FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\\r\\n' (PlayerID, FirstName, LastName,TeamID, Position, Touchdowns, TotalYards, Salary)" % (filename)
    elif(filename == "games.csv"):
        query = "LOAD DATA LOCAL INFILE \'%s\' INTO TABLE games FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\\r\\n' (GameID,Dates,Stadium,Result,Attendance,TicketRevenue)" % (filename)
    elif(filename == "play.csv"):
        query = "LOAD DATA LOCAL INFILE \'%s\' INTO TABLE play FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\\r\\n' (PlayerID,GameID) " % (filename)
    elif(filename == "teams.csv"):
        query = "LOAD DATA LOCAL INFILE \'%s\' INTO TABLE teams FIELDS TERMINATED BY ',' ENCLOSED BY '\"' LINES TERMINATED BY '\\r\\n' (TeamID,TeamName,City) " % (filename)
    mycursor.execute(query)
    
    mydb.commit()
    mydb.close()
  

def generatePlayersData(numberOfRows, output_filename):
    setID=set()
    rows=[]
    with open(output_filename, mode='w', newline='') as player_file:
        writer = csv.writer(player_file, delimiter=',')
        
        TeamIDs = [11,13,17,23,27]
        NFL_Teams = ["Patriots", "Broncos", "Cowboys", "Eagles", "GreenBay"]
        
        for _ in range(numberOfRows):
            PlayerID = randint(1, 1000000000)
            TeamID = random.choice(TeamIDs)
            while(PlayerID in setID):
                PlayerID = randint(1, 1000000000)
                TeamID = random.choice(TeamIDs)
            setID.add(PlayerID)
            FirstName = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5, 10))
            LastName = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5, 10))
            Team_name = random.choice(NFL_Teams)
            Position = random.choice(('QB','RB','WR'))
            Touchdowns = randint(1,1000)
            Total_Yards = randint(1, 1000000)
            Salary = randint(1000, 3000000)
            
            rows.append([PlayerID, TeamID, FirstName, LastName, Position, Touchdowns, Total_Yards, Salary])
        writer.writerows(rows)
    print("%s generated" % (output_filename))



generatePlayersData(10000,"players10000.csv")
generatePlayersData(100000,"players100000.csv")
generatePlayersData(1000000,"players1000000.csv")