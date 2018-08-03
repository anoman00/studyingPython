# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 23:06:28 2018

@author: Nishan
Euclidean Algorithm done iteratively and recursively
"""
def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    gcd = min(a, b)
    while a % gcd != 0 or b % gcd != 0:
        gcd -= 1
    return gcd

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if max(a,b) % min(a,b) == 0:
        return min(a,b)
    else:
        return gcdRecur(min(a,b), (max(a,b) % min(a,b)))
    