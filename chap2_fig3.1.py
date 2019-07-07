# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 11:39:55 2019

@author: HAggarwal
"""

#Find ube root of a perfect cube

x = int(input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
    ans = ans + 1
    
if ans**3 != abs(x):
    print('This is not a perfect cube')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x,  'is', ans )
