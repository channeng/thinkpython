import time

def fibonacci(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
print fibonacci(35)
print time.time()-start