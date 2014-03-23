def sum_of_digits(n):
	n = abs (n)
	sum = 0
	while n>0:
		number = n % 10
		n=n//10
		sum += number
	return sum
