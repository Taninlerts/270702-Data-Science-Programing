# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:19:27 2021

@author: ASUS
"""

def largestNumber(a):
    maxlen = len(str(max(a)))
    if all(b == 0 for b in a):
        return '0'
    return ''.join(sorted((str(b) for b in a), reverse=True,
                      key=lambda i: i*(maxlen * 2 // len(i))))
x = largestNumber(list(int(x) for x in input("Enter the digits :\t").split()))
print ("the largest formed number is", x)