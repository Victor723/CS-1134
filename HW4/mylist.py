#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 12 20:59:17 2017

@author: Zhoukx.joseph
"""

import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class MyList:
    def __init__(self):
        self.data = make_array(1)
        self.capacity = 1
        self.n = 0

    def __len__(self):
        return self.n


    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1


    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size


    def extend(self, other):
        for elem in other:
            self.append(elem)


    def __getitem__(self, ind):
        if ind < 0:
            ind = ind+self.n
        if (not (0 <=ind <= self.n - 1)):
            raise IndexError('invalid index')
        return self.data[ind]


    def __setitem__(self, ind, val):
        if ind < 0:
            ind = ind+self.n
        if (not (0 <=ind <= self.n - 1)):
            raise IndexError('invalid index')
      
        self.data[ind] = val
    
    def  __str__(self):
        return str([self.data[i] for i in range(self.n)])
    
    def __repr__(self):
        return str([self.data[i] for i in range(self.n)])
    
    def __add__(self,other):
        nlst = MyList()
        for i in range(self.n):
            nlst.append(self.data[i])
        for i in range(other.n):
            nlst.append(other.data[i])
        return nlst
    
    def __iadd__(self,other):
        for i in range(other.n):
            self.append(other[i])
        return self
    
    def __mul__(self,n):
        nlst = MyList()
        for i in range(n):
            for i in range(self.n):
                nlst.append(self.data[i])
        return nlst
    def __rmul__(self,n):
        return self*n
        
    def insert(self,index,val):
        if index<0 or index>self.n:
            raise IndexError('invalid index')
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        m = self.n - 1
        p = index
        while p <= m:
            self.data[m+1] = self.data[m]#shifting the elements
            m -= 1
        self.data[p] = val
        self.n += 1
        
    def pop(self,i=None):#set the default index to None
        if i is None:
            i=self.n-1#assign the default index to the last element if users didn't input index
        if self.n == 0:
            raise IndexError('the MyList() object is empty')
        if i > self.n-1 or i <-self.n:
            raise IndexError('Invalid Index')
        poped = self.data[i]
        k=self.n-1
        j=i
        while j < k:
            self.data[j]=self.data[j+1]#shifting data
            j +=1
        self.data[k] = None
        if self.n < (self.capacity//4):#shrinking the size
            self.resize(self.capacity//2)
        return poped

mlst = MyList()
for i in range(1,6):
    mlst.append(i)
print(mlst)
mlst*3
print(3*mlst)