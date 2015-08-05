from string import punctuation
from string import maketrans

def rm_punct(stringg,chars):
	return stringg.translate(maketrans("",""),chars)

def histogram(listt):
	hist = {}
	for word in listt:
		for i in word:
			hist[i]=hist.get(i,0)+1
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

print "Total number of words in book = %s" %(len(book_array))

histo= histogram(book_array)
keys = histo.keys()
hist_list= []

for key in keys:
	hist_list.append((histo[key],key))
print hist_list

hist_list.sort(reverse=True)
for count,letter in hist_list:
	print letter,count
