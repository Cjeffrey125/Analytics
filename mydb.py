import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'AdminAnalytic01'   
    )

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE Iskolar_ng_Bayan")

#just create a database to the pc if there is no db  \(0_0)/
#run it by typing in the terminal python mydb.py 
