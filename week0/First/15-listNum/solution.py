def list_to_number(digits):
	n=0
	digits=digits[::-1]
	for i in range(0,len(digits)):
		n+= digits[i]*(10**i)
	return n
