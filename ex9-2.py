# ans = 0.330738

def has_no_e(word):
	for letter in word:
		if letter == 'e':
			return False
	else:
		return True

with open("words.txt","r") as f:
	total = 0
	counter = 0
	for line in f:
		total +=1
		if has_no_e(line):
			counter +=1
	print total
	print counter
	percent = counter/float(total)
	print percent
