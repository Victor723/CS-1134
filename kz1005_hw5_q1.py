#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 09:21:51 2017

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

class Queue:
    def __init__ (self):#two ArrayStack objects
        self.s=ArrayStack()
        self.p=ArrayStack()
    def enqueue(self,elem):
        self.s.push(elem)
    def __len__(self):
        return len(self.s)+len(self.p)
    def dequeue(self):
        if len(self)==0:
            raise Empty("Queue is empty")
        if self.p.is_empty():#only when p is empty, pop element from s to p.
            while self.s.is_empty()==False:
                self.p.push(self.s.pop())
        return self.p.pop()#first in first out.

    def first(self):
        if len(self)==0:
            raise Empty("Queue is empty")
        if self.p.is_empty():
            while self.s.is_empty()==False:
                return self.s.top()
        return self.p.top()
