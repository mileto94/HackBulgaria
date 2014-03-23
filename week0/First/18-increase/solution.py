def is_increasing(seq):
	br = 0

	for i in range(0,len(seq)-1):
		if seq[i] < seq[i+1]:
			br += 1

	if br +1== len(seq):
		return True
	else:
		return False
