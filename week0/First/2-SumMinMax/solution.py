def sum_of_min_and_max(arr):
	Min = arr[0]
	Max = arr[0]
	for item in arr:
		if Min > item:
			Min = item
		if Max < item:
			Max = item
	return Min + Max
