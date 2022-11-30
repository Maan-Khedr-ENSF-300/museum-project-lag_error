DROP DATABASE IF EXISTS museum;
CREATE DATABASE museum; 
USE museum;

DROP TABLE IF EXISTS art_objects;
CREATE TABLE art_object(
<<<<<<< Updated upstream
    Id_num              int(10) not null,
    Artist              varchar(25),
    Year                int(4),
    Title               varchar(30) not null,
    Description         varchar(100) not null,
    Country             varchar(30) not null,
    Epoch               varchar(20) not null,
    Style               varchar(20) not null,
    
    primary key (Id_num)  
=======
	Id_num				int(10) not null,
	Artist				varchar(25),
	Year				int(4),
	Title				varchar(30)	not null,
    Description			varchar(100) not null,
    Country				varchar(30) not null,
    Epoch				varchar(20) not null,
	Style				varchar(20) not null,
    
	primary key (Id_num)  
>>>>>>> Stashed changes
);

DROP TABLE IF EXISTS PAINTING
CREATE TABLE PAINTING(
<<<<<<< Updated upstream
    Id_num              int(10) not null,
    Paint_type          varchar(25) not null,
    Drawn_on            varchar(25) not null,
    primary key (Id_num),
    foreign key(Id_num) references art_object(Id_num)
=======
	Id_num				int(10) not null,
	Paint_type			varchar(25) not null,
	Drawn_on			varchar(25) not null,
	primary key (Id_num),
	foreign key(Id_num) references art_object(Id_num)
>>>>>>> Stashed changes

);

DROP TABLE IF EXISTS SCULP_OR_STA
CREATE TABLE SCULT_OR_STA(
<<<<<<< Updated upstream
    Id_num              int(10) not null,
    Materials           varchar(25) not null,
    Height              int(10) not null,
    Weight              int(10) not null,
    primary key (Id_num),
    foreign key(Id_num) references art_object(Id_num)
=======
	Id_num				int(10) not null,
	Materials			varchar(25) not null,
	Height				int(10) not null,
	Weight				int(10) not null,
	primary key (Id_num),
	foreign key(Id_num) references art_object(Id_num)
>>>>>>> Stashed changes

);

DROP TABLE IF EXISTS OTHER
CREATE TABLE OTHER(
<<<<<<< Updated upstream
    Id_num              int(10) not null,
    Type                varchar(25) not null,
    primary key (Id_num),
    foreign key(Id_num) references art_object(Id_num)
=======
	Id_num				int(10) not null,
	Type				varchar(25) not null,
	primary key (Id_num),
	foreign key(Id_num) references art_object(Id_num)
>>>>>>> Stashed changes

);

DROP TABLE IF EXISTS PERMANET_COLLECTION
CREATE TABLE PERMANET_COLLECTION(
<<<<<<< Updated upstream
    Id_num              int(10) not null,
    Date                int(10) not null,
    Status              varchar(25) not null,
    primary key(Id_num),
    foreign key(Id_num) references art_object(Id_num)
=======
	Id_num				int(10) not null,
	Date				int(10) not null,
	Status				varchar(25) not null,
	primary key(Id_num),
	foreign key(Id_num) references art_object(Id_num)
>>>>>>> Stashed changes

);

DROP TABLE IF EXISTS BORROWED
CREATE TABLE BORROWED(
<<<<<<< Updated upstream
    Id_num              int(10) not null,
    Date_borrowed       int(10) not null,
    Date_return         int(25) not null,
    primary key(Id_num),
    foreign key(Id_num) references art_object(Id_num)
=======
	Id_num				int(10) not null,
	Date_borrowed		int(10) not null,
	Date_return			int(25) not null,
	primary key(Id_num),
	foreign key(Id_num) references art_object(Id_num)
>>>>>>> Stashed changes

);

DROP TABLE IF EXISTS ARTIST
CREATE TABLE ARTIST(
<<<<<<< Updated upstream
    Name                int(10) not null,
    Date_born       int(10),
    Date_die        int(10),
    Country         varchar(25) not null,
    Epoch           varchar(25) not null,
    Main_Style      var_char(25) not null,
    Description     var_char(100),  

    primary key(Name),
    foreign key(name) references art_object(Artist)
=======
	Name				int(10) not null,
	Date_born		int(10),
	Date_die		int(10),
	Country         varchar(25) not null,
	Epoch			varchar(25) not null,
	Main_Style      var_char(25) not null,
	Description 	var_char(100),	

	primary key(Name),
	foreign key(name) references art_object(Artist)
>>>>>>> Stashed changes

);

DROP TABLE IF EXISTS COLLECTION
CREATE TABLE COLLECTION(
<<<<<<< Updated upstream
    Name            VARCHAR(30) not null,
    Type            VARCHAR(30) not null,
    Description     VARCHAR(100) not null, 
    Current_Pnumber VARCHAR(20) not null,
    primary key(Name)
=======
	Name 			VARCHAR(30) not null,
	Type 			VARCHAR(30) not null,
	Description		VARCHAR(100) not null, 
	Current_Pnumber	VARCHAR(20)	not null,
	primary key(Name)
>>>>>>> Stashed changes
);

DROP TABLE IF EXISTS BELONG_TO_COLLECTION
CREATE TABLE BELONG_TO_COLLECTION(
<<<<<<< Updated upstream
    Id_Num          int(20) not null,
    Collection_name         varchar(30) not null,
    foreign key(Id_num) references art_object(Id_num),
    foreign key(Collection_name) references COLLECTION(name) 
=======
	Id_Num 			int(20) not null,
	Collection_name			varchar(30) not null,
	foreign key(Id_num) references art_object(Id_num),
	foreign key(Collection_name) references COLLECTION(name) 
>>>>>>> Stashed changes
);

DROP TABLE IF EXISTS EXHIBITION
CREATE TABLE EXHIBITTION(
<<<<<<< Updated upstream
    Name            int(20) not null,
    Start_date      int(20) not null,
    End_date        int(20) not null,           
    primary key(name)
=======
	Name			int(20) not null,
	Start_date		int(20) not null,
	End_date		int(20) not null,			
	primary key(name)
>>>>>>> Stashed changes
);


DROP TABLE IF EXISTS EXHIBITED_IN
CREATE TABLE EXHIBITED_IN(
<<<<<<< Updated upstream
    Id_num          int(20) not null,
    Name_exhibition varchar(20) not null,
    foreign key(Id_num) references art_object(Id_num),
    foreign key(Name_exhibition) references Exhibition(Name) 
    
=======
	Id_num			int(20) not null,
	Name_exhibition	varchar(20) not null,
	foreign key(Id_num) references art_object(Id_num),
	foreign key(Name_exhibition) references Exhibition(Name) 
	
>>>>>>> Stashed changes
);











<<<<<<< Updated upstream

=======
>>>>>>> Stashed changes
