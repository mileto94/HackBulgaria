import sys

def read_and_write(sys.argv[1],sys.argv[2]):
	file_to_read = sys.argv[1]
	file = open(file_to_read, "r")
	content = file.read()
	result = content.replace("\t","    ")
	file_to_write = sys.argv[2]
	second = open(file_to_write,"w")
	content2 = second.write(result)
	return True
	