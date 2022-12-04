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
    # users=cur_user.fetchall()
    # user_list=[i[2:-2] for i in users]
    # for each in user_list:
    #     print(each)
    username=input("Please enter you username: ")
    cur_user.execute("Select * from Users where Username=%(Username)s",{'Username':username})
    user_list=cur_user.fetchone()

    while user_list==[]:
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
'''
    if user[2]==1:
        end_user()
    elif user[2]==2:
        data_entry()
    elif user[2]==3:
        admin()
'''


def input_sql():
    choice=input("Which one are you changing? 1-Museum, 2-User")
    command=input("Please input command for SQL:")
    if choice==1:
        cur_museum.execute(command)
    elif choice==2:
        cur_user.execute(command)
    else: 
        return

def add_user():
    username=input("Please input new username: ")
    password=input("Please input new password: ")
    user_type=input("Please input user type (1-end user, 2-data entry, 3-admin): ")
    val=(username, password, user_type)
    command="INSERT INTO Users (Username, password, user_type) VALUES (%s,%s,%s)"
    cur_user.execute(command,val)
    print("User added successfully")
    return

def edit_user():
    pass

def remove_user():
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

def change_user_menu():
    choice=100
    while choice not in range(0,4):
        print("Please chose the number 0 to 4\n")
        print("Press 0: Previous page \n")
        print("Press 1: Add user\n ")
        print("Press 2: Update user\n")
        print("Press 3: Remove user\n")
        print("Press 4: Block user\n")
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
            block_user()
        choice=change_user_menu()
    return

def admin_menu():
    choice=100
    while choice not in range(0,5):
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
    usertype=log_in()
    print(usertype)

main()