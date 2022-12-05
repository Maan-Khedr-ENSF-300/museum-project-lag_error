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
    connection = mysql.connect(host="localhost", user="root", passwd="password", database="museum")
    cursor = connection.cursor()
    print("Options:")
    print("artobj, artist, collection, exhibition")
    table = input("Please enter the table for data insertion. Entries are case sensitive:")

    choice = input("Enter 1 to provide file, enter 2 to use prompts:")
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
            data = tuple(idnoinput, artistinput, yearinput, titleinput, Dscrpinput, Cntryinput, Epocinput, Styleinput)
        if table == "artist":
            nameinput = input("Enter the artist's name")
            dborninput = input("Enter the year they were born")
            ddieinput = input("Enter the year the artist died")
            contryinput = input("Enter the country they are from")
            epoch2input = input("Enter their era")
            mstyleinput = input("Enter their main style")
            descinput = input("Enter a description of them")
            data = tuple(nameinput, dborninput, ddieinput, contryinput, epoch2input, mstyleinput, descinput)
        if table == "collection":
            colnameinput = input("Enter the name of the collection")
            typeinput = input("Enter the type of the collection")
            dcrinput = input("Enter description of the collection")
            pnuminput = input("Enter current pnumber")
            data = tuple(colnameinput, typeinput, dcrinput, pnuminput)
        if table == "exhibition":
            exnameinput = input("Enter the name of the exhibition")
            sdateinput = input("Enter the startdate of the exhibition")
            edateinput = input("Enter the end date of the exhibition")
            data = tuple(exnameinput, sdateinput, edateinput)

    if table == "artobj":
        sql = "INSERT INTO art_object (Id_num, Artist, Year, Title, Description, Country, Epoch, Style) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
        cursor.executemany(sql, data)
    if table == "artist":
        sql = "INSERT INTO ARTIST (Name, Date_born, Date_die, Country, Epoch, Main_Style, Description) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.executemany(sql,data)
    if table == "collection":
        sql = "INSERT INTO COLLECTION (Name, Type, Description, Current_PNumber) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql,data)
    if table == "exhibition":
        sql = "INSERT INTO EXHIBITION (Name, Start_date, End_date) VALUES (%s, %s, %s)"
        cursor.executemany(sql,data)
    connection.commit()

def modify_info():
    print("preparing to update data")
    connection = mysql.connect(host="localhost", user="root", passwd="password", database="museum")
    cursor = connection.cursor()
    print("Options:")
    print("artobj, artist, collection, exhibition")
    table = input("Please enter the table for data insertion.")

    # Fnction will update info for art object, artist, exhibition, collection. 
    if table == "artobj":
        row = input("Please enter the Id_num of the art object you'd like to update:")
        print("Options for the attribute to be updated are:")
        print("Artist, Year, Title, Description, Country, Epoch, Style")
        attriinput = input("Enter the attribute to be updated. Entries are case sensitive:")
        userinput = input("What is the new value to enter:")
        cursor.execute(f"UPDATE art_object SET '{attriinput}' ='{userinput}',WHERE Id_num = '{row}'")
        connection.commit()
    if table == "artist":
        row2 = input("Please enter the Name of the art object you'd like to update:")
        print("Options for the attribute to be updated are:")
        print("Date_born, Date_die, Country, Epoch, Main_Style, Description")
        attriinput2 = input("Enter the attribute you'd like to update. Entries are case sensitive:")
        userinput2 = input("What is the new value to enter:")
        cursor.execute(f"UPDATE ARTIST SET '{attriinput2}' = '{userinput2}',WHERE Name = '{row2}'")
        connection.commit()
    if table == "collection":
        row3 = input("Please enter the Name of the collection you'd like to update:")
        print("Options for the attribute to be updated are:")
        print("Type, Description, Current_PNumber")
        attriinput3 = input("Enter the attribute you'd like to update. Entries are case sensitive:")
        userinput3 = input("What is the new value to enter:")
        cursor.execute(f"UPDATE COLLECTION SET '{attriinput3}' = '{userinput3}',WHERE Name = '{row3}'")
        connection.commit()
    if table == "exhibition":
        row4 = input("Please enter the Name of the exhibition you'd like to update:")
        print("Options for the attribute to be updated are:")
        print("Start_date, End_date")
        attriinput4 = input("Enter the attribute you'd like to update. Entries are case sensitive:")
        userinput4 = input("What is the new value to enter:")
        cursor.execute(f"UPDATE EXHIBITION SET '{attriinput4}' = '{userinput4}',WHERE Name = '{row4}'")
        connection.commit()

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
