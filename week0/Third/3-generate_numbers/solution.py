from random import randint


def generate_numbers(filename, n):
    result = []
    while n != 0:
        result.append(randint(1, 1000000))
        n -= 1
    file = open(filename, "w")
    random_string_numbers = map(str, result)
    contents = " ".join(random_string_numbers)
    file.write(contents)
    file.close()
    return contents
