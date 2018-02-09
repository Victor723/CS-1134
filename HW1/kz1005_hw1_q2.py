#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:26:52 2017

@author: Zhoukx.joseph
"""

def shift(lst, k, str="left"):#set the default value of str == "left"
    '''This function shift the element from the left
to the right handside of the list, or from the right to the left.
para k is the number of the elements that're going to be shift,
para str defines the direction of the shift'''
    if str == "left":
        for i in range(k):
            lst.append(lst[0])
            del lst[0]
        return lst
    if str == "right":
        for i in range(len(lst)-k):
            lst.append(lst[0])
            del lst[0]
        return lst

L=[1,2,3,4,5,6]
print(shift(L,2))#test the function