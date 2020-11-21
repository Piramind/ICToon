import sqlite3
from random import randint

class Order:
    def __init__(self):
        # Подключение к БД
        self.connect = sqlite3.connect("файл базы", check_same_thread=False)

    # Создание нового 
    def create_order(self, user_id):
        random_code = randint(100000, 999999)

        cursor = self.connect.cursor()
        request = "INSERT INTO orders(user_id, random_code) VALUES(?, ?)"
        cursor.execute(request, (user_id, random_code))
        self.connect.commit()

    # Получение элементов запроса
    def get_composition(self, order_id):
        cursor = self.connect.cursor()
        request = f"SELECT composition FROM orders WHERE order_id=?"
        result = cursor.execute(request, (order_id,)).fetchone()
        return result[0]

    # Добавляем данные в список
    def add_to_order(self, order_id, pizza_name):
        all_order = self.get_composition(order_id)

        if all_order is None:
            all_order = f"{pizza_name}"
        else:
            all_order += f" {pizza_name}"

        cursor = self.connect.cursor()
        request = "UPDATE orders SET composition=? WHERE order_id=?"
        cursor.execute(request, (all_order, order_id))
        self.connect.commit()

    # Получаем случайный код для заказа
    def get_random_code(self, order_id):
        cursor = self.connect.cursor()
        request = f"SELECT random_code FROM orders WHERE order_id=?"
        result = cursor.execute(request, (order_id,)).fetchone()
        return result[0]

    # Берём неоплаченный заказ для определенного пользователя
    def get_not_paid_order(self, user_id):
        cursor = self.connect.cursor()
        request = f"SELECT order_id FROM orders WHERE user_id=? AND paid=FALSE"
        result = cursor.execute(request, (user_id,)).fetchone()
        return result[0]