def sevens_in_a_row(arr, n):
	if n==1:
		for item in arr:
			if item==7:
				return True
			else:
				return False
	br=1
	flag=False
	for i in range(0,len(arr)-1):
		if arr[i]==7:
			if arr[i]==arr[i+1]:
				br+=1
				if br>=n:
					flag = True
					break
			else:
				br=1
	return flag
