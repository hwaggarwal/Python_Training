# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 12:00:10 2019

@author: HAggarwal
"""

#User is asked to enter an integer and prints two integers
# root and pwr, such that 0 < pwr < 6 and root**pwr = integer (by the user)

#Should do the problem again.

num = int(input('Please enter an integer: '))
root = 0
pwr = 1

while root**pwr < num:
    root += 1
    pwr = 1
    while pwr < 6:
        if root**pwr == num:
            break
        pwr += 1
    if root**pwr == num and pwr < 6:
        break
    else:
        pwr = 1

if root**pwr == num:
    print('Root =', root, ', Power =', pwr )
else:
    print('This number cannot be converted into roots and powers')
    
