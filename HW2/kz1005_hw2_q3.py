#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 20:25:08 2017

@author: Zhoukx.joseph
"""

def factors(num):
    L = []
    for x in range(1,int(num**(1/2))+1):
        if num % x == 0:
            yield x
            if x*x != num:
                L.append(int(num/x))
    for x in reversed(L):
        yield x
for i in factors(100):
    print(i)