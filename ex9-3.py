def avoids(word,forbd_letters):
	for i in forbd_letters:
		for letter in word:
			if letter == i:
				return False
	else:
		return True

with open("ex9-2words.txt") as f:
	forbd_letters = raw_input("Please enter forbidden letters in a string \n > ")
	total =0
	counter =0
	for line in f:
		word= line.strip()
		total +=1
		if avoids(word,forbd_letters):
			counter +=1
			print word
	percent =counter/float(total)
	print percent