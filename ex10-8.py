import random

def has_duplicates(listt):
	unique_list = list(set(listt))
	if len(unique_list) < len(listt):
		return True
	else:
		return False


results = []
for i in range(10000):
	listt = []
	for i in range(23):
		listt.append(random.randint(1,365))
	results.append(has_duplicates(listt))

count_true = 0
for i in results:
	if i == True:
		count_true+=1

print count_true
print len(results)
print count_true/float(len(results))

