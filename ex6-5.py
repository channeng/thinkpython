import time

def ack(m,n):
	if m == 0:
		return n+1
	if m > 0:
		if n == 0:
			return ack(m-1,1)
		if n > 0:
			return ack(m-1,ack(m,n-1))

start = time.time()
print ack(4,2)
print time.time()-start