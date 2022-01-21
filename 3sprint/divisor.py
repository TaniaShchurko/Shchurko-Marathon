def divisor(num):
    check=1
    while(True):
        while check<=num:
            if num % check == 0:
                yield check
            check+=1
        if check > num:
            yield None
            check += 1