import sys


def concat_files(argv):
    megatron = []
    for index in range(1, len(sys.argv)):
        filename = sys.argv[index]
        file_read = open(filename, "r")
        contents = file_read.read()
        megatron.append(contents)
        file_read.close()
    content = "\n".join(megatron)
    return content
