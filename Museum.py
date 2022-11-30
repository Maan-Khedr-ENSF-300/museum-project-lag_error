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
    pass

def modify_info():
    pass

def data_entry_menu():
    pass

def data_entry():
    pass

def end_user_menu(user_type):
    choice=100
    while choice not in range(0,5):
        if user_type == 1:
            print("Please chose the number 0 to 4 \n")
        else:
            print("Please chose the number 0 to 5 \n")

        print("Press 0: Quit the program \n")
        print("Press 1: Search for the artist by name\n ")
        print("Press 2: Search for the art-piece by name\n")
        print("Press 3: Search for the collection by name\n")
        print("Press 4: Search for the exhibition\n")
        if user_type != 1:
            print("Press 5: To go back")
        choice = int(input("please chose the options: \n"))
        if user_type == 1 and choice==5:
            choice=100

    return choice 

def end_user(user_type):
    choice = end_user_menu(user_type)
    
    if choice == 1:
        artist= input("Enter your artist name:").lower
        artist_search(artist)


    elif choice ==2:
        pass
    elif choice ==3:
        pass
    elif choice ==4:
        print("Please enter 1 if you want to search for a specific name ")
        print("Please enter 2 if you want to see the exhibitions:")
    else:
        choice = end_user_menu
def artist_search(artist_name):
    cursor.execute("select")


def main():
    pass
