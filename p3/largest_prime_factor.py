'''
Solution to Problem 3 of http://ProjectEuler.net by Erik Lanning, 12/22/2016
'''
		
#Returns a prime larger than num
def nextPrime(num):
	i = 2	
	nextNum = num + 1
	while i != nextNum:
		if (nextNum % i) == 0:
			i = 1
			nextNum += 1
		i += 1
	return nextNum
	
factorize = 600851475143
largestPrime = 2

while factorize > largestPrime:
	while factorize % largestPrime == 0:
		factorize /= largestPrime
	if factorize > largestPrime:
		largestPrime = nextPrime(largestPrime)

print largestPrime
