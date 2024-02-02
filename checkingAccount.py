def check(numbers):
    checking = 0
    inc = 1

    try:
        if len(numbers) > 9:
            return None
        else:
            for i in range(9, 0, -1):
                add = numbers[i - 1] * inc
                checking += add
                inc += 1

            checking %= 11
            if checking == 0:
                checking = "OK"
                return checking
            elif checking != 0:
                return "ERR"
    except TypeError as e:
        return "ILL"
    
