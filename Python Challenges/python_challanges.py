'''
try
Question 1
Level 1

Question:
Write a program which can compute the factorial of a given numbers.
'''
def factorial(x):
  k = 1
  for i in range(1, x+1):
    k = i * k
  return k

'''
Question:
Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number.

'''
def listOrTuple():
    numbers = input('Provide Numbers separated by commas:')
    list = numbers.split(',')
    try:
        for i in list:
            int(i)
    except ValueError:
        print('Not Numbers')
        return listOrTuple()
    return tuple(list)

'''
Question:
Write a program which accepts a string of any length and removes all the duplicate characters

'''


def del_repeats(x):
    dict = {}
    for i in x:
        dict[i] = 0
    for i in x:
        dict[i] += 1
    list = []
    for i in dict:
        if dict[i] == 1:
            list.append(i)
    return ''.join(list)