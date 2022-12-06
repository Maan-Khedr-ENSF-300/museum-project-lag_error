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
            option =input()
            if (option==5 and user_type!='3'):
                continue
        return option


def data_entry(user_type):
    choice = data_entry_menu(user_type)
    while (choice !=0):
        if choice ==1:
            end_user_menu(user_type)
        elif choice ==2:
            add_tuples()
        elif choice ==3:
            modify_info()
        elif choice ==4:
            delete_info()
        elif choice==5:
            return
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
        choice = end_user_menu
    return


def artist_search(artist_name):
    list_of_artist = []

    cur_museum.execute("select* from ARTIST where Name = %(Name)s",{'Name':artist_name})
    list_of_artist= cur_museum.fetchone()
    while list_of_artist is None :
        print("artist name is in valid")
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


'''def delete_info():
    list_of_table_name = []
    cur_museum.execute("SHOW TABLES")
    for table_name in cur_museum:
        list_of_table_name.append(table_name[0])
    for i in list_of_table_name:
        print(i)
    data_user_option= input("please enter the name table you want to delete: ")
    if data_user_option.upper() in list_of_table_name:
        cur_museum.execute(f"Select * from {data_user_option.upper()}")
        list_of_element = cur_museum.fetchall()
        colum_names = cur_museum.column_names
        attribute_size = len(colum_names)
        for i in range(len())
        for table_element in cur_museum:
            list_of_element.append(table_element)
        first_element=input("Enter the "+ str(list_of_element[0])+ " to delete from table"+ str(data_user_option) )
        for i in range(0,len(table_element)):
            cur_museum.execute("Delete* from data_user_option.upper() where table_element[0] = %(table_element)s", {'table_element[0]': first_element})'''










    
        

        

        
        




