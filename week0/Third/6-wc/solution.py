def count_characters(file_to_read):
    file_read = open(file_to_read, "r")
    contents = file_read.read()
    count_chars = 0
    for content in contents:
        count_chars += 1
    file_read.close()
    return count_chars

def count_words(file_to_read):
    file_read = open(file_to_read, "r")
    contents = file_read.read()
    contents = contents.replace("\n\n", " ")
    count_words = 0
    for content in contents:
        if content == " " or content == "\n" or content == "\t":
            count_words += 1
    file_read.close()
    return count_words

def count_lines(file_to_read):
    file_read = open(file_to_read, "r")
    contents = file_read.read().split("\n")
    file_read.close()
    return len(contents)
