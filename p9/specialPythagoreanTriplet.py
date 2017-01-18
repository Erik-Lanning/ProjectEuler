'''
Solution to problem 9 from http://ProjectEuler.net by Erik Lanning, 12/24/2016
'''
import math

weakUpperBound = 999

product = 0
for a in range(1, weakUpperBound):
	for b in range(1, weakUpperBound):
		c = 1000 - a - b
		if c == math.sqrt(a ** 2 + b ** 2):
			product = a * b * c

print product
