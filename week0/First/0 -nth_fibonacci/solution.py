# 1 1 2 3 5 8 13 21...
def nth_fibonacci(n):
	a = 1
	b = 1
	index = 2
	while index < n:
		next = a + b
		a = b
		b = next
		index = index + 1
	return b


