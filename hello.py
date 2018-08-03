# -*- coding: utf-8 -*-
"""
Created on Thu Jun 28 22:10:30 2018

@author: Nishan
"""

print('Please think of a number between 0 and 100!')
low = 0
high = 100
ans = int((high + low)/2.0)
print('Is your secret number ',ans)
i = input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.: ')
while i == 'h' or i == 'l' or i == 'c' or i != 'h' or i != 'l' or i !='c':
    if i == 'h':
        high = ans
        ans = int((high + low)/2.0)
        print('Is your secret number ',ans)
        i = input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.: ')
    elif i == 'l':
        low = ans
        ans = int((high + low)/2.0)
        print('Is your secret number ',ans)
        i = input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.: ')
    elif i == 'c':
        print('Game over. Your secret number was: ',ans)
        break
    else:
        print('Sorry, I did not understand your input.')
        print('Is your secret number ',ans)
        i = input('Enter h to indicate the guess is too high. Enter l to indicate the guess is too low. Enter c to indicate I guessed correctly.: ')