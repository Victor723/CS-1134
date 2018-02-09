#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 26 21:39:17 2017

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
def isint(n):
    try:
        n = int(n)
        return True
    except ValueError:
        return False
def isfloat(n):
    try:
        n = float(n)
        return True
    except ValueError:
        return False
d={}# A dictionary to store the value of variables
s=ArrayStack()# A stack to store the different results
while True:
    n = input('-->')#Please enter integers (positive or negative doesn't matter).
    if 'done()' in n:#enter 'done()'to stop the program
        break
    lst=n.split()#split the string to detect whether isalpha or isdigit
    if len(lst)==1:# specical condition when only one number of variable is enter
        if isint(lst[0]) or isfloat(lst[0]):
            print(lst[0])
        else:
            print(d[lst[0]])
        continue
    if lst[0].isalpha() and lst[1]=='=':#Special condition when enter " variable = "
        for i in range(2,len(lst)):# start the loop from the third element
            if isint(lst[i]):
                s.push(int(lst[i]))
                continue
            elif isfloat(lst[i]):
                s.push(float(lst[i]))
                continue
            elif lst[i].isalpha():
                s.push(d[lst[i]])
                continue
            op1,op2=s.pop(),s.pop()
            if lst[i] == '+':
                s.push(op2 + op1)
            elif lst[i] == '-':
                s.push(op2 - op1)
            elif lst[i] == '*':
                s.push(op2 * op1)
            elif lst[i] == '/':
                s.push(op2 / op1)
            elif lst[i] == '%':
                s.push(op2 % op1)
            elif lst[i] == '**':
                s.push(op2 ** op1)
            elif lst[i] == '//':
                s.push(op2 // op1)
            else:
                continue
        d[lst[0]]=s.pop()#if only "variable = num" is entered, it can also do the assignment
        print(lst[0])#because the loop starts from the third element, and only implement only once in this case
        continue

    else:
        for i in range(len(lst)):
            if isint(lst[i]):
                s.push(int(lst[i]))
                continue
            elif isfloat(lst[i]):
                s.push(float(lst[i]))
                continue
            elif lst[i].isalpha():
                s.push(d[lst[i]])
                continue
            op1,op2=s.pop(),s.pop()
            if lst[i] == '+':
                s.push(op2 + op1)
            elif lst[i] == '-':
                s.push(op2 - op1)
            elif lst[i] == '*':
                s.push(op2 * op1)
            elif lst[i] == '/':
                s.push(op2 / op1)
            elif lst[i] == '%':
                s.push(op2 % op1)
            elif lst[i] == '**':
                s.push(op2 ** op1)
            elif lst[i] == '//':
                s.push(op2 // op1)
            else:
                continue
        print(s.pop())
        continue




