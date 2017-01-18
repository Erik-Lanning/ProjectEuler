'''
Solution to problem 10 from http://ProjectEuler.com by Erik Lanning, 12/24/2016
Used Sieve of Eratosthenes algorithm.
'''
import math

theSum = 0
sieve = {}
bound = 2000000

i = 2

while i < bound:
	sieve[i] = True
	i += 1

for i in range(2, int(math.sqrt(bound))):
	if sieve[i] == True:
		j = i**2
		k = 1
		while j < bound:
			sieve[j] = False
			j = i**2 + k * i
			k += 1

i = 2
while i < bound:
	if sieve[i] == True:
		theSum += i
	i += 1
		
print theSum
