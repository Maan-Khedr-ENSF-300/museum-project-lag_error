DROP DATABASE IF EXISTS museum;
CREATE DATABASE museum; 
USE museum;

DROP TABLE IF EXISTS art_objects;
CREATE TABLE art_object(
	Id_num				int(10) not null,
	Artist				varchar(25),
	Year				int(4),
	Title				varchar(30)	not null,
	primary key (OlympicID),
	foreign key (Country) references COUNTRY(CName)    
);