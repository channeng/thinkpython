def sumall(*args):
	listt = []
	for i in args:
		listt =listt+[i]
	return sum(listt)

print sumall(2,3,5,6,7,7,43)