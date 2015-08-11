class Time(object):
	"""Represents the time of day.
	attributes: hour, minute, second
	"""

def hrs_in_secs(hours):
	return hours*60*60

def mins_in_secs(mins):
	return mins*60

def is_after(t1,t2):
	t1_time = hrs_in_secs(t1.hour)+mins_in_secs(t1.minute)+t1.second
	t2_time = hrs_in_secs(t2.hour)+mins_in_secs(t2.minute)+t2.second
	return t1_time>t2_time

t1 = Time()
t1.hour = 1
t1.minute = 2
t1.second = 30

t2 = Time()
t2.hour = 1
t2.minute = 2
t2.second = 3

print is_after(t1,t2)