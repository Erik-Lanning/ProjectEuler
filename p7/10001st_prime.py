'''
Solution to problem 7 from http://ProjectEuler.net by Erik Lanning, 12/24/2016
'''
import math

def isPrime(num):
	i = 2
	while i != num:
		if num % i == 0:
			return False
		i += 1
	return True

primeTerm = 1
primeNumber = 2
upperBound = 10001

while primeTerm != upperBound:
	primeNumber += 1
	while not isPrime(primeNumber):
		primeNumber += 1
	primeTerm += 1
		
print primeNumber
