import string

with open("words.txt","r") as f:
	words = []
	for line in f:
		word = line.strip()
		words = words + [word.lower()]
	for i in words:
		print i
