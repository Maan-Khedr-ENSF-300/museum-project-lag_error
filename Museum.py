from getpass import getpass
import mysql.connector

museum=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123321Long@",
    database="museum"
)

users=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123321Long@",
    database="museumusers"
)
cur_museum=museum.cursor()
cur_user=users.cursor()


def log_in():
    print("Welcom to Museum")
    print()

    username=input("Please enter you username: ")
    if username=="q":
        return 0
    cur_user.execute("Select * from users where Username=%(Username)s",{'Username':username})
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
        pwd=input("Please enter your password or q for ending this app: ")

    cur_user.execute("Select Username from Block_List where Username=%(Username)s",{'Username':username})
    blocked=[cur_user.fetchone()]

    if blocked[0]:
        print("Sorry, user is blocked.")
        return
    return user_list[2]

def valid_check(table_name, primary_keytype, primary_key):
    # execute the select statement
    # search_name is row to search, table_name self explanator, primary_keytype tells if it is id_num or name since it changes depending on table
    # primary_key is the value that they entered for the primary key
    cur_museum.execute("Select * from " +table_name+" where "+primary_keytype+"=%(pkey)s",{'pkey':primary_key})
    museum_list = cur_museum.fetchone()
    if museum_list is None:
        return False
    else:
        return True

def artist_search(artist_name):
    list_of_artist = []

    cur_museum.execute("select* from ARTIST where Name = %(Name)s",{'Name':artist_name})
    list_of_artist= cur_museum.fetchone()
    while list_of_artist is None :
        if artist_name=='q':
            return
        print("artist name is not valid")
        artist_name = input('Please enter a new artist name:')
        cur_museum.execute("select* from ARTIST where Name = %(Name)s",{'Name':artist_name})
        
    
    cur_museum.execute("SELECT Name, Date_born, Date_die, Country, Epoch, Main_Style, Description from ARTIST where Name = %(Name)s",{'Name':artist_name})
    row_artist = cur_museum.fetchone()
    for i in range (0,7):
        if row_artist[i] == "":
            row_artist[i] = "Not valid"

    print("Name of artist: "+str(row_artist[0]))
    print("Date born: "+str(row_artist[1]))
    print("Date die: "+str(row_artist[2]))
    print("Country: "+str(row_artist[3]))
    print("Epoch: "+str(row_artist[4]))
    print("Main Style: "+str(row_artist[5]))
    print("Desciption: "+str(row_artist[6]))
        
def art_piece_search(art_piece):
    cur_museum.execute("select* from ART_OBJECT where Title= %(Title)s",{'Title': art_piece})
    list_of_arobject = cur_museum.fetchone()
    while list_of_arobject is None:
        if art_piece=="q":  ###previous page
            return          ###
        print("Your art_object not found")
        art_piece = input("Enter you art-piece name:")
        cur_museum.execute("select* from ART_OBJECT where Title = %(Title)s",{'Title':art_piece})
    cur_museum.execute("Select Id_num, Artist, Year, Title, Description, Country, Epoch, Style from ART_OBJECT where Title= %(Title)s",{'Title': art_piece})
    row_art_piece = cur_museum.fetchone()
    print("Name of the object: "+ str(row_art_piece[3]))
    print("Name of the artist: "+ str(row_art_piece[1]))

def colect_search(colect_name):
    list_of_collection =[]
    cur_museum.execute("select Name from COLLECTION where Name =%(Name)s", {'Name':colect_name})
    list_of_collection =cur_museum.fetchone()
    while list_of_collection is None:
        if colect_name == "q":
            return
        print("Your art_object not found")
        colect_name = input("Please enter the collection you looking for: ")
        cur_museum.execute("select Name from COLLECTION where Name =%(Name)s", {'Name':colect_name})
    cur_museum.execute("Select Name, Type, Description, Current_Pnumber from COLLECTION where Name =%(Name)s", {'Name':colect_name})
    row_collection =cur_museum.fetchone()
    for i in range(0,4):
        if row_collection[i]== "":
            row_collection[i] = "Not mentioned"
    print("Collection name: "+str(row_collection[0]))
    print("Type: "+str(row_collection[1]))
    print("Description: " + str(row_collection[2]))
    print("Current phone number: " + str(row_collection[3]))

