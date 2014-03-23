def count_substrings(haystack, needle):
	br=0
	for item in haystack:
		br = haystack.count(needle)
	return br
