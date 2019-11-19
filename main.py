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

step = 1
user = User()

# handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    bot.send_message(message.chat.id,
                     "Добро пожаловать в компанию AIVA ONE\nДля начала нужно ответить на несколько вопросов.\nНапишите Ваше имя?")

@bot.message_handler(content_types=['text'])
def text_handler(message):
    global step
    global cursordb
    text = message.text
    chat_id = message.chat.id
    textString = text
    if step == 1:
        user.name = textString
        bot.send_message(chat_id, "Отлично. А теперь напишите Вашу фамилию?")
        step = step + 1
    if step == 2:
        user.surname = textString
        bot.send_message(chat_id, "Напишите Ваше отчество?")
        step = step + 1
    if step == 3:
        user.lastname = textString
        bot.send_message(chat_id, "Напишите Вашу дату рождения?")
        step = step + 1
    if step == 4:
        user.birthdate = textString
        bot.send_message(chat_id, "Напишите Ваш ИИН?")
        step = step + 1
    if step == 5:
        user.idn = textString
        bot.send_message(chat_id, "Напишите номер удостоверения личности?")
        step = step + 1
    if step == 6:
        user.idnumber = textString
        bot.send_message(chat_id, "Напишите дату получения удостоверения личности?")
        step = step + 1
    if step == 7:
        user.iddate = textString
        bot.send_message(chat_id, "Напишите место получения удостоверения личности?")
        step = step + 1
    if step == 8:
        user.idaddress = textString
        bot.send_message(chat_id, "Напишите фактически адрес проживания?")
        step = step + 1
    if step == 9:
        user.address = textString
        bot.send_message(chat_id, "Напишите номер банковской карты?")
        step = step + 1
    if step == 10:
        user.cardnumber = textString
        bot.send_message(chat_id, "Напишите номер счёта карты?")
        step = step + 1
    if step == 11:
        user.scorenumber = textString
        bot.send_message(chat_id, "Напишите Ваш контактный номер?")
        step = step + 1
    if step == 12:
        user.phone = textString
        bot.send_message(chat_id, "Напишите адрес электронной почты?")
        step = step + 1
    if step == 13:
        user.email = textString
        bot.send_message(chat_id, "Отлично, " + user.name + ". Ваш запрос принят ожидайте ответа.")
        sql = "INSERT INTO user_info (name, surname,lastname,birthdate,idn,idnumber,iddate,idaddress,city,address,cardnumber,scorenumber,phone,email) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (user.name,user.surname,user.lastname,user.birthdate,user.idn, user.idnumber,user.iddate, user.idaddress,user.city,user.address,user.cardnumber,user.scorenumber,user.phone,user.email, chat_id)
        cursordb.execute(sql, val)
        mydb.commit()
        print(cursordb.rowcount,"-" + chat_id + " record inserted.")
        # step = step + 1


bot.polling()
