def sum_numbers(filename):
    file_read = open(filename)
    contents = file_read.read().split(" ")
    numbers = map(int, contents)
    file_read.close()
    return sum(numbers)
