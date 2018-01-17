


def IPadd():
	from flask import request
	rover = request.environ['HTTP_X_FORWARDED_FOR']
	return rover


def get_data():
	import requests, json, datetime
	#grabs your latitude, longitude and Time zone
	current_year = datetime.datetime.now().strftime('%Y')
	loc_request=requests.get('http://ip-api.com/json')
	type(loc_request)
	loc_request.status_code==requests.codes.ok
	loc_request_json_data = loc_request.text
	Location_info = json.loads(loc_request_json_data)



	# your location data

	longi = str(Location_info['lon'])
	latit = str(Location_info['lat'])
	city = Location_info['city']
	region = Location_info['timezone']

	
	#using your location data to get customized shabbos data
	#link is for master heb cal calendar api
	heb_cal_address='http://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year='+current_year+'&month=x&ss=on&mf=on&c=on&geo=pos&latitude=['+latit+']&longitude=['+longi+']&tzid=['+region+']&m=50&s=off'

	#begin main loop

	
	import time, requests, datetime, json
	res = requests.get(heb_cal_address)
	ready = json.loads(res.text)
	data = ready.get('items')
	return data, city
	#beginning of main while loop that should hold until candles followed by havdala
    

def parse_data(data):
	import requests, json, datetime
	for i in range(0, len(data)):
		if data[i].get('category') == 'candles' or data[i].get('category') == 'havdalah':
			date_retrival= data[i].get('date')
			date_retrival2 = date_retrival.split('T')
			time = date_retrival2[1].split('-')
			date_plus_time = date_retrival2[0] +" "+ time[0]
			date_obj = datetime.datetime.strptime(date_plus_time, '%Y-%m-%d %H:%M:%S')
			event_date = date_obj.strftime('%A %B %d, %Y')
			event_time = date_obj.strftime('%I:%M %p')
			event_type = data[i].get('category')
			if date_obj >= datetime.datetime.now():
				return event_date, event_time, event_type, date_obj
			

def return_candletime_string():
	import datetime
	info = get_data()
	candletime = parse_data(info[0])
	city = info[1]
	event_type = candletime[2]
	event_date = candletime[0]
	event_time = candletime[1]
	if event_type == 'candles':
		event_type = "Candle lighting"
	elif event_type == "havdalah":
		event_type = "Havdalah"
	else:
		event_type = "Event"
	return event_type +  " in " + city + " on " + event_date + " will be at " + event_time


def time_remaining():
	import datetime
	info = get_data()
	candletime = parse_data(info[0])
	date_obj = candletime[3]
	time_remain = date_obj - datetime.datetime.now()
	time_remain1 = str(time_remain).split(" ")
	days_remain = time_remain1[0]
	hours_mins_remain = time_remain1[2].split(":")
	hours_remain = hours_mins_remain[0]
	minutes_remain = hours_mins_remain[1]
	return "You have " + days_remain + " days, " + hours_remain + " hours, and " + minutes_remain +" minutes to go"

	






	
"""
	
				

def timetil():
	#grabs your latitude, longitude and Time zone
	import requests, json, datetime
	current_year = datetime.datetime.now().strftime('%Y')
	loc_request=requests.get('http://ip-api.com/json')
	type(loc_request)
	loc_request.status_code==requests.codes.ok
	loc_request_json_data = loc_request.text
	Location_info = json.loads(loc_request_json_data)



	# your location data
	longi = str(Location_info['lon'])
	latit = str(Location_info['lat'])
	city = Location_info['city']
	region = Location_info['timezone']
	



	#using your location data to get customized shabbos data
	#link is for master heb cal calendar api
	heb_cal_address='http://www.hebcal.com/hebcal/?v=1&cfg=json&maj=on&min=on&mod=on&nx=on&year='+current_year+'&month=x&ss=on&mf=on&c=on&geo=pos&latitude=['+latit+']&longitude=['+longi+']&tzid=['+region+']&m=50&s=off'

	#begin main loop
	
	import json, requests, datetime, time
	from subprocess import call
	res = requests.get(heb_cal_address)
	ready = json.loads(res.text)
	data = ready.get('items')
	#beginning of main while loop that should hold until candles followed by havdala
    

	for i in range(0, len(data)):
		if data[i].get('category') == 'candles' or data[i].get('category') == 'havdalah':
       		date_retrival = data[i].get('date')
       		date_retrival2 = date_retrival.split('T')
			time = date_retrival2[1].split('-')
			date_plus_time = date_retrival2[0] +" "+ time[0]
			date_obj = datetime.datetime.strptime(date_plus_time, '%Y-%m-%d %H:%M:%S')
			if date_obj >= datetime.datetime.now():
				time_remain = date_obj - datetime.datetime.now()
				time_remain1 = str(time_remain).split(" ")
				days_remain = time_remain1[0]
				hours_mins_remain = time_remain1[2].split(":")
				hours_remain = hours_mins_remain[0]
				minutes_remain = hours_mins_remain[1]

				return "You have " + days_remain + " days, " + hours_remain + " hours, and " + minutes_remain +" minutes to go"
 
 print(time_stmt)
 print(timetil)

 """