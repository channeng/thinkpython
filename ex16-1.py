class Time(object):
	"""Represents the time of day.
	attributes: hour, minute, second
	"""

time = Time()
time.hour = 1
time.minute = 2
time.second = 3

def print_time(Time_object):
	print "%.2d:%.2d:%.2d" %(Time_object.hour,Time_object.minute,Time_object.second)

print_time(time)