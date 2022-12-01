DROP DATABASE IF EXISTS museum;
CREATE DATABASE museum; 
USE museum;

DROP TABLE IF EXISTS art_objects;
CREATE TABLE art_object(
	Id_num				int(10) not null,
	Artist				varchar(25),
	Year				int(4),
	Title				varchar(30)	not null,
    Description			varchar(100) not null,
    Country				varchar(30) not null,
    Epoch				varchar(20) not null,
    
	primary key (Id_num)  
);

DROP TABLE IF EXISTS users;
CREATE TABLE users(
	
)