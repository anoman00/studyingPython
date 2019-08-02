# -*- coding: utf-8 -*-
"""
Calculates remaining balance after interest paid
"""

def b(balance, monthlyPaymentRate, annualInterestRate):
    i = 12
    while i > 0:
        balance = (balance-(balance*monthlyPaymentRate))+((balance-(balance*monthlyPaymentRate))*(annualInterestRate/12))
        i -= 1
    return round(balance,2)
print('Remaining Balance: ',b(balance, monthlyPaymentRate, annualInterestRate))