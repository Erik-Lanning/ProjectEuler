'''
Solution to Problem 5 of http://ProjectEuler.net by Erik Lanning
'''
testNumber = 20
divisorCheck = (19, 17, 13, 11, 15, 12, 16, 14, 18, 20)
bound = len(divisorCheck) - 1
index = 0

while index != bound:
	if testNumber % divisorCheck[index] != 0:
		testNumber = testNumber + 20
		index = 0
		continue
	index += 1

print testNumber