def search_exhibition(exhibition):
    if exhibition == '1':
        exhibition_name =input("Type your exhibition you want to search: ")
        list_of_exhibition=[]
        cur_museum.execute("select Name from EXHIBITION where Name =%(Name)s", {'Name':exhibition_name})
        list_of_exhibition=cur_museum.fetchall()
        while list_of_exhibition is None:
            if exhibition_name == 'q':
                return
            print("Your exhibtion is not found")
            exhibtion_name =input("Type your exhibition you want to search: ")
            cur_museum.execute("select Name from EXHIBITION where Name =%(Name)s", {'Name':exhibition_name})
        cur_museum.execute("Select Name, Start_date, End_date, End_date from EXHIBITION where Name =%(Name)s", {'Name':exhibition_name})
        row_exhibition= cur_museum.fetchone()
        print("Exhibition name: " +str(row_exhibition[0]) + " is found")
        print("Exhibition start date: " +str(row_exhibition[1]))
        print("Exhibition end date: " +str(row_exhibition[2]))
    elif exhibition =="2":
        list_of_exhibition=[]
        cur_museum.execute("select Name from EXHIBITION")
        list_of_exhibition=cur_museum.fetchall()
        print("The collections are")
        for i in list_of_exhibition:
            print(i[0])
    return

def end_user_menu(user_type):
    choice=100
    while choice not in range(0,6):
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
            print("Press 5: Previous Page")
        choice = int(input("please chose the options: \n"))
        if user_type == 1 and choice==5:
            choice=100

    return choice 

def end_user(user_type):
    choice = end_user_menu(user_type)
    while choice!=0:
        if choice == 1:
            artist= input("Enter your artist name:")
            artist_search(artist)

        elif choice ==2:
            art_piece = input("Enter you art-piece name:")
            art_piece_search(art_piece)

        elif choice ==3:
            colect_name = input("Please enter the collection you looking for: ")
            colect_search(colect_name)
        elif choice ==4:
            exhibition=input("Please enter 1 if you want to search for a specific name\nPlease enter 2 if you want to see the exhibitions:")
        
            search_exhibition(exhibition)
        choice = end_user_menu(user_type)
    return

def add_tuples():
    print("Preparing to insert new tuple(s) into a table in the database.")
    cursor = museum.cursor()
    table='none'
    while table!="artobj" and table!="artist" and table!="collection" and table!="exhibition":
        if table=='q':
            return
        print("Options:")
        print("artobj, artist, collection, exhibition")
        table = input("Please enter the table for data insertion. Entries are case sensitive:")

    choice = input("Enter 1 to provide file, enter 2 to use prompts:")
    choice = int(choice)

    if choice == 1:
        filename = input("Enter file name")
        with open(filename) as f:
            lines = f.readlines()
            data = (tuple(line.split()) for line in lines)
    
    if choice == 2:
        if table == "artobj":
            print("Before adding a new object please check if the artist of the object are stored in our data first\n If the artist is not found please enter the artist information first")
            artist_check = input("Please enter your artist")
            list_of_artist = []
            cur_museum.execute("select* from ARTIST where Name = %(Name)s",{'Name':artist_check})
            list_of_artist= cur_museum.fetchone()
            while list_of_artist is None:
                print("The artist is not exist in our data")
                print("Please press 2 to add data and type artist to add info of the artist before adding this art-piece")
            print("The artist is in our data-Please enter the infomation about the art-piece")
                

            idnoinput = input("Enter the id_no: ")
            artistinput = input("Enter the name of the artist: ")
            yearinput = input("Enter the year of the art: ")
            titleinput = input("Enter the title: ")
            Dscrpinput = input("Enter description of the piece: ")
            Cntryinput = input("Enter the country for the piece: ")
            Epocinput = input("Enter epoc: ")
            Styleinput = input("Enter the style of the art: ")
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
        sql = "INSERT INTO art_object(Id_num, Artist, Year, Title, Description, Country, Epoch, Style) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)" 
        cursor.execute(sql, data)
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
    museum.commit()

