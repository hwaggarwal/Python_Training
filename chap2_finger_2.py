# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 13:56:05 2019

@author: HAggarwal
"""

# =============================================================================
# s is a string which contains decimal numbers. Print sum of numbers in s
# =============================================================================

s = '1.23, 2.4, .123'

s = s+','
value = ''
num = 0
for i in range(len(s)):    
    if (s[i] != ','):
        value += s[i]
    else:
        num = num + float(value)
        value = ''
       
print('The sum of numbers in', s, ':', str(num))
    