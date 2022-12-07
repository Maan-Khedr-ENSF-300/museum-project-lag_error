DROP DATABASE IF EXISTS museumusers;
CREATE DATABASE museumusers; 
USE museumusers;

DROP TABLE IF EXISTS Users;
CREATE TABLE Users(
	Username		varchar(30) not null,
	Passwrd		varchar(30) not null,
	Access_Level	int(20) not null,
	primary key(Username)
);
INSERT INTO Users(Username, Passwrd, Access_Level)
VALUES
('Bob', 'Abc123p34', '1'),
('Tim', 'BlueBigB', '1'),
('Zack', '13#%@KFFc', '2'),
('Joe', 'password', '1'),
('Zoe', '1234','1'),
('ThatGuy', '20020202','1'),
('Lokko','ENSF300','3');


DROP TABLE IF EXISTS Block_List;
CREATE TABLE Block_List(
	Username		varchar(30) not null,
	Blocked_Date	varchar(20) not null,
	foreign key(Username) references Users(Username)
);
INSERT INTO Block_List(Username, Blocked_Date)
VALUES
('Joe', 'May 4 2021'),
('Zoe', 'Jan 8 2019'),
('ThatGuy', 'Feb 28 2020')