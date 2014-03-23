def count_consonants(string):
	br=0
	new_string = string.lower()
	consonants = ['q','w','r','t','p','s','d','f','g','h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
	for letter in new_string:
		if letter in consonants:
			br+=1
	return br
