def unique_words_count(arr):
	count=0
	array={}
	for item in arr:
		if item in array:
			array[item]+=1

		else:
			array[item]=1
	for key in array:
		if key!="":
			count+=1
	return count
