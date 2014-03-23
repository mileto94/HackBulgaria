def member_of_nth_fib_lists(listA, listB, needle):
	A = listA
	B = listB
	index = 2
	result = [A,B]
	#make fibonacci sequence
	while index < 7:
		temp = A + B
		A = B
		B = temp
		index = index + 1
		result.append(temp)
	#check if needle is part of fibonacci sequence
	if needle in result:
		return True
	return False
