#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 22:03:30 2017

@author: Zhoukx.joseph
"""

def split_parity(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst.append(lst[i])
            count +=1
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            lst.append(lst[i])
            count +=1
    for i in range(count):
        lst[i]=lst.pop()
    return lst
L=[1,2,3,4,5,6,7,9,10,10,11]

def split_parity2(lst):
    n=len(lst)
    for i in range(n):
        if lst[i]%2==0:
            lst.append(lst[i])
    for i in range(n):
        if lst[i]%2!=0:
            lst.append(lst[i])
    for i in range(n):
        lst[i]=lst.pop()
    return lst
print(split_parity2(L))