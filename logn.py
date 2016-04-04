import time
from random import randint


def b_search(v, x, l, r):
	while l <= r:
		m = (l+r)/2
		if v[m] == x:
			return m
		elif v[m] < x:
			l = m+1
		else:
			r = m-1
	return -1


start_time = time.time()
v = []
for x in range(0,10000000):
  v.append(x)
b_search(v, randint(0, 10000000), 0, 9999999)
print("--- %s seconds ---" % (time.time() - start_time))