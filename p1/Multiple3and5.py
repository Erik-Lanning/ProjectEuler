'''
For Project Euler.net, problem one by Erik Lanning 12/20/2016
'''

upperBound = 1000

sum = 0
for i in range(1, upperBound):
	if (i % 3 == 0) or (i % 5 == 0):
		sum += i
print sum