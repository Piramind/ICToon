from icalendar import Calendar, Event
from datetime import datetime
from pytz import UTC # timezone

cal = Calendar()
cal.add('prodid', '-//My calendar product//mxm.dk//')
cal.add('version', '2.0')

event = Event()
event.add('summary', 'Информация о курсе опенеду')
event.add('dtstart', datetime(2020,4,4,8,0,0,tzinfo=UTC))
event.add('dtend', datetime(2020,4,4,10,0,0,tzinfo=UTC))
event.add('dtstamp', datetime(2020,4,4,0,10,0,tzinfo=UTC))
event['uid'] = ''
event.add('priority', 5)

cal.add_component(event)

f = open('example.ics', 'wb')
f.write(cal.to_ical())
f.close()