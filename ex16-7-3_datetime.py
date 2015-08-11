import datetime

def strfdelta(time_delta, formatt):
    d = {"days": time_delta.days}
    d["hours"], rem = divmod(time_delta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return formatt.format(**d)

def double_day(bday1,bday2):
	bboy1=datetime.datetime.strptime(bday1,'%d-%m-%Y')
	bboy2=datetime.datetime.strptime(bday2,'%d-%m-%Y')
	Dday_diff = abs(bboy1-bboy2)*2
	Dday = min(bboy1,bboy2)+Dday_diff
	print "Double Day = "+str(datetime.datetime.strftime(Dday,'%d-%m-%Y'))
	print "Boy 1 will be %s old and Boy 2 will be %s old" %(Dday-bboy1,Dday-bboy2)

double_day('23-04-1965','21-10-1991')
