def cat2(file_to_read):
    file = open(file_to_read, "r")
    contents = file.read().split("\n")  # Makes lines together which were separeted by new lines
    file.close()
    contents = "\n".join(contents) + "\n"  # Prints out every line on new line
    return contents
