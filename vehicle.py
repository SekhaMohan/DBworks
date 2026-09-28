#define a class to perform database operations on Vehicle table
#create a class named VehicleListCreatRetrieveUpdateDelete and define methods
#list()---->for reading all records
#create()--->for creating new record
#retrieve(id)--->for reading a specific record
#update(id,data)--->for updating specific record
#delete(id)--->for deleting a specific record

import mysql.connector

class VehicleListCreatRetrieveUpdateDelete:
    def __init__(self):
        self.connection=mysql.connector.connect(
            user="root",password="root",host="localhost",database="vehicle_db")
        print(self.connection)
        self.cursor = self.connection.cursor()
        print("successfully connected")
    def list(self):
        query="select * from vehicle"
        self.cursor.execute(query)
        records = self.cursor.fetchall()
        if records:
            for row in records:
                print(row)
        else:
            print("no records found")
    def create(self,brand,model,type,price,year):
        query="insert into vehicle(brand,model,type,price,year) values(%s,%s,%s,%s,%s)"
        data = (brand,model,type,price,year)
        self.cursor.execute(query, data)
        self.connection.commit()
        print("data inserted successfully")
    def retrieve(self,id):
        query = "select * from vehicle where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        record = self.cursor.fetchone()
        if record:
            print(record)
        else:
            print("no records found")
    def update(self,brand,model,type,price,year,id):
        query = "update vehicle set brand=%s,model=%s,type=%s,price=%s,year=%s where id=%s"
        data = (brand, model, type, price, year, id)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("data is updated")
        else:
            print("id not found")
    def delete(self,id):
        query = "delete from vehicle where id=%s"
        data = (id,)
        self.cursor.execute(query, data)
        self.connection.commit()
        if self.cursor.rowcount > 0:
            print("data is deleted")
        else:
            print("data not found")
book_instance=VehicleListCreatRetrieveUpdateDelete()
#book_instance.list()
#book_instance.create("tata","nexon","SUV",140000,2024)
#book_instance.retrieve(2)
#book_instance.update("honda","city","sedan",150000,2023,1)
book_instance.delete(2)
