def anagram(word,uses_letters):
	if len(word) == len(uses_letters):
		if len(list(set(uses_letters.lower()))) == len(list(set(word.lower()))):
			unique_list = {}
			for i in list(set(uses_letters.lower())):
				unique_list[i] = 0
				for l in uses_letters:
					if l == i:
						unique_list[i] +=1

			unique_list_word = {}
			for i in list(set(word.lower())):
				unique_list_word[i] = 0
				for l in word:
					if l == i:
						unique_list_word[i] +=1

			for i in unique_list:
				try: 
					if unique_list[i] != unique_list_word[i]:
						# print "%s don't match %s" %(unique_list[i],unique_list_word[i])
						return False
				except KeyError:
					# print "The letter %s cannot be found in %s" %(i,word)
					return False
			else:
				return True
		else:
			# print "unique_list length don't match"
			return False
	else:
		# print "words length don't match"
		return False

with open("ex9-2words.txt") as f:
	uses_letters = raw_input("Please enter uses_letters in a string \n > ")
	total =0
	counter =0
	for line in f:
		word= line.strip()
		total +=1
		if anagram(word,uses_letters):
			counter +=1
			print word
	percent =counter/float(total)
	print percent