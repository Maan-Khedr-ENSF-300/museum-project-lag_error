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
    print("Options:")
    print("artobj, artist, collection, exhibition")
    table = input("Please enter the table for data insertion.")

    choice = input("Enter 1 to provide file, enter 2 to use prompts")
    choice = int(choice)

    if choice == 1:
        filename = input("Enter file name")
        with open(filename) as f:
            lines = f.readlines()
            data = tuple(tuple(line.split()) for line in lines)
    
    if choice == 2:
        if table == "artobj":
            idnoinput = input("Enter the id_no")
            artistinput = input("Enter the name of the artist")
            yearinput = input("Enter the year of the art")
            titleinput = input("Enter the title")
            Dscrpinput = input("Enter description of the piece")
            Cntryinput = input("Enter the country for the piece")
            Epocinput = input("Enter epoc")
            Styleinput = input("Enter the style of the art")
            data = (idnoinput, artistinput, yearinput, titleinput, Dscrpinput, Cntryinput, Epocinput, Styleinput)
        if table == "artist":
            nameinput = input("Enter the artist's name")
            dborninput = input("Enter the year they were born")
            ddieinput = input("Enter the year the artist died")
            contryinput = input("Enter the country they are from")
            epoch2input = input("Enter their era")
            mstyleinput = input("Enter their main style")
            descinput = input("Enter a description of them")
            data = (nameinput, dborninput, ddieinput, contryinput, epoch2input, mstyleinput, descinput)
        if table == "collection":
            colnameinput = input("Enter the name of the collection")
            typeinput = input("Enter the type of the collection")
            dcrinput = input("Enter description of the collection")
            pnuminput = input("Enter current pnumber")
            data = (colnameinput, typeinput, dcrinput, pnuminput)
        if table == "exhibition":
            exnameinput = input("Enter the name of the exhibition")
            sdateinput = input("Enter the startdate of the exhibition")
            edateinput = input("Enter the end date of the exhibition")
            data = (exnameinput, sdateinput, edateinput)

    if table == "artobj":
        sql = "insert into [artobj] values (?, ?, ?, ?, ?, ?, ?, ?)" 
        cursor.executemany(sql, data)
    if table == "artist":
        sql = "insert into [artist] values (?, ?, ?, ?, ?, ?, ?)"
        cursor.executemany(sql,data)
    if table == "collection":
        sql = "insert into [collection] values (?, ?, ?, ?)"
        cursor.executemany(sql,data)
    if table == "exhibition":
        sql = "insert into [exhibition] values (?, ?, ?)"
        cursor.executemany(sql,data)

def modify_info():
    print("preparing to update data")
    connection = mysql.connect(host="localhost", user="root", passwd="password", database="users")
    cursor = connection.cursor()
    print("Options:")
    print("artobj, artist, collection, exhibition")
    table = input("Please enter the table for data insertion.")

    
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
