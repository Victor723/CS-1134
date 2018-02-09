#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:41:18 2017

@author: Zhoukx.joseph
"""

def fibs(n):
    i = 0
    q = 1
    count = 0
    while count < n:
        c = i+q
        i = q
        q = c
        count+=1
        yield i

for i in fibs(9):
    print(i)