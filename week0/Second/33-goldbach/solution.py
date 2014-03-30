def is_prime(n):
    n = abs(n)
    count = 1
    if n == 1:
        return False
    for i in range(2, n + 1):
        if n % i == 0:
            count += 1
    if count > 2:
        return False
    return True


def goldbach(n):
    result = []
    arr = list(x for x in range(2, n) if is_prime(x))
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] + arr[j] == n:
                temp_tuple = (arr[i], arr[j])
                result.append(temp_tuple)
    return result
