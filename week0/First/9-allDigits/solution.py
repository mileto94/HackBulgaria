def contains_digits(number, digits):
    temp_number = str(number)
    arr_number = []
    br = 0
    for num in temp_number:
        arr_number.append(num)
    for x in digits:
        if str(x) in arr_number:
            br+=1
    if br == len(digits):
        return True
    else:
        return False
