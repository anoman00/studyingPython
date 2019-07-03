# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:08:32 2018

@author: Nisha
This calculates minimum monthly payment required to 
pay off balance within 1 year with interest.
"""

m = (round((balance*(annualInterestRate/12))/10))*10
def b(balance, m, annualInterestRate):
    i = 12
    while i > 0:
        balance = (balance-m)+((balance-m)*(annualInterestRate/12))
        i -= 1
    return balance
def minn(balance, annualInterestRate, m):
    if b(balance, m, annualInterestRate) <= 0:
        return m
    else:
        return minn(balance, annualInterestRate, 10+m)
print('Lowest Payment: ',minn(balance, annualInterestRate, m))