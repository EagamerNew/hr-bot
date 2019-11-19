# coding=utf-8
import bs4
import parser
import mysql.connector

# main variables
import telebot

TOKEN = "1006785313:AAEvXqIWpCSvSH2c_KKcrICPm_0B1jTj9ew"
bot = telebot.TeleBot(TOKEN)
mydb = mysql.connector.connect(
  host="91.201.214.132",
  user="alysu",
  passwd="123",
  database="friday"
)
cursordb = mydb.cursor()

class User:
    name = ""
    surname = ""
    lastname = ""
    birthdate = ""
    idn = ""
    idnumber = ""
    iddate = ""
    idaddress = ""
    city = ""
    address = ""
    cardnumber = ""
    scorenumber = ""
    phone = ""
    email = ""
    chatid = ""

step = 0
user = User()

def get_name(message):
    global user
    user.name = message.text
    print(user.name + " HELLO")
    bot.send_message(message.chat.id, "Отлично. А теперь напишите Вашу фамилию?")
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global user
    user.surname = message.text
    print(user)
    bot.send_message(message.chat.id, "Напишите Ваше отчество?")
    bot.register_next_step_handler(message, get_lastname);

def get_lastname(message):
    global user
    user.lastname = message.text
    bot.send_message(message.chat.id, "Напишите Вашу дату рождения?")
    bot.register_next_step_handler(message, get_birthdate);

def get_birthdate(message):
    global user
    user.birthdate = message.text
    bot.send_message(message.chat.id, "Напишите Ваш ИИН?")
    bot.register_next_step_handler(message, get_idn);

def get_idn(message):
    global user
    user.idn = message.text
    bot.send_message(message.chat.id, "Напишите номер удостоверения личности?")
    bot.register_next_step_handler(message, get_idnumber);

def get_idnumber(message):
    global user
    user.idnumber = message.text
    bot.send_message(message.chat.id, "Напишите дату получения удостоверения личности?")
    bot.register_next_step_handler(message, get_iddate);

def get_iddate(message):
    global user
    user.iddate = message.text
    bot.send_message(message.chat.id, "Напишите место получения удостоверения личности?")
    bot.register_next_step_handler(message, get_idaddress);

def get_idaddress(message):
    global user
    user.idaddress = message.text
    bot.send_message(message.chat.id, "Напишите фактически адрес проживания?")
    bot.register_next_step_handler(message, get_address);

def get_address(message):
    global user
    user.address = message.text
    bot.send_message(message.chat.id, "Напишите номер банковской карты?")
    bot.register_next_step_handler(message, get_cardnumber);

def get_cardnumber(message):
    global user
    user.cardnumber = message.text
    bot.send_message(message.chat.id, "Напишите номер счёта карты?")
    bot.register_next_step_handler(message, get_scorenumber);

def get_scorenumber(message):
    global user
    user.scorenumber = message.text
    bot.send_message(message.chat.id, "Напишите Ваш контактный номер?")
    bot.register_next_step_handler(message, get_phone);

def get_phone(message):
    global user
    user.phone = message.text
    bot.send_message(message.chat.id, "Напишите адрес электронной почты?")
    bot.register_next_step_handler(message, get_email);

def get_email(message):
    global user
    global mydb
    global cursordb
    user.email = message.text
    # bot.register_next_step_handler(message, get_surname);
    bot.send_message(message.chat.id, "Отлично, ",user.name,". Ваш запрос принят ожидайте ответа.")
    sql = "INSERT INTO user_info (name, surname,lastname,birthdate,idn,idnumber,iddate,idaddress,city,address,cardnumber,scorenumber,phone,email,chatid) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (user.name,user.surname,user.lastname,user.birthdate,user.idn, user.idnumber,user.iddate, user.idaddress,user.city,user.address,user.cardnumber,user.scorenumber,user.phone,user.email, user.chatid)
    cursordb.execute(sql, val)
    mydb.commit()
    print(cursordb.rowcount,"-" ,user.chatid ," record inserted.")


# handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    global user
    bot.send_message(message.chat.id,
                     "Добро пожаловать в компанию AIVA ONE\nДля начала нужно ответить на несколько вопросов.\nНапишите Ваше имя?")
    user.chatid = message.chat.id
    bot.register_next_step_handler(message, get_name);

# @bot.message_handler(content_types=['text'])
# def text_handler(message):
#     global step
#     global cursordb
#     user.chatid = message.chat.id
#     user.name = message.text
#     bot.register_next_step_handler(message, get_name);

bot.polling()
