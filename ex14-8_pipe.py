import os
cmd = 'ls'
# Runs in bash and saves the result
fp = os.popen(cmd)

# Retrieve result from var
file_read = fp.read()

# Converts string result into array
file_list= file_read.split("\n")

for i in file_list:
	print i