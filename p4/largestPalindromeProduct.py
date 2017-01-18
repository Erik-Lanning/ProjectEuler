'''
Solution to problem 3 from http://ProjectEuler.net by Erik Lanning, 12/23/2016
'''
def isPalindrome(num1, num2):
	palindrome = True
	stringProduct = str(num1 * num2)
	length = len(stringProduct)
	
	i = 0
	if length == 0:
		while i < length / 2:
			if ( stringProduct[i] != stringProduct[-1*(i+1)] ):
				return False
			i += 1
	else:
		while i != length / 2:
			if ( stringProduct[i] != stringProduct[-1*(i+1)] ):
				return False
			i += 1
	return palindrome

currPalindrome = 0
for i in range(1,1000):
	for j in range(1,1000):
		if isPalindrome(i, j):
			if currPalindrome < i * j:
				currPalindrome = i * j
				
print currPalindrome
