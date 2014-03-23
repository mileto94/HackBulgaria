def groupBy(func, seq):
	dic={}
	for i in seq:
		if func (i) in dic:
			dic[func(i)].append(i)
		else:
			dic[func(i)]=[i]

	return dic
