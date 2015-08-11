class Time(object):
	"""Represents the time of day.
	attributes: hour, minute, second
	"""

def hrs_in_secs(hours):
	return hours*60*60

def mins_in_secs(mins):
	return mins*60

def increment(t1,seconds):
	sum_time = hrs_in_secs(t1.hour) + mins_in_secs(t1.minute) + t1.second + seconds
	incremented_time = Time()
	incremented_time.hour = sum_time/3600
	incremented_time.minute = sum_time%3600/60
	incremented_time.second = sum_time%3600%60
	return incremented_time

def print_time(time_object):
	print "%.2d:%.2d:%.2d" %(time_object.hour,time_object.minute,time_object.second)


t1 = Time()
t1.hour = 1
t1.minute = 2
t1.second = 30

print_time(t1)
print_time(increment(t1,35933))