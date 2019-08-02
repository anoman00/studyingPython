# -*- coding: utf-8 -*-
"""
This calculates minimum monthly payment required to 
pay off balance within 1 year with interest 
much faster using bisection.
"""

m_ub = (balance*(1+(annualInterestRate/12))**12)/12.0
m_lb = balance/12
def b(balance, m, annualInterestRate):
    i = 12
    while i > 0:
        balance = (balance-m)+((balance-m)*(annualInterestRate/12))
        i -= 1
    return balance
def minimum(balance, annualInterestRate, m_ub, m_lb):
    m_avg = (m_ub + m_lb)/2
    if round(b(balance, m_avg, annualInterestRate),2) == 0:
        return round(m_avg,2)
    elif round(b(balance, m_avg, annualInterestRate),2) > 0:
        m_lb = m_avg
        return minimum(balance, annualInterestRate, m_ub, m_lb)
    else:
        m_ub = m_avg
        return minimum(balance, annualInterestRate, m_ub, m_lb)
print('Lowest Payment: ',minimum(balance, annualInterestRate, m_ub, m_lb))