DROP DATABASE IF EXISTS museum;
CREATE DATABASE museum; 
USE museum;

DROP TABLE IF EXISTS ARTIST;
CREATE TABLE ARTIST(
	Name			int(10) not null,
	Date_born		int(10),
	Date_die		int(10),
	Country         varchar(25) not null,
	Epoch			varchar(25) not null,
	Main_Style      varchar(25) not null,
	Description 	varchar(100),	

	primary key(Name)
);

DROP TABLE IF EXISTS art_object;
CREATE TABLE art_object(
	Id_num				int(10) not null,
	Artist				varchar(25),
	Year				int(4),
	Title				varchar(30)	not null,
    Description			varchar(100) not null,
    Country				varchar(30) not null,
    Epoch				varchar(20) not null,
	Style				varchar(20) not null,
    
	primary key (Id_num)  ,
	foreign key(Artist) references Artist(Name)

);

DROP TABLE IF EXISTS PAINTING;
CREATE TABLE PAINTING(
	Id_num				int(10) not null,
	Paint_type			varchar(25) not null,
	Drawn_on			varchar(25) not null,
	primary key (Id_num),
	foreign key(Id_num) references art_object(Id_num)

);

DROP TABLE IF EXISTS SCULP_OR_STA;
CREATE TABLE SCULT_OR_STA(
	Id_num				int(10) not null,
	Materials			varchar(25) not null,
	Height				int(10) not null,
	Weight				int(10) not null,
	primary key (Id_num),
	foreign key(Id_num) references art_object(Id_num)

);

DROP TABLE IF EXISTS OTHER;
CREATE TABLE OTHER(
	Id_num				int(10) not null,
	Type				varchar(25) not null,
	primary key (Id_num),
	foreign key(Id_num) references art_object(Id_num)

);

DROP TABLE IF EXISTS PERMANET_COLLECTION;
CREATE TABLE PERMANET_COLLECTION(
	Id_num				int(10) not null,
	Date				int(10) not null,
	Status				varchar(25) not null,
	primary key(Id_num),
	foreign key(Id_num) references art_object(Id_num)

);

DROP TABLE IF EXISTS BORROWED;
CREATE TABLE BORROWED(
	Id_num				int(10) not null,
	Date_borrowed		int(10) not null,
	Date_return			int(25) not null,
	primary key(Id_num),
	foreign key(Id_num) references art_object(Id_num)

);


DROP TABLE IF EXISTS COLLECTION;
CREATE TABLE COLLECTION(
	Name 			VARCHAR(30) not null,
	Type 			VARCHAR(30) not null,
	Description		VARCHAR(100) not null, 
	Current_Pnumber	VARCHAR(20)	not null,
	primary key(Name)
);

DROP TABLE IF EXISTS BELONG_TO_COLLECTION
CREATE TABLE BELONG_TO_COLLECTION(
	Id_Num 			int(20) not null,
	Collection_name			varchar(30) not null,
	foreign key(Id_num) references art_object(Id_num),
	foreign key(Collection_name) references COLLECTION(name) 
);

DROP TABLE IF EXISTS EXHIBITION;
CREATE TABLE EXHIBITTION(
	Name			int(20) not null,
	Start_date		int(20) not null,
	End_date		int(20) not null,			
	primary key(name)
);


DROP TABLE IF EXISTS EXHIBITED_IN;
CREATE TABLE EXHIBITED_IN(
	Id_num			int(20) not null,
	Name_exhibition	varchar(20) not null,
	foreign key(Id_num) references art_object(Id_num),
	foreign key(Name_exhibition) references Exhibition(Name) 
	
);



