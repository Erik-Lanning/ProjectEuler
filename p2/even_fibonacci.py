'''
Problem 2 from ProjectEuler.net by Erik Lanning, 12/20/2016
'''

cap = 4000000

sum = 0
ithTerm = 1
jthTerm = 0
kthTerm = 0
while ithTerm <= cap:
	if ithTerm % 2 == 0:
		sum += ithTerm
	kthTerm = jthTerm
	jthTerm = ithTerm
	ithTerm = jthTerm + kthTerm
	
print sum