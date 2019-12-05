# coding=utf-8

import mysql.connector

mydb = mysql.connector.connect(
  host="91.201.214.132",
  user="alysu",
  passwd="123",
  database="friday"
)
cursordb = mydb.cursor()

class User:
    name = "123"
    surname = "123"
    lastname = "123"
    birthdate = "312"
    idn = "312"
    idnumber = ""
    iddate = ""
    idaddress = ""
    city = ""
    address = ""
    cardnumber = ""
    scorenumber = ""
    phone = ""
    email = ""
    chatid = "111"

def selectAll():
    global cursordb
    sql = "SELECT * FROM user_info;"
    # val = (user.name,user.surname,user.lastname,user.birthdate,user.idn, user.idnumber,user.iddate, user.idaddress,user.city,user.address,user.cardnumber,user.scorenumber,user.phone,user.email, user.chatid)
    cursordb.execute(sql)
    myresult = cursordb.fetchall()
    for x in myresult:
        print(x, " - ")

def insertData():
    global mydb
    user = User()
    sql = "INSERT into user_info(name, surname,lastname,birthdate,idn,idnumber,iddate,idaddress,city,address,cardnumber,scorenumber,phone,email,chatid) VALUES(%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (user.name,user.surname,user.lastname,user.birthdate,user.idn, user.idnumber,user.iddate, user.idaddress,user.city,user.address,user.cardnumber,user.scorenumber,user.phone,user.email, user.chatid)
    cursordb.execute(sql, val)
    mydb.commit()
    print(cursordb.rowcount,"-" ,user.chatid ," record inserted.")
# insertData()
selectAll()