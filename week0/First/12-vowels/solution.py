def count_vowels(string):
	string=string.lower()
	br=0
	letters = ["a", "e", "y", "u", "i", "o"]
	for letter in string:
		if letter in letters:
			br += 1
	return br
