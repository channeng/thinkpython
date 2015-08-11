import datetime
def print_date(date_object):
	print date_object.strftime('Today is %a,  %dth of %b, %Y')

print_date(datetime.date.today())