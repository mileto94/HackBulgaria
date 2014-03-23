def is_an_bn(word):
	w=word.lower()
	mid=len(w)//2

	if w=='':
		return True
	elif len(w)%2 != 0 or w[0]!="a":
		return False
	else:
		for i in range(mid):
			if w[i]!="a":
				return False
			else:
				for i in range(mid,len(w)):
					if w[i]!="b":
						return False
					else:
						return True
