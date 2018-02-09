#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 14:28:00 2017

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

class Dequeue:
    INITIAL_CAPACITY=10
    def __init__(self):
        self.data = [None] * Dequeue.INITIAL_CAPACITY
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
        self.data[self.front] = None
        self.front = (self.front+1)%len(self.data)
        self.num-=1
        if(self.num < len(self.data) // 4):
            self.resize(len(self.data) // 2)
    def delete_last(self):
        if self.is_empty():
            raise Empty("Dequeue is empty")
        back = (self.front+self.num-1)%len(self.data)
        self.data[back]=None
        self.num-=1
        if(self.num < len(self.data) // 4):
            self.resize(len(self.data) // 2)
    
    def resize(self, new_cap):
        old_data = self.data
        self.data = [None] * new_cap
        old_ind = self.front
        for new_ind in range(self.num):
            self.data[new_ind] = old_data[old_ind]
            old_ind = (old_ind + 1) % len(old_data)
        self.front = 0
p={}
s1=ArrayStack()
s2=ArrayStack()
while True:
    d=[]
    n=input('-->')
    if n=='done()':
        break
    for a in n.split():
        if a.isalpha():
            if a in p:
                s2.push(p[a])
            else:
                d.append(a)
        if a.isdigit():
            s1.push(a)
            continue
        op1,op2=s1.pop(),s1.pop()
        if a == '+':
            s1.push(int(op2) + int(op1))
        elif a == '-':
            s1.push(int(op2) - int(op1))
        elif a == '*':
            s1.push(int(op2) * int(op1))
        elif a == '/':
            s1.push(int(op2) / int(op1))
        else:
            continue
    if len(d)==1:
        d.append(int(s1.top()))
        p[d[0]]=d[1]
    if len(d)==0 or len(d)>2:
        print(s1.pop())
    elif len(d)==1 and d[0] in p:
        print(p[d[0]])
    else:
        print(d[0])
    continue
            