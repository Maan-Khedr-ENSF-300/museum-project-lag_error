DROP DATABASE IF EXISTS museum;
CREATE DATABASE museum; 
USE museum;

DROP TABLE IF EXISTS ARTIST
CREATE TABLE ARTIST(
	Name			int(20) not null,
	Date_born		int(10),
	Date_die		int(10),
	Country         varchar(25) not null,
	Epoch			varchar(25) not null,
	Main_Style      var_char(25) not null,
	Description 	var_char(100),	

	primary key(Name)
);

INSERT INTO ARTIST (Name, Date_born, Date_die, Country, Epoch, Main_style, Description)
VALUES
('Hans Holbein', 1497, 1543, 'Germany', This_era, This_style, NULL)

DROP TABLE IF EXISTS art_objects;
CREATE TABLE art_object(
	Id_num				int(10) not null,
	Artist				varchar(25),
	Year				int(4),
	Title				varchar(30)	not null,
    Description			varchar(100) not null,
    Country				varchar(30) not null,
    Epoch				varchar(20) ,
	Style				varchar(20) not null,
    
	primary key (Id_num)  ,
	foreign key(Artist) references Artist(Name)

);
INSERT INTO art_objects(Id_num, Artist, Year, Title, Description, Country, Epoch, Styple)
VALUES
('1', 'LEONARDO da Vinci','1503','Monalisa','considered an archetypal masterpice of Italian Renaissance', 'Italy','Renaissance', 'sfumato'),
('2' ,'Vincent van Gough','1889', 'Starry night','considered to be his magnum opus', 'Netherlands', 'Post Impressionist', 'Modern Art'),
('3','Edvand Much','1893','The sream','featuring a ghoulish figure that looks like the host from the Tales from the Crypt', null, 'Symnbolist movement'),
('4', 'Grayson Perry','1994', 'My Gods','depicts four large figures',)





DROP TABLE IF EXISTS PAINTING
CREATE TABLE PAINTING(
	Id_num				int(10) not null,
	Paint_type			varchar(25) not null,
	Drawn_on			varchar(25) not null,
	primary key (Id_num),
	foreign key(Id_num) references art_object(Id_num)

);
INSERT INTO PAINTING(Id_num, Paint_type, Drawn_on)
VALUES
('1', 'Portrait','poplar wood panel'),
('2', 'Portrait','canvas'),
('3', 'Portrai', 'cardboard')

DROP TABLE IF EXISTS SCULP_OR_STA
CREATE TABLE SCULT_OR_STA(
	Id_num				int(10) not null,
	Materials			varchar(25) not null,
	Height				int(10) not null,
	Weight				int(10) not null,
	primary key (Id_num),
	foreign key(Id_num) references art_object(Id_num)

);

DROP TABLE IF EXISTS OTHER
CREATE TABLE OTHER(
	Id_num				int(10) not null,
	Type				varchar(25) not null,
	primary key (Id_num),
	foreign key(Id_num) references art_object(Id_num)

);

DROP TABLE IF EXISTS PERMANET_COLLECTION
CREATE TABLE PERMANET_COLLECTION(
	Id_num				int(10) not null,
	Date				int(10) not null,
	Status				varchar(25) not null,
	primary key(Id_num),
	foreign key(Id_num) references art_object(Id_num)

);

DROP TABLE IF EXISTS BORROWED
CREATE TABLE BORROWED(
	Id_num				int(10) not null,
	Date_borrowed		int(10) not null,
	Date_return			int(25) not null,
	primary key(Id_num),
	foreign key(Id_num) references art_object(Id_num)

);


DROP TABLE IF EXISTS COLLECTION
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

DROP TABLE IF EXISTS EXHIBITION
CREATE TABLE EXHIBITTION(
	Name			int(20) not null,
	Start_date		int(20) not null,
	End_date		int(20) not null,			
	primary key(name)
);


DROP TABLE IF EXISTS EXHIBITED_IN
CREATE TABLE EXHIBITED_IN(
	Id_num			int(20) not null,
	Name_exhibition	varchar(20) not null,
	foreign key(Id_num) references art_object(Id_num),
	foreign key(Name_exhibition) references Exhibition(Name) 
	
);










