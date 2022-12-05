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
    admin()
    #log_in()
main()