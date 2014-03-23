def is_prime(n):
	n = abs (n)
	count = 1
	if n ==1:
		return False
	for i in range (2,n):
		if n % i == 0:
			count += 1
	if count > 2:
		return False
	else:
		return True
