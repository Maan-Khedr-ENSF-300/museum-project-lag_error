from getpass import getpass
import mysql.connector
import numpy as np

museum=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="museum"
)

users=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password",
    database="users"
)

def log_in():
    pass

def add_user():
    pass

def edit_user():
    pass

def block_user():
    pass

def modify_database():
    pass

def admin_menu():
    pass

def admin():
    pass

def add_tuples():
    print("Preparing to insert new tuple(s) into a table in the database.")
    connection = mysql.connect(host="localhost", user="root", passwd="password", database="users")
    cursor = connection.cursor()
    table = input("Please enter the table for data insertion.")

    choice = input("Enter 1 to provide file, enter 2 to use prompts")

    if choice == 1:
        filename = input("Enter file name")
        with open(filename) as f:
            lines = f.readlines()
            data = tuple(tuple(line.split()) for line in lines)
    
    # Need to add code for a series of entries through prompts
    # CODE GOES HERE

    sql = "insert into [table] values (?, ?, ?, ?, ?, ?)" 
    cursor.executemany(sql, data)

def modify_info():
    print("Preparing to update the database")
    
# work on this

def data_entry_menu():
    pass

def data_entry():
    pass

def end_user_menu():
    pass

def end_user():
    pass


def main():
    pass
