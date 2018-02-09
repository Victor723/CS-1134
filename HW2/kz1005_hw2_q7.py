#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 13:18:17 2017

@author: Zhoukx.joseph
"""

def findChange(lst):
    start = 0
    end = len(lst)-1
    result = False
    while result == False:
        if lst[int(round((start+end)/2))]==0:
            if lst[int(round((start+end+1)/2))]==1:
                return int(round((start+end+1)/2))
            start+=int(round((start+end)/2))
        else:
            if lst[int(round((start+end-1)/2))]==0:
                return int(round((start+end)/2))
            end-=int(round((start+end)/2))

L=[0,0,1,1,1,1]
