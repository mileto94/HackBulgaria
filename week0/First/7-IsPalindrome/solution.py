def is_int_palindrome(n):
	arr=[]
	flag=False
	num=0
	if n>=0 and n<10:
		flag = True
	elif n>=10:
		while n!=0:
			num=n%10
			n=n//10
			arr.append(num)
	b=arr[::-1]
	for i in range (0,len(arr)):
		if arr[i]==b[i]:
			flag=True
		else:
			flag=False
	return flag
