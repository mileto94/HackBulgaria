def read_from_file(file_to_read):
    file_read = open(file_to_read, "r")
    content = file_read.read()
    file_read.close()
    return content
