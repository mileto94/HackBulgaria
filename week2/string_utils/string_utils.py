def lines(text):
	result = []
	new_text = text.split("\n")
	for line in new_text: 
		result.append(line)

	return result

def unlines(elements):
	result_new_elements = map(str, elements)
	new = "\n".join(result_new_elements)
	
	return new

def words(text):
	new_text = text.split(" ")
	return new_text

def unwords(text):
	return " ".join(text)
	
def tabs_to_spaces(text):
	new_str = text.replace("\t","    ")
	return new_str
