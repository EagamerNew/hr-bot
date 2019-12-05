# coding=utf-8
# -*- coding: utf-8 -*-
import bs4
import parser
import mysql.connector

# main variables
import telebot
from telebot import types
import requests

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

    def setValueByIndex(self, value, num):
        if num == 1:
            self.name = value
        if num == 2:
            self.surname = value
        if num == 3:
            self.lastname = value
        if num == 4:
            self.birthdate = value
        if num == 5:
            self.idn = value
        if num == 6:
            self.idnumber = value
        if num == 7:
            self.iddate = value
        if num == 8:
            self.idaddress = value
        if num == 9:
            self.city = value
        if num == 10:
            self.address = value
        if num == 11:
            self.cardnumber = value
        if num == 12:
            self.scorenumber = value
        if num == 13:
            self.phone = value
        if num == 14:
            self.email = value

step = 0
user = User()

def get_name(message):
    global user
    user.name = message.text
    print(user.name + " - hello " )
    print(user.chatid)
    bot.send_message(message.chat.id, "Отлично. А теперь напишите Вашу фамилию? На кириллице и с большой буквы.")
    bot.register_next_step_handler(message, get_surname);

def get_surname(message):
    global user
    user.surname = message.text
    print(user)
    bot.send_message(message.chat.id, "Напишите Ваше отчество? На кириллице и с большой буквы.")
    bot.register_next_step_handler(message, get_lastname);

def get_lastname(message):
    global user
    user.lastname = message.text
    bot.send_message(message.chat.id, "Отлично. Напишите Вашу дату рождения? Например: 13.12.1999")
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
    bot.register_next_step_handler(message, get_city);

def get_city(message):
    global user
    user.idaddress = message.text
    bot.send_message(message.chat.id, "Напишите город проживания?")
    bot.register_next_step_handler(message, get_idaddress);

def get_idaddress(message):
    global user
    user.city = message.text
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
    bot.send_message(message.chat.id,
                     "Все ли данные заполнены правильно? Напишите 'да' или 'нет'\n" + user_info_to_string())
    bot.register_next_step_handler(message, check_yes_no);
    # bot.register_next_step_handler(message, accept_user_info);

    

def accept_user_info(message):
    global user
    user.name = message.text
    print(user.name + " HELLO")
    print(user_info_to_string())

def check_yes_no(message):
    global user
    text = message.text.encode('utf-8')
    # bot.register_next_step_handler(message, accept_user_info);
    print(text.lower())

    if str.lower(text)== "да" or text == "Да" or text == "ДА":
        bot.send_message(message.chat.id, "Отлично, " + user.name.encode('utf-8') + ". Ваш запрос принят ожидайте ответа.")
        resp = telegram_bot_sendtext("Добрый день, Айгерим! К нам пожаловал новый сотрудник. Я собрал для Вас его данные: \n" + user_info_to_string())
        print(resp)
        # sql = "INSERT INTO user_info (name, surname,lastname,birthdate,idn,idnumber,iddate,idaddress,city,address,cardnumber,scorenumber,phone,email,chatid) VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        # val = (user.name,user.surname,user.lastname,user.birthdate,user.idn, user.idnumber,user.iddate, user.idaddress,user.city,user.address,user.cardnumber,user.scorenumber,user.phone,user.email, user.chatid)
        # cursordb.execute(sql, val)
        # mydb.commit()
        # print(cursordb.rowcount,"-" ,user.chatid ," record inserted.")
    elif str.lower(text) == "нет" or text == "Нет" or text == "НЕТ" or text == "НЕт":
        bot.send_message(message.chat.id, "Какой пункт нужно изменить? Напишите пункт от 1 до 12")
        bot.register_next_step_handler(message, select_changing_info);
    else:
        bot.send_message(message.chat.id,
                     "Что-то не так... Ответьте 'да' или 'нет'");
        bot.register_next_step_handler(message, check_yes_no);

