# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 21:07:24 2018

@author: Nishan
"""

def b(balance, monthlyPaymentRate, annualInterestRate):
    i = 12
    while i > 0:
        balance = (balance-(balance*monthlyPaymentRate))+((balance-(balance*monthlyPaymentRate))*(annualInterestRate/12))
        i -= 1
    return round(balance,2)
print('Remaining Balance: ',b(balance, monthlyPaymentRate, annualInterestRate))