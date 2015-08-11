import datetime

def strfdelta(time_delta, formatt):
    d = {"days": time_delta.days}
    d["hours"], rem = divmod(time_delta.seconds, 3600)
    d["minutes"], d["seconds"] = divmod(rem, 60)
    return formatt.format(**d)

def time_to_birthday():
	birthday = raw_input("When were you born? (dd-mm-yyyy) \n")
	birthdate = datetime.datetime.strptime(birthday, "%d-%m-%Y")
	print datetime.datetime.strftime(birthdate,"Your birthday is on %d/%m/%Y")
	age = datetime.datetime.now()-birthdate
	print strfdelta(datetime.timedelta(seconds = datetime.timedelta.total_seconds(age)),"{days} days {hours}:{minutes}:{seconds}")

time_to_birthday()