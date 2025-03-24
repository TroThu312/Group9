import subprocess
import os

#check pip is exits
try:
    subprocess.check_output(["pip", "--version"])
    subprocess.call(["pip", "install", "--upgrade", "pip"])
except:
    command  = """curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py"""
    #run command
    subprocess.call(command, shell=True)
    #install pip
    subprocess.call(["python", "get-pip.py"])
    #remove get-pip.py
    os.remove("get-pip.py")
    #update pip
    subprocess.call(["pip", "install", "--upgrade", "pip"])


#install requirements
subprocess.call(["pip", "install", "-r", "requirements.txt"])

from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
import ctypes

#prepare for database
load_dotenv(find_dotenv())
host = os.getenv("HOSTNAME")
client = MongoClient(host)
#Check there was database named Group9 in client
if "Group9" in client.list_database_names():
    print("Database already existed")
    db = client['Group9']
else:
    #create database
    db = client['Group9']
    print("Database created")

#check there was collection named admin in db
def import_admin_data():
    with open("./Data/admin.json", "r") as f:
        data = f.read()

    for element in eval(data):
        #check element is in collection
        if element["Username"] not in db["admin"].find({}).distinct("Username"):
            db["admin"].insert_one(element)
        else:
            continue
    print("Imported admin data successfully")
if "admin" in db.list_collection_names():
    print("Collection admin already existed")
    #import data from ./Data/admin.json
    import_admin_data()

else:
    collection = db.create_collection("admin")
    print("Collection admin created")
    #import data from ./Data/admin.json to collection
    import_admin_data()

#check there was collection named users in db
def import_user_data():
    with open("./Data/users.json", "r") as f:
        data = f.read()

    for element in eval(data):
        #check element is in collection
        if element["Student_Id"] not in db["users"].find({}).distinct("Student_Id"):
            db["users"].insert_one(element)
        else:
            continue
    print("Imported users data successfully")
if "users" in db.list_collection_names():
    print("Collection users already existed")
    #import data from ./Data/users.json
    import_user_data()

else:
    collection = db.create_collection("users")
    print("Collection users created")
    #import data from ./Data/users.json to collection
    import_user_data()

#check there was collection named warehouse in db
def import_books_data():
    with open("./Data/books.json", "r") as f:
        data = f.read()

    for element in eval(data):
        #check element is in collection
        if element["Book_Id"] not in db["books"].find({}).distinct("Book_Id"):
            db["books"].insert_one(element)
        else:
            continue
    print("Imported books data successfully")

if "books" in db.list_collection_names():
    print("Collection books already existed")
    #import data from ./Data/books.json
    import_books_data()
else:
    collection = db.create_collection("books")
    print("Collection books created")
    #import data from ./Data/books.json to collection
    import_books_data()

#check there was collection named transactions in db
def import_transactions_data():
    #import data from ./Data/transactions.json to collection
    with open("./Data/transactions.json", "r") as f:
        data = f.read()

    for element in eval(data):
        #check element is in collection
        if element["Transaction_Id"] not in db["transactions"].find({}).distinct("Transaction_Id"):
            db["transactions"].insert_one(element)
        else:
            continue
    print("Imported transactions data successfully")


if "transactions" in db.list_collection_names():
    print("Collection transactions already existed")
    #import data from ./Data/transactions.json
    import_transactions_data()
else:
    collection = db.create_collection("transactions")
    print("Collection transactions created")
    #import data from ./Data/transactions.json to collection
    import_transactions_data()

ctypes.windll.user32.MessageBoxW(0, "Setup successfully!!!!!\nWelcome to Group9  <3", "Group9", 1)