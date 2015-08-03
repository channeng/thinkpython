
def bisect(word,listt,index_posit):
	length = len(listt)
	mid = length/2
	if listt[mid] == word:
		return index_posit
	else:
		new_list = sorted([word,str(listt[mid])])
		print "%s %s %s" %(index_posit,word,new_list)
		if new_list[0] == word:
			index_posit -= mid
			bisect(word,listt[0:mid],index_posit)
		else:
			index_posit += mid
			bisect(word,listt[(mid+1):length],index_posit)


with open("words.txt","r") as f:
	listt = []
	for line in f:
		word = line.strip()
		listt.append(word)

print bisect("give",listt,len(listt))
print listt[82181]

