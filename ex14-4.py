import os

def write_file(filename,string1,string2):
	string1 = str(string1)
	string2 = str(string2)
	with open(filename,"w") as f:
		f.write(string1+"\n")
		f.write(string2)

filename = "my_first_log.txt"
string1 = os.getcwd()
string2 = os.listdir(string1)

write_file(filename,string1,string2)