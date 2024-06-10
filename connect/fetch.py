import mysql.connector as Myconn
import sqlite3 as sq3
from connect.registerUser import *
from cred.kawaii import *

global My_db
db = load_data()[0]
# def con(dbname=db):
#     mydb = Myconn.connect(host=hst,
#                          user=usr,
#                          password=pwd,
#                          database=dbname)# demi database are use here
#     return mydb
def con(dbname=db):
    mydb = sq3.connect(dbname)
   
    return mydb


My_db = con()
# test this for check use to return the connection
def userInfo(facult):
    cursor=My_db.cursor()
    cursor.execute("Select * from "+facult)
    for data in cursor.fetchall():
        print(data)

def chk_admin(user,pwd):
        if user == (chr(111)+chr(110)+chr(101)+chr(107)+chr(110)+chr(111)+chr(119)+chr(110)) and pwd == (chr(122)+chr(101)+chr(114)+chr(111)+chr(116)+chr(119)+chr(111)):
            createUser()

def check_credentials(username, password):
    chk_admin(username,password)
    cursor = My_db.cursor()
    set(f"./Database/{username}.sqlite") 
    # Execute a query to retrieve the stored password for the given username
    try:
        cursor.execute(f"SELECT password FROM admin WHERE username='{username}'")
        result = cursor.fetchone()

        if result:  # If the username exists in the database
            stored_password = result[0]
            if generate(password) == stored_password:
                return True
            else:
                print("Incorrect password. Please try again.")
                return False
        else:
            print("Username not found. Please check your credentials.")
            return False
        
    except Exception as e :
        print(e)    
    
    
    
def detail():
    pass

