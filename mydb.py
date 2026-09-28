# from sys import executable
#
# import mysql.connector

# con=mysql.connector.connect(user="root",password="root",host="localhost")
#    #establish connection between python code and mysql server
#     #it returns a connection object
# print(con)
#
#
#
# c=con.cursor()  # cursor object used to execute sql queries/command
#
# #c.execute(command)
# #create database file
#
# c.execute("create database school_db")
# print("Database file created")

# con=mysql.connector.connect(user="root",password="root",host="localhost",database="school_db")
# c=con.cursor()
# c.execute('''
# create table student(roll_no int not null primary key,
#                                       name varchar(20),
#                                       age int,
#                                       place varchar(20),
#                                       phone int,
#                                       total_mark int)
#                                       ''')
# print("table created successfully")

# c.execute('''insert into student(roll_no,name,age,place,phone,total_mark)
#                          values(101,"Arun",12,"kollam",345678909,145),
#                                (102,"Sai",14,"ktym",456789987,129),
#                                (103,"Nikhil",11,"Kochi",456750982,178),
#                                (104,"Anu",15,"idukki",345698145,156)
#                         ''');
# con.commit()     #to save data permanently inside db
# print("data entered")


# query ="insert into student(roll_no,name ,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)"
# data=(106,"kiran",12,"ekm","345678908",140)
#
# c.execute(query,data)
# con.commit()
# print("data entered")

## to display data in terminal##

# query="select * from student"
# c.execute(query)

# records=c.fetchall()
# if records:
#     for row in records:
#         print(row)
# else:
#     print("no records found")


#read all attributes of a student with roll_number=roll number entered by user

# number=int(input("enter roll number:"))
# query="select * from student where roll_no=%s"
# data=(number,)
# c.execute(query,data)
# record=c.fetchone()
# if record:
#     print(record)
# else:
#     print("no record found")

#update mark of student with roll number =roll number entered by user

# number=int(input("enter roll number:"))
# up_mark=int(input("entre new mark:"))
# query="update student set total_mark=%s where roll_no=%s "
# data=(up_mark,number)
# c.execute(query,data)
# con.commit()
# print("updated")

##delete a record with roll number= roll number entered by user

# number=int(input("enter roll number:"))
# query="delete from student where roll_no=%s"
# data=(number,)
# c.execute(query,data)
# con.commit()
# print("deleted")

# #create a new record using values entered by user
# roll=int(input("enter roll number:"))
# name=input("enter name:")
# age=int(input("enter age:"))
# place=input("enter place:")
# phone=input("enter ph_number:")
# mark=int(input("enter new_mark:"))
# query="insert into student(roll_no,name,age,place,phone,total_mark)values(%s,%s,%s,%s,%s,%s)"
# data=(roll,name,age,place,phone,mark)
# c.execute(query,data)
# con.commit()
# print("new record entered")


