def collatz(number):
    if number == 1:
        return number
    elif number % 2 == 1:
        return collatz(3*number + 1)
    else:
        return collatz(number//2)

def collatz_while(number):
    while number != 1:
        if number % 2 == 1:
            number = 3*number + 1
        else:
            number = number // 2
    return number