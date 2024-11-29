import mysql.connector

from tabulate import tabulate

con = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "hari",
    database = "python_db"
    )



def insert(namee,age,city):
    res = con.cursor()
    sql = "insert into users(namee,age,city) values (%s,%s,%s)"
    user = (namee,age,city)
    res.execute(sql,user)
    con.commit()
    
    print("data insert succesfully")

def update(namee,age,city,id):
    res = con.cursor()
    sql = "update users set namee = %s,age = %s, city = %s where id = %s"
    user = (namee,age,city,id)
    res.execute(sql,user)
    con.commit()
    print("data update succesfully")

def select():
    res = con.cursor()
    sql = "select id,namee,age,city from users"
    res.execute(sql)
    data  = res.fetchall()
    #data  = res.fetchone()
    #data  = res.fetchmany(2)
    print(tabulate(data,headers = ["id","namee","age","city"]))

def delete(id):
    res = con.cursor()
    sql = "delete from users where id = %s"
    user = (id,)
    res.execute(sql,user)
    con.commit()
    print("data delete succesfully")

while True:
    print("1 insert data")
    print("2 update data")
    print("3 select data")
    print("4 delete data")
    print("5 exit")
    choice = int(input("enter the choice:"))
    if choice == 1:
        namee = input("enter the name:")
        age = input("enter the age:")
        city = input("enter the city:")
        insert(namee,age,city)

    elif choice == 2:
        id = input("enter the id : ")
        namee = input("enter the name : ")
        age = input("enter the age : ")
        city = input("enter the city : ")
        update(namee,age,city,id)

    elif choice == 3:
        select()

    elif choice == 4:
        id = input("enter the id to delete:")
        delete(id)

    elif choice == 5:
        break

    else:
        print("invalid selection . please tyr again !")





        
