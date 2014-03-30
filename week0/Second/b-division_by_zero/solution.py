def count_numbers(numbers):
    result = numbers
    for i in range(len(result)):
        for index in range(i + 1, len(result)):
            if result[i] > result[index]:
                num = result[i] // result[index]
            else:
                num = result[index] // result[i]
            if num not in result and num != 0:
                result.append(num)
            if result[len(result) - 1] > result[i]:
                n = result[len(result) - 1] // result[i]
            else:
                n = result[i] // result[len(result) - 1]
            if n not in result and n != 0:
                result.append(n)
    return len(result)
