# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 14:40:28 2019

@author: HAggarwal
"""

x = 25
epsilon = 0.01
step = 1
guess = 0.0

while guess <= x:
    if abs(guess**2 -x) < epsilon:
        break
    else:
        guess += step

if abs(guess**2 - x) >= epsilon:
    print('failed')
else:
    print('succeeded: ' + str(guess))
    

