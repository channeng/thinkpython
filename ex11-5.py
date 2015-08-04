import time

memo = {0:0,1:1}

def fibonacci(n,memo):
	try:
		return memo[n]
	except KeyError:
		new= fibonacci(n-1,memo) + fibonacci(n-2,memo)
		memo[n]=new
		return new

start = time.time()
print fibonacci(90,memo)
print time.time()-start