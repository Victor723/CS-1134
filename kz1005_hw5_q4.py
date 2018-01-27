#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:29:11 2017

@author: Zhoukx.joseph
"""

class Empty(Exception):
    pass

class ArrayStack:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

    def is_empty(self):
        return len(self) == 0

    def push(self, val):
        self.data.append(val)

    def top(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data[-1]

    def pop(self):
        if (self.is_empty()):
            raise Empty("Stack is empty")
        return self.data.pop()

class MaxStack:
# the storage is different from the entering number, so some modifications are made
# to the push, pop, and top methods.
# if the entering number is "3 1 4 6"
# the storage in the stack would be "3 1 7(3+4) 10(6+4)", if the value is higher
# than the max, then will store value+max, and assign max=value
# Similar situation for methods pop and top
    def __init__(self):
        self.s=ArrayStack()
        self.m=None
    
    def __len__(self):
        return len(self.s)

    def is_empty(self):
        return len(self.s) == 0

    def push(self, val):
        if len(self.s)==0:
            self.s.push(val)
            self.m=val
        elif self.m>val:
            self.s.push(val)
        else:
            self.s.push(val+self.m)
            self.m=val

    def top(self):
        if self.s.is_empty():
            raise Empty('Stack is Empty')
        if self.s.top()>self.m:
            return self.m
        else:
            return self.s.top()

    def pop(self):
        if self.s.is_empty():
            raise Empty('Stack is Empty')
        if self.top()<self.m:
            return self.s.pop()
        else:
            temp=self.m
            self.m=self.s.pop()-self.m
            return temp
    def max(self):
        if self.s.is_empty():
            raise Empty('Stack is Empty')
        return self.m