def modify_info():
    print("preparing to update data")
    cursor = museum.cursor()
    print("Options:")
    print("artobj, artist, collection, exhibition")
    table = input("Please enter the table for data insertion.")
    while table != "artobj" and table != "artist" and table != "collection" and table != "exhibition":
        print("Invalid table")
        print("Options:")
        print("artobj, artist, collection, exhibition")
        table = input("Please enter the table for data insertion.")

    # Fnction will update info for art object, artist, exhibition, collection. 
    if table == "artobj":
        check=False
        while check==False:
            row = input("Please enter the Id_num of the art object you'd like to update or q for previous page:")
            if row=="q":
                return
            check=valid_check('art_object','Id_num',row)

        print("Options for the attribute to be updated are:")
        print("Artist, Year, Title, Description, Country, Epoch, Style")
        #Same, do some check and loop here, so do other s
        attriinput = input("Enter the attribute to be updated. Entries are case sensitive:")
        userinput = input("What is the new value to enter:")

        sql="UPDATE art_object SET " + attriinput +" =%s WHERE Id_num = %s"
        value=(userinput,row)
        cursor.execute(sql, value)
        museum.commit()
    if table == "artist":
        check = False
        while check == False:
            row2 = input("Please enter the Name of the object you'd like to update or q for previous page:")
            if row2=="q":
                return
            check = valid_check('ARTIST', 'Name', row2)
        print("Options for the attribute to be updated are:")
        print("Date_born, Date_die, Country, Epoch, Main_Style, Description")
        attriinput2 = input("Enter the attribute you'd like to update. Entries are case sensitive:")
        userinput2 = input("What is the new value to enter:")
        sql = "UPDATE ARTIST SET " + attriinput2 +" =%s WHERE Name = %s"
        value =(userinput2,row2)
        cursor.execute(sql,value)
        museum.commit()
    if table == "collection":
        check = False
        while check == False:
            row3 = input("Please enter the Name of the collection you'd like to update or q for previous page:")
            if row3 == "q":
                return
            check = valid_check('COLLECTION', 'Name', row3)
        print("Options for the attribute to be updated are:")
        print("Type, Description, Current_PNumber")
        attriinput3 = input("Enter the attribute you'd like to update. Entries are case sensitive:")
        userinput3 = input("What is the new value to enter:")
        sql="UPDATE COLLECTION SET " + attriinput3 +" =%s WHERE Name = %s"
        value(userinput3,row3)
        cursor.execute(sql,value)
        museum.commit()
    if table == "exhibition":
        check = False
        while check == False:
            row4 = input("Please enter the Name of the exhibition you'd like to update or q for previous page:")
            if row4 == "q":
                return
            check = valid_check('EXHIBITION', 'Name', row4)
        print("Options for the attribute to be updated are:")
        print("Start_date, End_date")
        attriinput4 = input("Enter the attribute you'd like to update. Entries are case sensitive:")
        userinput4 = input("What is the new value to enter:")
        sql="UPDATE EXHIBITION SET " + attriinput4 +" =%s WHERE Name = %s"
        value(userinput4,row4)
        cursor.execute(sql,value)
        museum.commit()
