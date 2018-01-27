#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:23:44 2017

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

class ArrayDeque:
    INITIAL_CAPACITY=10
    def __init__(self):
        self.data = [None] * ArrayDeque.INITIAL_CAPACITY
        self.num = 0
        self.front = 0

    def __len__(self):
        return self.num

    def is_empty(self):
        return self.num==0

    def first(self):
        if self.is_empty():
            raise Empty("Dequeue is empty")
        return self.data[self.front]

    def last(self):
        if self.is_empty():
            raise Empty("Dequeue is empty")
        back = (self.front+self.num-1)%len(self.data)
        return self.data[back]

    def add_first(self,elem):
        if (self.num == len(self.data)):
            self.resize(2 * len(self.data))
        avail = (self.front-1) % len(self.data)
        self.data[avail] = elem
        self.front = (self.front-1)%len(self.data)
        self.num+=1
    
    def add_last(self,elem):
        if (self.num == len(self.data)):
            self.resize(2 * len(self.data))
        avail = (self.num + self.front) % len(self.data)
        self.data[avail]=elem
        self.num+=1

    def delete_first(self):
        if self.is_empty():
            raise Empty("Dequeue is empty")
        value = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front+1)%len(self.data)
        self.num-=1
        if(self.num < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value
    def delete_last(self):
        if self.is_empty():
            raise Empty("Dequeue is empty")
        back = (self.front+self.num-1)%len(self.data)
        value=self.data[back]
        self.data[back]=None
        self.num-=1
        if(self.num < len(self.data) // 4):
            self.resize(len(self.data) // 2)
        return value
    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front
        for new_ind in range(self.num):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front = 0

class MidStack():
    def __init__(self):
        self.s=ArrayStack()
        self.d=ArrayDeque()
    def is_empty(self):
        return len(self.d)==len(self.s)==0
    def __len__ (self):
        return len(self.d)+len(self.s)
    def push(self,other):#if the length of the MidStack object is even
        if len(self)%2==0:#push element from dequeue to stack
            self.d.add_last(other)#add_last works the same as push
            self.s.push(self.d.delete_first())
        else:
            self.d.add_last(other)
    def top(self):
        if self.is_empty():
            raise Empty("MidStack is empty")
        if self.d.is_empty():
            return self.s.top()
        else:
            return self.d.last()
    def pop(self):
        if self.is_empty():
            raise Empty("MidStack is empty")
        if not self.d.is_empty():
            if len(self)==2:
                return self.d.delete_first()
            elif len(self)%2==1:
                self.d.add_first(self.s.pop())#To coorperate with the mid_push method,
            return self.d.delete_last()#this specific condition was made.
        else:
            return self.s.pop()
    def mid_push(self,other):
        self.d.add_first(other)
        if len(self)%2==1:
            self.s.push(self.d.delete_first())