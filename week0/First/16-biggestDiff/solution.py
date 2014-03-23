def biggest_difference(arr):
	min = arr[0]
	max = arr[0]
	for item in arr:
		if item < min:
			min = item
	for item in arr:
		if item > max:
			max = item

	return min-max
