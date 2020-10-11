import time
from datetime import date,datetime,timedelta


FORMATO_DATA="%Y-%m-%d"
FORMATO_DATA_IT="%d/%m/%Y"
FORMATO_DATA_ORA="%Y-%m-%d %H:%M:%S"
FORMATO_DATA_ORA_NOMEFILE="%Y-%m-%d_%H-%M-%S"
FORMATO_DATA_ORA_NOSPAZI="%Y%m%d%H%M%S"
FORMATO_ORA="%H:%M:%S"


def now():
	return datetime.now()
def today():
	return date.today()

def getsecs():
	return int(time.time())
def getmillis():
	return int(time.time()*1000)

#
# conversioni
#
def date_to_string(data=None,formato=None):
	if(data is None):
		data=now()
	if(formato is None):
		formato=FORMATO_DATA_ORA
	return data.strftime(formato)

def string_to_date(stringa,formato):
	return datetime.strptime(stringa,formato)
def secondi_to_date_string(secondi,formato):
	return time.strftime(formato, time.gmtime(secondi))

#
# operazioni
#
def is_datetime(dataora):
	return type(dataora) is datetime

def date_diff(d1,d2):
	return abs(d2 - d1)

def plus_days(data,days_to_add):
	return data + timedelta(days=days_to_add)
def minus_days(data,days_to_subtract):
	return data - timedelta(days=days_to_subtract)

def set_start_of_day(data):
	return data.replace(hour=0, minute=0, second=0, microsecond=0)
def set_end_of_day(data):
	return data.replace(hour=23, minute=59, second=59, microsecond=999999)
