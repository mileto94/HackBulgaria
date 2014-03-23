def nth_fib_lists(listA, listB, n):
	A = listA
	B = listB
	if n==1:
		return A
	else:
		index = 2
		while index < n:
			next = A + B
			A = B
			B = next
			index = index + 1
		return B

