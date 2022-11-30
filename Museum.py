from getpass import getpass
import mysql.connector
import numpy as np
import sys 

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
    print("Welcom to Museum")
    print()
    user_password_class="Select "    ####wait for aidan
    username=input("Please enter you username")
    # while username not in user_List:
    #     if user=="q":
    #         return 0
    #     print("Invalid user")
    #     user=input("Please enter username or q for ending this app")
    # pwd=input("Please enter your password: ")
    # while pwd!=user_List[user]:
    #     if user=="q":
    #         return 0
    #     print("Invalid password")
    #     user=input("Please enter your password or q for ending this app")
    return 1


def add_user():
    pass

def edit_user():
    pass

def block_user():
    pass

def modify_database():
    connection = mysql.connect(host="localhost",user="root", passwd="password", database="museum") 
    cursor = connection.cursor() 
    link=input("Please put the path of the database: ")
    f = open(link)
    full_sql = f.read()
    if not full_sql:
        print("Invalid Link")
        return
    sql_commands = full_sql.replace('\n', '').split(';')[:-1]
    for sql_command in sql_commands: 
        cursor.execute(sql_command)
        cursor.close()  
    global museum
    museum=connection


def admin_menu():
    pass

def admin():
    pass

def add_tuples():
    pass

def modify_info():
    pass

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


main()