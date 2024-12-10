def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    elif first == 0:
        return 1
    else:
        return int(str_number)


result1 = get_multiplied_digits(40203)
print(result1)

result2 = get_multiplied_digits(402030)
print(result2)