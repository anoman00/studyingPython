
number = input('Insert a number such that the primes after it can be generated:' )
def genPrime():
    p = number
    yield p
    while True:
        p += 1
        k = p - 1
        while k > 1:
            if p % k != 0:
                k -= 1
            else:
                p += 1
                k = p-1 #why does k need to be reset? Shouldnt it reset when while True loop resets? 
        else:
            yield p