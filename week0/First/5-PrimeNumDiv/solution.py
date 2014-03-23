def is_prime(n):
	n = abs (n)
	sum = 1
	if n ==1:
		return False
	for i in range (1,n):
		if n % i == 0:
			sum += i
	if sum > 2:
		return False
	else:
		return True

def prime_number_of_divisors(n):
	n = abs (n)
	br = 1
	if n == 1:
		return True
	else:
		for i in range (2,n+1):
			if n % i == 0:
				br = br + 1
		return is_prime(br)
