#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 23:22:36 2017

@author: Zhoukx.joseph
"""

def two_sum(lst,target):
    L={(target-lst[i]):i for i in range(len(lst))}
    I={i:lst[i]for i in range(len(lst))}
    for i in range(len(lst)):
        if I.get(i) in L:
            return (i,L.get(I.get(i)))
        
srt_lst=[-2, 7, 11, 15, 20, 21]
print(two_sum(srt_lst,22))