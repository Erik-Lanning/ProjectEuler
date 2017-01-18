'''
Solution to problem 6 from http://ProjectEuler.net by Erik Lanning, 12/24/2016
'''

upperBound = 100 + 1

sumOfSquares = 0
squareOfSum = 0

for i in range(1, upperBound):
	sumOfSquares += pow(i, 2)
	squareOfSum += i
	
squareOfSum = pow(squareOfSum, 2)

print (squareOfSum - sumOfSquares)
