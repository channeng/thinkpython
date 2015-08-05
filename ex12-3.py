def histogram(string):
	hist = {}
	for i in string:
		hist[i] = hist.get(i,0) + 1
	return hist

def sort_dict(string):
	hist = histogram(string)
	dsu = []
	listt = hist.items()
	for letter,count in listt:
		dsu.append((count,letter))

	dsu.sort(reverse=True)
	for i in range(len(dsu)):
		print dsu[i][1],

with open("words.txt") as f:
	for line in f:
		word = line.strip()
		print sort_dict(word)

