def uses_all(word,uses_letters):
	for i in uses_letters:
		for letter in word:
			if letter == i:
				break
		else:
			return False
	else:
		return True

with open("ex9-2words.txt") as f:
	uses_letters = raw_input("Please enter uses_letters in a string \n > ")
	total =0
	counter =0
	for line in f:
		word= line.strip()
		total +=1
		if uses_all(word,uses_letters):
			counter +=1
			print word
	percent =counter/float(total)
	print percent
	