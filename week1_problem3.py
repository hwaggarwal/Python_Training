# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:58:21 2019

@author: HAggarwal
"""

# =============================================================================
# Assume s is a string of lower case characters.
# 
# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print
# 
# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. 
# For example, if s = 'abcbcd', then your program should print
# 
# Longest substring in alphabetical order is: abc
# =============================================================================

s = 'abcacd'
temp = ''
len_counter = 0
final = ''

for i in range(len(s)-1):
    temp = s[i]
    while s[i+1]>= s[i]:
        temp += s[i+1]
        i += 1
        if i == (len(s) -1):
            break
    if len(temp) > len(final):
        final = temp
print('Longest substring in alphabetical order is: ' + final)
        