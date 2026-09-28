# Create a database named shop
#
# Create a table `Product` with the following fields:
#
#  `product_id` – Primary Key
#  `name`
#  `brand`
#  `category`
#  `price`
#  `stock`
#
# Write a menu-driven Python program using MySQL with the following options:
#
# text
# 1. Insert Product details
# 2. Read all Product details
# 3. Search a Product by product_id
# 4. Update the stock of a Product
# 5. Delete a Product record
# 6. Exit

from sys import executable

import mysql.connector

con=mysql.connector.connect(user="root",password="root",host="localhost")
print(con)
c=con.cursor()
#c.execute("create database shop")
con=mysql.connector.connect(user="root",password="root",host="localhost",database="shop")
c=con.cursor()
# c.execute('''
# create table product(product_id int not null primary key,
#                                       name varchar(20),
#                                       brand varchar(30),
#                                       category varchar(40),
#                                       price int,
#                                       stock int)
#                                       ''')
# print("table is created successfully")

def insert():
    product_id=int(input("enter the id:"))
    name=input("enter the name:")
    brand=input("enter the brand:")
    category=input("enter the category:")
    price=int(input("enter the price:"))
    stock=int(input("enter the stock:"))
    query="insert into product(product_id,name,brand,category,price,stock) values(%s,%s,%s,%s,%s,%s)"
    data=(product_id,name,brand,category,price,stock)
    c.execute(query,data)
    con.commit()
    print("data inserted")

def get():
    query="select * from product"
    c.execute(query)
    records=c.fetchall()
    if records:
        for row in records:
            print(row)
    else:
        print("no records found")

def search():
    product_id = int(input("enter the id:"))
    query = "select * from product where product_id=%s"
    data = (product_id,)
    c.execute(query, data)
    record = c.fetchone()
    if record:
        print("record found")
    else:
        print("No record found")

def update():
    product_id=int(input("enter the id:"))
    stock=int(input("enter the new_stock:"))
    query="update product set stock=%s where product_id=%s"
    data=(stock,product_id,)
    c.execute(query,data)
    con.commit()
    print("updated")

def delete():
    product_id = int(input("enter the id:"))
    query = "delete from product where product_id=%s"
    data=(product_id,)
    c.execute(query,data)
    con.commit()
    print("deleted")
while (True):
    print("displayed details")
    print("1.Insert Product ")
    print("2. Read all Product details")
    print("3. Search a Product by product_id")
    print("4. Update the stock of a Product")
    print("5. Delete a Product record")
    print("6. Exit")
    choice=int(input("enter the choice:"))
    if choice==1:
        insert()
    elif choice==2:
        get()
    elif choice==3:
        search()
    elif choice==4:
        update()
    elif choice==5:
        delete()
    else:
        exit()



