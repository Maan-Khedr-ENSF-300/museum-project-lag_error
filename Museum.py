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
    database="museumusers"
)
cur_museum=museum.cursor()
cur_user=users.cursor()


def log_in():
    print("Welcom to Museum")
    print()

    username=input("Please enter you username: ")
    cur_user.execute("Select * from Users where Username=%(Username)s",{'Username':username})
    user_list=cur_user.fetchone()

    while user_list is None:
        if username=="q":
            return 0
        print("Invalid user")
        username=input("Please enter username or q for ending this app: ")
        cur_user.execute("Select * from Users where Username=%(Username)s",{'Username':username})

        
    pwd=input("Please enter your password: ")
    while pwd!=user_list[1]:
        if pwd=="q":
            return 0
        print("Invalid password")
        pwd=input("Please enter your password or q for ending this app")

    cur_user.execute("Select Username from Block_List where Username=%(Username)s",{'Username':username})
    blocked=[cur_user.fetchone()]

    if blocked[0]:
        print("Sorry, user is blocked.")
        return
    return user_list[2]


def input_sql():
    choice=input("Which one are you changing? 1-Museum, 2-User")
    command=input("Please input command for SQL:")
    if choice==1:
        cur_museum.execute(command)
        cur_museum.commit()
    elif choice==2:
        cur_user.execute(command)
        cur_user.commit()
    else: 
        return

def add_user():
    username=input("Please input new username: ")
    password=input("Please input new password: ")
    user_type=input("Please input user type (1-end user, 2-data entry, 3-admin): ")
    val=(username, password, user_type)
    command="INSERT INTO Users(Username, Passwrd, Access_Level) VALUES (%s,%s,%s)"
    cur_user.execute(command,val)
    print("User added successfully")
    cur_user.commit()
    return

def edit_user():
    alter_user=input("Which user you would like to change? ")
    cur_user.execute("Select * from Users where Username=%(Username)s",{'Username':alter_user})
    user_list=cur_user.fetchone()
    while user_list is None:
        if alter_user=="q":
            return 0
        print("Invalid user")
        alter_user=input("Please enter username or q for previous page: ")
        cur_user.execute("Select * from Users where Username=%(Username)s",{'Username':alter_user})

    edit_info=input("Please input the attribute you would like to update (Username/Passwrd/Access_Level):")
    new_info=input("Please input the new information:")
    command=("Update Users SET %(edit_info)s=%(New_info)s Where Username=%(alter_user)s")
    value=(edit_info,new_info,alter_user)
    cur_user.execute(command,value)
    print("User edited successfully")
    cur_user.commit()

    return

def remove_user():
    del_user=input("Which user you would like to change? ")
    cur_user.execute("Select * from Users where Username=%(Username)s",{'Username':del_user})
    user_list=cur_user.fetchone()
    while user_list is None:
        if del_user=="q":
            return 0
        print("Invalid user")
        del_user=input("Please enter username or q for previous page: ")
        cur_user.execute("Select * from Users where Username=%(Username)s",{'Username':del_user})
    
    cur_user.execute("Select * from Block_List where Username=%(Username)s",{'Username':del_user})
    user_list=cur_user.fetchone()
    if user_list is not None:
        command=("Delete from Block_List Where Username=%(Username)s")
        cur_user.execute(command,{'Username':del_user})


    command=("Delete from Users Where Username=%(Username)s")
    cur_user.execute(command,{'Username':del_user})


    print("User deleted successfully")
    cur_user.commit()

    return


def block_unblock_user():
    change_user=input("Which user you would like to change his/her block state? ")
    cur_user.execute("Select * from Users where Username=%(Username)s",{'Username':change_user})
    user_list=cur_user.fetchone()
    while user_list is None:
        if del_user=="q":
            return 0
        print("Invalid user")
        del_user=input("Please enter username or q for previous page: ")
        cur_user.execute("Select * from Users where Username=%(Username)s",{'Username':change_user})
    
    cur_user.execute("Select * from Block_List where Username=%(Username)s",{'Username':change_user})
    user_list=cur_user.fetchone()
    if user_list is None:
        date=input("The date of the block starts is:")
        value=(change_user, date)
        command="INSERT INTO Block_List (Username, Blocked_Date) VALUES (%(Username)s,%(Block_Date)s)"
        print("This user is being blocked")
    else:
        command=("Delete from Block_List Where Username=%(Username)s")
        value={'Username':change_user}
        print("This user is unblocked")
    
    cur_user.execute(command,value)
    cur_user.commit()
    return

def show_user():
    cur_user.execute("Select Username, Passwrd, Access_Level from Users Where Access_Level<>3")
    print("{:<15}, {:<15}, {}".format("Username", "Password", "Access Level"))
    for (Username, Passwrd, Access_Level) in cur_user:
        print("{:<15}, {:<15}, {}".format(Username, Passwrd, Access_Level))

def show_block_list():
    cur_user.execute("Select Username, Blocked_Date from Block_List")
    print("{:<15}, {:<15}".format("Username", "Block Date"))
    for (Username, Block_Date) in cur_user:
        print("{:<15}, {:<15}".format(Username, Block_Date))

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

def change_user_menu():
    choice=100
    while choice not in range(0,7):
        print("Please chose the number 0 to 6\n")
        print("Press 0: Previous page \n")
        print("Press 1: Add user\n ")
        print("Press 2: Update user\n")
        print("Press 3: Remove user\n")
        print("Press 4: Block/Unblock user\n")
        print("Press 5: View all non-admin users\n")
        print("Press 6: View all blocked users\n")
        choice = int(input("please chose the options: \n"))
    return choice 

def change_user():
    choice=change_user_menu()
    while choice!=0:
        if choice==1:
            add_user()
        if choice==2:
            edit_user()
        if choice==3:
            remove_user()
        if choice==4:
            block_unblock_user()
        if choice==5:
            show_user()
        if choice==6:
            show_block_list()
        choice=change_user_menu()
    return

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
        print("Data added correctly")
    if table == "artist":
        sql = "INSERT INTO ARTIST (Name, Date_born, Date_die, Country, Epoch, Main_Style, Description) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.executemany(sql,data)
        print("Data added correctly.")
    if table == "collection":
        sql = "INSERT INTO COLLECTION (Name, Type, Description, Current_PNumber) VALUES (%s, %s, %s, %s)"
        cursor.executemany(sql,data)
        print("Data added correctly.")
    if table == "exhibition":
        sql = "INSERT INTO EXHIBITION (Name, Start_date, End_date) VALUES (%s, %s, %s)"
        cursor.executemany(sql,data)
        print("Data added correctly.")
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


def admin_menu():
    choice=100
    while choice not in range(0,6):
        print("Please chose the number 0 to 5\n")
        print("Press 0: Quit the program \n")
        print("Press 1: Change user information\n ")
        print("Press 2: Change database\n")
        print("Press 3: Change data\n")
        print("Press 4: View data\n")
        print("Press 5: Direct input sql command")
        choice = int(input("please chose the options: \n"))
    return choice 

def admin():
    choice=admin_menu()
    while choice!=0:
        if choice==1:
            change_user()
        if choice==2:
            modify_database()
        if choice==3:
            data_entry(3)
        if choice==4:
            end_user(3)
        if choice==5:
            input_sql()
        choice=admin_menu()
    return


def main():
    pass
main()