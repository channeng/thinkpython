from string import punctuation
from string import maketrans
from random import choice

def rm_punct(stringg,chars):
	return stringg.translate(maketrans("",""),chars)

def histogram(listt):
	hist = {}
	for word in listt:
		hist[word]=hist.get(word,0)+1
	return hist

with open("ebook.txt","r") as f:
	book_array = []
	for i,l in enumerate(f):
		pass
	book_length = i+1

with open("ebook.txt","r") as f:
	book_array = []
	for count in range(book_length):
		line_array = rm_punct(f.readline().strip().lower(),punctuation).split(" ")
		if len(line_array) == 1:
			pass
		else:
			book_array = book_array + line_array

total_words = len(book_array)
print "Total number of words in book = %s" %(total_words)

markov = {}
for i in range(total_words-3):
	markov[book_array[i],book_array[i+1]] = markov.get((book_array[i],book_array[i+1]),[])+[book_array[i+2]]

first_word = choice(book_array)
second_word = choice(book_array)
print first_word,second_word,
def print_sentence(book_array,first_word,second_word,rept):
	if rept > 0:
		try:
			next_word = choice(markov[first_word,second_word])
			print next_word,
			print_sentence(book_array,second_word,next_word,rept-1)
		except KeyError:
			next_word = choice(markov[choice(book_array),choice(book_array)])
			print next_word,
	else:
		pass

print_sentence(book_array,"the","one",100)