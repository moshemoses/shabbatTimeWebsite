import datetime, json

date_plus_time = '2019-01-04 16:30:00+02:00'
print(date_plus_time)
date_obj = datetime.datetime.strptime(date_plus_time, '%Y-%m-%d %H:%M:%S')
print(date_obj)
event_date = date_obj.strftime('%A %B %d, %Y')
print(event_date)
event_time = date_obj.strftime('%I:%M %p')
print(event_time)
