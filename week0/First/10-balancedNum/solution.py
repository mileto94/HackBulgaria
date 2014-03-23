def is_number_balanced(n):
	num=0
	arr=[]
	if n>=0 and n<10:
		return True
	else:
		while n>0:
			num=n%10
			arr.append(num)
			n=n//10
		mid=len(arr)//2
		avL=0
		for i in arr[:mid]:
			avL+=i
		avR=0
		if len(arr)%2==0:
			for i in range(mid,len(arr)):
				avR+=arr[i]
		else:
			for i in range(mid+1,len(arr)):
				avR+=arr[i]
		if avR==avL:
			return True
		else:
			return False
