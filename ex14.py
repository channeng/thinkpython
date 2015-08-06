def write_file(filename,string):
	string = str(string)
	with open(filename,"w") as f:
		f.write(string)

write_file("my_first_log.txt",1232343)