def remove_info():
    print("Options:")
    print("artobj, artist, collection, exhibition")
    table = input("Please enter the table to remove info from: ")
    while table != "artobj" and table != "artist" and table != "collection" and table != "exhibition":
        print("Invalid table")
        print("Options:")
        print("artobj, artist, collection, exhibition")
        table = input("Please enter the table to remove info from: ")
    if table == "artobj":
        del_info = int(input("What is the Id_num of the art object you'd like to delete: "))
        cur_museum.execute("Select * from art_object where Id_num =%(Id_num)s",{'Id_num':del_info})
        museum_list = cur_museum.fetchone()
        while museum_list is None:
            if del_info == "q":
                return
            print("Invalid Id_num")
            del_info = input("Please enter an Id_num or q for previous page: ")
            cur_museum.execute("Select * from art_object where Id_num =%(Id_num)s",{'Id_num':del_info})
        
        cur_museum.execute("Select * from PAINTING Where Id_num =%(Id_num)s",{'Id_num':del_info})
        museum_list = cur_museum.fetchone()
        if museum_list is not None:
            command = ("Delete from PAINTING Where Id_num=%(Id_num)s")
            cur_museum.execute(command,{'Id_num':del_info})
        
        cur_museum.execute("Select * from SCULP_OR_STA Where Id_num = %(Id_num)s",{'Id_num':del_info})
        museum_list = cur_museum.fetchone()
        if museum_list is not None:
            command = ("Delete from SCULP_OR_STA Where Id_num=%(Id_num)s")
            cur_museum.execute(command,{'Id_num':del_info})
        
        cur_museum.execute("Select * from PERMANENT_COLLECTION Where Id_num = %(Id_num)s",{'Id_num':del_info})
        museum_list = cur_museum.fetchone()
        if museum_list is not None:
            command = ("Delete from PERMANENT_COLLECTION Where Id_num=%(Id_num)s")
            cur_museum.execute(command,{'Id_num':del_info})
        
        cur_museum.execute("Select * from BORROWED Where Id_num = %(Id_num)s",{'Id_num':del_info})
        museum_list = cur_museum.fetchone()
        if museum_list is not None:
            command = ("Delete from BORROWED Where Id_num=%(Id_num)s")
            cur_museum.execute(command,{'Id_num':del_info})
        
        cur_museum.execute("Select * from BELONG_TO_COLLECTION Where Id_num = %(Id_num)s",{'Id_num':del_info})
        museum_list = cur_museum.fetchone()
        if museum_list is not None:
            command = ("Delete from BELONG_TO_COLLECTION Where Id_num=%(Id_num)s")
            cur_museum.execute(command,{'Id_num':del_info})
        
        cur_museum.execute("Select * from EXHIBITED_IN Where Id_num = %(Id_num)s",{'Id_num':del_info})
        museum_list = cur_museum.fetchone()
        if museum_list is not None:
            command=("Delete from EXHIBITED_IN Where Id_num=%(Id_num)s")
            cur_museum.execute(command,{'Id_num':del_info})

        command = ("Delete from art_object Where Id_num=%(Id_num)s")
        cur_museum.execute(command,{'Id_num':del_info})
        print("artobj deleted successfully")
    
    if table == "artist":
        del_info = input("What is the Name of the artist you'd like to delete: ")
        cur_museum.execute("Select * from ARTIST where Name =%(Name)s",{'Name':del_info})
        museum_list = cur_museum.fetchone()
        while museum_list is None:
            if del_info == "q":
                return
            print("Invalid Name")
            del_info = input("Please enter a Name or q for previous page: ")
            cur_museum.execute("Select * from ARTIST where Name =%(Name)s",{'Name':del_info})
        
        cur_museum.execute("Select * from art_object Where Artist=%(Name)s",{'Name':del_info})
        museum_list = cur_museum.fetchone()
        if museum_list is not None:
            cur_museum.execute("Select Id_num from art_object Where Artist=%(Name)s",{'Name':del_info})
            Id_num = cur_museum.fetchone()

