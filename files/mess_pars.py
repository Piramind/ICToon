import requests
import telebot
from bs4 import BeautifulSoup
import datetime
import time
from web_parse import parse_schedule_for_day
from web_parse import get_page

access_token = '952672295:AAF4aqUSI5s0lPNkrDw1KkYvxm-cf3VpP38'
bot = telebot.TeleBot(access_token)

daynames = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

@bot.message_handler(commands=daynames)
def message_parse(message):
    trip = message.text.split()
    trip[0].lower()
    trip[0] = trip[0][1:]
    if trip[0] in daynames:       # в этом операторе надо реализовать поиск даты
        answer = parse_schedule_for_day(trip[0], trip[1], trip[2])
        bot.send_message(message.chat.id, answer, parse_mode='HTML')

    elif trip[0] == 'tomorrow':
        tmrw_day = datetime.date.today().weekday() + 1
        if tmrw_day == 7:
            tmrw_day = 0
        tmrw_day = daynames[tmrw_day]
        answer = parse_schedule_for_day(trip[0],trip[1], trip[2])
        bot.send_message(message.chat.id, answer, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, 'Я сломалься')
        print(trip)
"""
    elif message[0] == 'near':
        _, group = message.text.split()
        current_day = datetime.date.today().weekday()
        if current_day == 7:
            current_day = 0

        web_page = get_page(group)
        not_found = True
        today = True
        while not_found:
            if today:
                today = False
                schedule_for_day = parse_schedule_for_day(web_page, daynames[current_day])
                if schedule_for_day is None:
                    continue
                else:
                    times_lst, locations_lst, lessons_lst = schedule_for_day
                    now_time = time.strptime(time.strftime('%H:%M'), '%H:%M')
                    for time_comarison in range(len(times_lst)):
                        if now_time < time.strptime(times_lst[time_comarison].split('-')[0], '%H:%M'):
                            bot.send_message(message.chat.id, f'Nearest lesson today at:{times_lst[time_comarison]}\n'
                                                            f'Lesson: {lessons_lst[time_comarison]} at'
                                                            f' {locations_lst[time_comarison]}')
                            not_found = False
                            break
            else:
                current_day += 1
                if current_day == 7:
                    current_day = 0
                schedule_for_day = parse_schedule_for_day(web_page, daynames[current_day])
                if schedule_for_day is None:
                    continue
                else:
                    times_lst, locations_lst, lessons_lst = schedule_for_day
                    bot.send_message(message.chat.id, f'Nearest lesson on {daynames[current_day].capitalize()} at:'
                                                    f'{times_lst[0]}\n'
                                                    f'Lesson: {lessons_lst[0]} in '
                                                    f'{locations_lst[0]}')
                    not_found = False
    else:
        return None
"""
    # предлагаю заменить на вызов следующей функции с аргументами[date, odd, group], максимум с возвратом кода успеха

if __name__ == '__main__':
    bot.polling(none_stop=True)