def select_changing_info(message):
    global user
    global step
    text = message.text.encode('utf-8')
    if not text.isdigit() or int(text)<1 or int(text)>12:
        bot.send_message(message.chat.id,
                     "Что-то не так... Напишите номер пункта от 1 до 12");
        bot.register_next_step_handler(message, select_changing_info);
    else:
        num = int(text)
        if num == 1:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.name.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 1
            bot.register_next_step_handler(message, change_info);
        if num == 2:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.surname.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 2
            bot.register_next_step_handler(message, change_info);
        if num == 3:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.lastname.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 3
            bot.register_next_step_handler(message, change_info);
        if num == 4:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.birthdate.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 4
            bot.register_next_step_handler(message, change_info);
        if num == 5:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.idn.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 5
            bot.register_next_step_handler(message, change_info);
        if num == 6:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.idnumber.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 6
            bot.register_next_step_handler(message, change_info);
        if num == 7:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.iddate.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 7
            bot.register_next_step_handler(message, change_info);
        if num == 8:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.idaddress.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 8
            bot.register_next_step_handler(message, change_info);
        if num == 9:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.city.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 9
            bot.register_next_step_handler(message, change_info);
        if num == 10:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.address.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 10
            bot.register_next_step_handler(message, change_info);
        if num == 11:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.cardnumber.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 11
            bot.register_next_step_handler(message, change_info);
        if num == 12:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.scorenumber.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 12
            bot.register_next_step_handler(message, change_info);
        if num == 13:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные " + user.phone.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 13
            bot.register_next_step_handler(message, change_info);
        if num == 14:
            bot.send_message(message.chat.id,
                     user.name.encode('utf-8') + ", Вы хотите введённые данные  почту " + user.email.encode('utf-8') + "? Тогда распишите более правильный ответ. Я его с удовольствием отредактирую \xE2\x9C\x8C	");
            step = 14
            bot.register_next_step_handler(message, change_info);


def change_info(message):
    global step
    global user
    text = message.text
    user.setValueByIndex(text,step)
    bot.send_message(message.chat.id,
                     "Все ли данные заполнены правильно? Напишите 'да' или 'нет'\n" + user_info_to_string())
    bot.register_next_step_handler(message, check_yes_no);


def user_info_to_string():
    global user
    string = "1. Имя: " + user.name.encode('utf-8') + "\n"
    string += "2. Фамилия: " + user.surname.encode('utf-8') + "\n"
    string += "3. Отчество: " + user.lastname.encode('utf-8') + "\n"
    string += "4. Дата рождения: " + user.birthdate.encode('utf-8') + "\n"
    string += "5. ИИН: " + user.idn.encode('utf-8') + "\n"
    string += "6. Дата получения УЛ: " + user.idnumber.encode('utf-8') + "\n"
    string += "7. Фактический адрес: " + user.iddate.encode('utf-8') + "\n"
    string += "8. Место получения УЛ: " + user.idaddress.encode('utf-8') + "\n"
    string += "9. Город: " + user.city.encode('utf-8') + "\n"
    string += "10. Адрес: " + user.address.encode('utf-8') + "\n"
    string += "11. Номер банковской карты: " + user.cardnumber.encode('utf-8') + "\n"
    string += "12. Номер счёта карты: " + user.scorenumber.encode('utf-8') + "\n"
    string += "13. Контактный номер: " + user.phone.encode('utf-8') + "\n"
    string += "14. Почта: " + user.email.encode('utf-8') + "\n"
    return str(string)

def build_menu(buttons,
               n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu

def telegram_bot_sendtext(bot_message):
    
    bot_token = '1006785313:AAEvXqIWpCSvSH2c_KKcrICPm_0B1jTj9ew'
    bot_chatID = '1041971636'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

# handlers
@bot.message_handler(commands=['start', 'go'])
def start_handler(message):
    global user
    user = User()
    bot.send_message(message.chat.id,
                     "Добро пожаловать в компанию AIVA ONE\nДля начала нужно ответить на несколько вопросов.\nНапишите Ваше имя? Например: Жасулан")
    user.chatid = message.chat.id
    bot.register_next_step_handler(message, get_name);

# @bot.message_handler(content_types=['text'])
# def text_handler(message):
#     global step
#     global cursordb
#     user.chatid = message.chat.id
#     user.name = message.text
#     bot.register_next_step_handler(message, get_name)

bot.polling()
# https://habr.com/ru/post/350648/