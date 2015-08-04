def histogram(word):
	hist = dict()
	for char in word:
		hist[char] = hist.get(char,0)+1
	return hist

hist = histogram("oiawevanp'nwpeaw")

for i in hist:
	print i, hist[i]