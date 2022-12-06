use museum;
#T1
#For the database museum, we have art_object to display attibutes for an art_obect, it has a foreign key of artist, which reference
#to the artist table for the key attribute, the name. The key attribute here is Id_num of the art_object.
select * from museum.art_object;
#For artist, it has attributes requires from the client for artist. No foreign key here. The Key of arttist are their name
select * from museum.artist;
#For belong_to_collection, it is relation to link up art object and collection. There will be super key of Id_num and Collection_name
#which both of them are foreign key, reference to art_object and Collection respectively
select * from museum.belong_to_collection;
#For borrowed, it is showing the art object that is borrowed. It has a key that reference to Id_num, the key of art_object
select * from museum.borrowed;
#For collection, it is showing all collection of art museum, it has the key of Name, with no foreign key
select * from museum.collection;
#For exhibted_in, it is relation to link up art object and exhibition. There will be super key of Id_num and Name_exhibition
#which both of them are foreign key, reference to art_object and exhibition respectively
select * from museum.exhibited_in;
#For exhibition, it is showing all exhibition, with Name as key attribute, no foreign key
select * from museum.exhibition;
#For other, painting, sculp_or_sta, all are subclass of superclass art_object, so they will have key of Id_num, 
#which reference from art_object
select * from museum.other;
select * from museum.painting;
select * from museum.sculp_or_sta;
#For permanent_collection, it is showing the collections that belongs to the art_museum. It has a key that reference to Id_num, the key of art_object
select * from museum.permanent_collection;

#As we did not do access control, we use database to manage users, which is the museumusers database
use museumusers;
#the users table is showing the username, password and Access_Level. The username will be the key 
select * from museumusers.users;
#The block_list shows all users being blocked and the start date. The key here is foreign key, reference to Username of useres relation
select * from museumusers.block_list;

use museum;
#T2
select Id_num, Artist, Title
from museum.art_object
where Country='Italy';

#T3
select *
from museum.collection
order by Current_Pnumber;

#T4
select Artist 
from art_object
where Id_num in (select Id_num from EXHIBITED_IN as i, EXHIBITION as e where i.Name_exhibition=e.Name and e.Start_date='01-11-2022');

#T5
select Title, Country, Name_exhibition
from (art_object natural join exhibited_in as all_exhi)
where artist<>'Vincent van Gough';

#T6
Drop trigger if exists wrong_art_date;
create trigger wrong_art_date
before update on art_object
for each row
		set new.Year=IF (new.Year < (select Date_born from artist as a, art_object as o where o.artist=a.Name) or
        new.Year > (select Date_die from artist as a, art_object as o where o.artist=a.Name), 
        (select Date_die from artist as a, art_object as o where o.artist=a.Name),new.Year);


#T7
Drop trigger if exists null_artist;
create trigger null_artist
before delete on artist
for each row 
		Update art_object
        set art_object.artist=null
        where art_object.artist=old.Name;
        
