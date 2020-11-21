import requests
import telebot
from bs4 import BeautifulSoup
import datetime
import time



username = ''
password = ''

url = 'https://isu.ifmo.ru/pls/apex/f?p=2143:LOGIN:111590327276412'
sess = requests.Session()
sess.verify = False

resp = sess.post(url + '/login', data={'username': username, 'password': password})
resp.raise_for_status()

resp = sess.get(url + '/index.html')
resp.raise_for_status()

print(resp)


def parse_schedule_for_day(web_page, day_name):
    soup = BeautifulSoup(web_page, "html5lib")
    schedule_table = soup.find("table", attrs={"id": f"{DAY_NAMES.index(day_name) + 1}day"})
    if schedule_table is None:
        return

    times_list = schedule_table.find_all("td", attrs={"class": "time"})
    times_list = [time.span.text for time in times_list]

    locations_list = schedule_table.find_all("td", attrs={"class": "room"})
    locations_list = [room.span.text for room in locations_list]

    lessons_list = schedule_table.find_all("td", attrs={"class": "lesson"})
    lessons_list = [lesson.text.split('\n\n') for lesson in lessons_list]
    lessons_list = [', '.join([info for info in lesson_info if info])
                    for lesson_info in lessons_list]

    return times_list, locations_list, lessons_list