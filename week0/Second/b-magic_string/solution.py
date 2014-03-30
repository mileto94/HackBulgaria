def magic_string(S):
    count = 0
    left_part = S[:len(S) // 2]
    right_part = S[len(S) // 2:]
    for index in range(len(left_part)):
        if left_part[index] != '>':
            count += 1
        if right_part[index] != '<':
            count += 1
    return count