# Accounting for Id_num deletions(s)

            cur_museum.execute("Select * from PAINTING Where Id_num =%(Id_num)s",{'Id_num':Id_num})
            museum_list = cur_museum.fetchone()
            if museum_list is not None:
                command = ("Delete from PAINTING Where Id_num=%(Id_num)s")
                cur_museum.execute(command,{'Id_num':Id_num})
        
            cur_museum.execute("Select * from SCULP_OR_STA Where Id_num = %(Id_num)s",{'Id_num':Id_num})
            museum_list = cur_museum.fetchone()
            if museum_list is not None:
                command = ("Delete from SCULP_OR_STA Where Id_num=%(Id_num)s")
                cur_museum.execute(command,{'Id_num':Id_num})
        
            cur_museum.execute("Select * from PERMANENT_COLLECTION Where Id_num = %(Id_num)s",{'Id_num':Id_num})
            museum_list = cur_museum.fetchone()
            if museum_list is not None:
                command = ("Delete from PERMANENT_COLLECTION Where Id_num=%(Id_num)s")
                cur_museum.execute(command,{'Id_num':Id_num})
        
            cur_museum.execute("Select * from BORROWED Where Id_num = %(Id_num)s",{'Id_num':Id_num})
            museum_list = cur_museum.fetchone()
            if museum_list is not None:
                command = ("Delete from BORROWED Where Id_num=%(Id_num)s")
                cur_museum.execute(command,{'Id_num':Id_num})
        
            cur_museum.execute("Select * from BELONG_TO_COLLECTION Where Id_num = %(Id_num)s",{'Id_num':Id_num})
            museum_list = cur_museum.fetchone()
            if museum_list is not None:
                command = ("Delete from BELONG_TO_COLLECTION Where Id_num=%(Id_num)s")
                cur_museum.execute(command,{'Id_num':Id_num})
        
            cur_museum.execute("Select * from EXHIBITED_IN Where Id_num = %(Id_num)s",{'Id_num':Id_num})
            museum_list = cur_museum.fetchone()
            if museum_list is not None:
                command=("Delete from EXHIBITED_IN Where Id_num=%(Id_num)s")
                cur_museum.execute(command,{'Id_num':Id_num})

            command = ("Delete from art_object Where Artist=%(Name)s")
            cur_museum.execute(command,{'Name':del_info})

        command = ("Delete from ARTIST Where Name=%(Name)s")
        cur_museum.execute(command,{'Name':del_info})
        print("Artist deleted successfully")
    
    if table == "collection":
        del_info = input("What is the name of the collection you'd like to delete: ")
        cur_museum.execute("Select * from COLLECTION where Name=%(Name)s",{'Name':del_info})
        museum_list = cur_museum.fetchone()
        while museum_list is None:
            if del_info == "q":
                return
            print("Invalid name")
            del_info = input("Please enter a name or q for previous page: ")
            cur_museum.execute("Select * from COLLECTION where Name=%(Name)s",{'Name':del_info})
        
        cur_museum.execute("Select * from BELONG_TO_COLLECTION where Collection_name=%(Name)s",{'Name':del_info})
        museum_list = cur_museum.fetchone()
        if museum_list is not None:
            command = ("Delete from BELONG_TO_COLLECTION Where Collection_name=%(Name)s")
            cur_museum.execute(command,{'Name':del_info})
        
        command = ("Delete from COLLECTION where Name=%(Name)s")
        cur_museum.execute(command,{'Name':del_info})
        print("Collection deleted successfully")

    if table == "exhibition":
        del_info = input("What is the name of the exhibition you'd like to delete: ")
        cur_museum.execute("Select * from EXHIBITION where Name=%(Name)s",{'Name':del_info})
        museum_list = cur_museum.fetchone()
        while museum_list is None:
            if del_info == "q":
                return
            print("Invalid name")
            del_info = input("Please enter a name or q for previous page: ")
            cur_museum.execute("Select * from EXHIBITION where Name=%(Name)s",{'Name':del_info})
        
        cur_museum.execute("Select * from EXHIBITED_IN where Name_exhibition=%(Name)s",{'Name':del_info})
        museum_list = cur_museum.fetchone()
        if museum_list is not None:
            command = ("Delete from EXHIBITED_IN where Name_exhibition=%(Name)s")
            cur_museum.execute(command,{'Name':del_info})
        
        command = ("Delete from EXHIBITION where Name=%(Name)s")
        cur_museum.execute(command,{'Name':del_info})
        print("Exhibition deleted successfully")
    museum.commit()

    
def data_entry_menu(user_type):
        print("Welcome to the program")
        option=100
        while option not in range(0,6):
            print("Please chose one of the option below")
            print("Press 0: Quit program")
            print("Press 1: Search data")
            print("Press 2: Add data")
            print("Press 3: Update data")
            print("Press 4: Delete data")
            if user_type=='3':
                print("Press 5: Previous page")
            if (option==5 and user_type=='3'):
                return
            option=int(input("Please input your option: "))
        return option

def data_entry(user_type):
    choice = data_entry_menu(user_type)
    while (choice !=0):
        if choice ==1:
            end_user(user_type)
        elif choice ==2:
            add_tuples()
        elif choice ==3:
            modify_info()
        elif choice ==4:
            remove_info()
        elif choice==5:
            return
        choice = data_entry_menu(user_type)
    return
        
def input_sql():
    choice=input("Which one are you changing? 1-Museum, 2-User")
    command=input("Please input command for SQL:")
    if choice==1:
        cur_museum.execute(command)
        museum.commit()
    elif choice==2:
        cur_user.execute(command)
        users.commit()
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
    users.commit()
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
    command="Update Users SET "+ edit_info +"=%s Where Username=%s"
    value=(new_info,alter_user)
    cur_user.execute(command,value)
    print("User edited successfully")
    users.commit()

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
    users.commit()

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
    users.commit()
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


def main():
    user=log_in()
    if user==1:
        end_user(1)
    if user==2:
        data_entry(2)
    if user==3:
        admin()
    print("Thank you for using this database")


if __name__=="__main__":
    main()


