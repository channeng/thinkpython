def middle(word):
	word = list(word)
	middle = []
	for i in range(len(word)-2):
		middle.append(word.pop(1))
	return "".join(middle)

print middle("proper")