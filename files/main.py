import styleer
from mess_pars import message_parse
import web_parse
import telebot
import sqlite3

access_token = ''
bot = telebot.TeleBot(access_token)

# Подключаем библиотеку

class User:
    def __init__(self):
        # Создаём соединение с БД
        self.connect = sqlite3.connect("db", check_same_thread=False) # здесь указываем путь к файлу базы
    # Получаем id всех пользователей
    def get_all_id(self):
        cursor = self.connect.cursor()
        request = "SELECT id FROM user"
        result = cursor.execute(request).fetchall()
        return [i[0] for i in result]


    # Добавляем нового пользователя
    def add_id_to_db(self, user_id):
        cursor = self.connect.cursor()
        request = "INSERT INTO user(id, stat) VALUES(?, ?)"
        cursor.execute(request, (user_id, 0))
        self.connect.commit()


     # Получаем статус работы с ботом
    def get_status(self, user_id):
        cursor = self.connect.cursor()
        request = f"SELECT stat FROM user WHERE id=?"
        result = cursor.execute(request, (user_id,)).fetchone()
        return result[0]


    # Изменяем статус работы с ботом
    def set_status(self, user_id, value):
        cursor = self.connect.cursor()
        request = f"UPDATE user SET stat=? WHERE id=?"
        cursor.execute(request, (value, user_id))
        self.connect.commit()


    # Получаем id текущего 
    def get_current_order_id(self, user_id):
        cursor = self.connect.cursor()
        request = f"SELECT current_order_id FROM user WHERE id=?"
        result = cursor.execute(request, (user_id,)).fetchone()
        return result[0]


    # Меняем id текущего 
    def set_current_order_id(self, user_id, value):
        cursor = self.connect.cursor()
        request = f"UPDATE user SET current_order_id=? WHERE id=?"
        cursor.execute(request, (value, user_id))
        self.connect.commit()
        