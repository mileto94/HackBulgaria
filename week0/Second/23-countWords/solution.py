def count_words(arr):
	count=1
	array={}
	for item in arr:
		if item in array:
			array[item]+=1
		else:
			array[item]=1
	return array
