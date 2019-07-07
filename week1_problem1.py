# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 08:51:44 2019

@author: HAggarwal
"""

# =============================================================================
# Assume s is a string of lower case characters.
# 
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:
#     Number of vowels: 5
# =============================================================================

s = 'azbobobegghakl'
numofVow = 0

for char in s:
    if char in 'aeiou':
        numofVow += 1
        
print('Number of vowels: ' + str(numofVow))

