import mysql.connector

dataBase = mysql.connector.connect(
					host = "localhost",
					user = "root",
					passwd = "password",
					database = "STUDENT_INFO" )

cursorObject = dataBase.cursor()


studentRecord = """CREATE TABLE STUDENT (
				NAME VARCHAR(20) NOT NULL,
				BRANCH VARCHAR(50),
				ROLL INT NOT NULL,
				SECTION VARCHAR(5),
				AGE INT
				)"""

cursorObject.execute(studentRecord)

dataBase.close()

import mysql.connector
import tkinter as tk
from tkinter import simpledialog

mydb = mysql.connector.connect(
host = "localhost",
user = "root",
password = "password",
database = "STUDENT_INFO"
)

mycursor = mydb.cursor()

print("Enter number of students you want to enter details for : ")
n = int(input())
i = 0
while i < n:
    ROOT = tk.Tk()

    ROOT.withdraw()
# the input dialog
    name = simpledialog.askstring(title="Test",prompt="Student Name?:")
    roll= simpledialog.askstring(title="Test",prompt="Student roll number?:")
    
    

    sql = "INSERT INTO STUDENT (Name, ROLL)VALUES (%s, %s)"
    val = (name,roll)
  
    mycursor.execute(sql, val)
    mydb.commit()
  
    print(mycursor.rowcount, "details inserted")
    i = i + 1
mydb.close()
