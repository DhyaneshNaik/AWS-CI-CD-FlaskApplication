create database UserDetails;
use UserDetails;

create table Employees
(
	Id INT auto_increment primary key,
    Fname VARCHAR(50) not null,
    Lname VARCHAR(50) not null,
    Emailid VARCHAR(50) not null,
    Phone VARCHAR(15) not null
);

drop table Employees;

select * from Employees;

insert into Employees (Fname,Lname,Emailid,Phone) values ("Dhyanesh","Naik","dhyaneshnaik243@gmail.com","+91-9832585555");
insert into Employees (Fname,Lname,Emailid,Phone) values ("Fname","Lname","fname@gmail.com","+91-9834587445");
f"INSERT INTO Employees values ({fname},{lname},{email},{phone})"