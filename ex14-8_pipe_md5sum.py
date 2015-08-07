import os

filename = "words.txt"
cmd = 'md5 '+filename
# Runs in bash and saves the result
fp = os.popen(cmd)

'''Retrieve result from var 
--> Result is always a string object'''
file_read = fp.read()

print file_read