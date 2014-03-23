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

def prime_factorization(n):
	answer=[]
	arr=[]
	for i in range (1,n+1):
		if is_prime(i)==True:
			arr.append(i)

	count=0

	for item in arr:
		if n%item==0:
			count+=1
			for i in range(2,n):
				p=item**i
				if n%p==0:
					count+=1

			answer.append((item,count))
		else:

			count=0

	return answer
