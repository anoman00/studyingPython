# -*- coding: utf-8 -*-
"""
Created on Sun Jul  1 01:30:22 2018

@author: Nishan
"""

for iteration in range(5):
    count = 0
    while True:
        for letter in "hello, world":
            count += 1
        print("Iteration " + str(iteration) + "; count is: " + str(count))