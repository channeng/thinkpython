import time

with open("words.txt","r") as f:
	start = time.time()
	listt = []
	for i in f:
		listt.append(i)
	end = time.time()

	elapsed_time = end - start
	print elapsed_time

	start2 = time.time()
	listt = []
	for i in f:
		listt = listt + [str(i)]
	end2 = time.time()

	elapsed_time2 = end2 - start2
	print elapsed_time2
