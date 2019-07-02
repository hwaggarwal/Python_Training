# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 09:28:21 2019

@author: HAggarwal
"""

# =============================================================================
# Assume s is a string of lower case characters.
# 
# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', 
# then your program should print
# 
# Number of times bob occurs is: 2
# =============================================================================

s = 'bobbobobob'
counterbob = 0 # Counts occurences of bob

for i in range(len(s)):
    if s[i: i+3] == 'bob': # The slice goes out of bound
        counterbob += 1

print('Number of times bob occurs is: ' + str(counterbob))
        


