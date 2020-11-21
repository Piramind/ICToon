import requests
import telebot
from bs4 import BeautifulSoup
import datetime
import time
from web_parse import parse_schedule_for_day

access_token = ''
bot = telebot.TeleBot(access_token)

daynames = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

@bot.message_handler(content_type=['text'])
def message_parse(message):
    message = message.split(' ')
    message[0].upper()
    if message[0] in daynames:       # в этом операторе надо реализовать поиск даты
        parse_schedule_for_day(message[0],message[1], message[2])
    elif message[0] == 'tomorrow':
        pass
    elif message[0] == 'near':
        pass
    elif message[0] == 'дата хз хз':
        pass
    else:
        return 'ошибка ввода лох'
    return *args   # предлагаю заменить на вызов следующей функции с аргументами[date, odd, group], максимум с возвратом кода успеха
