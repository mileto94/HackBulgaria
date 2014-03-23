def number_to_list(n):
	arr = []
	num = 0
	while n>0:
		num = n % 10
		arr.append(num)
		n = n//10
	arr=arr[::-1]
	return arr
