#!/usr/bin/python
"""
Without psyco:
Found 25000 primes in 5.770000 seconds
Found 50000 primes in 15.530000 seconds
Found 75000 primes in 28.440000 seconds
Found 100000 primes in 43.810000 seconds

With psyco:
Found 25000 primes in 1.590000 seconds
Found 50000 primes in 4.250000 seconds
Found 75000 primes in 8.130000 seconds
Found 100000 primes in 12.880000 seconds
"""

import time
import sys
from math import sqrt

def isprime(x):
	if x < 2:
		return False
	if x < 4:
		return True
	if x == 5:
		return True
	if x % 2 == 0:
		return False
	if x % 5 == 0:
		return False
	if (x + 1) % 6 != 0:
		if (x - 1) % 6 != 0:
			return False
	lim=sqrt(x)+1
	for y in range(3, int(lim), 2):
		if x % y == 0:
			return False
	return True

def genprime(max):
	count = 0
	current = 1
	while count<max:
		if isprime(current):
			count = count + 1
		current = current + 1

def main():
	"""
	try:
		import psyco
		psyco.full()
	except ImportError:
		pass
	"""
	start=int(sys.argv[1])
	stop=int(sys.argv[2])+1
	for x in range(start, stop, start):
		begin = time.clock()
		genprime(x)
		end = time.clock()
		duration = end - begin
		print 'Found %(count)d primes in %(time)f seconds' % {'count': x, 'time': duration}

if __name__ == "__main__":
	main()

