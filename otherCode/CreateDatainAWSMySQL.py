import pymysql

db = pymysql.connect("userdetails.ck2j6hk9ucgh.ap-south-1.rds.amazonaws.com","admin","Sunitanaik0497")
cursor= db.cursor()

query="create database UserDetails;"
cursor.execute(query=query)

cursor.execute("use UserDetails;")
query="""
create table Employees
(
	Id INT auto_increment primary key,
    Fname VARCHAR(50) not null,
    Lname VARCHAR(50) not null,
    Emailid VARCHAR(50) not null,
    Phone VARCHAR(15) not null
);
"""
cursor.execute(query=query)

query='insert into Employees (Fname,Lname,Emailid,Phone) values ("Fname","Lname","fname@gmail.com","+91-9834587445");'
cursor.execute(query=query)

cursor.connection.commit()
cursor.close()