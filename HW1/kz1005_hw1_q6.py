#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 19:47:35 2017

@author: Zhoukx.joseph
"""

class Vector:
    def __init__(self,d):
        if isinstance(d, int):
            self.coords = [0]*d
        if isinstance(d, list):
            self.coords = d[:]

    def __len__(self):
        return len(self.coords)
    
    def __getitem__(self,j):
        return self.coords[j]
    
    def __str__(self):
        return '<'+str(self.coords)[1:-1]+'>'
    
    def __setitem__(self,j,val):
        self.coords[j]=val
    
    def __add__(self,other):
        if (len(self)!=len(other)):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j]+other[j]
        return result
    
    def __eq__(self, other):
        return self.coords == other.coords
    def __ne__(self, other):
        return not (self == other)
    
    def __repr__(self):
        return str(self)
    
    def __sub__(self,u):
        if (len(self)!=len(u)):
            raise ValueError("dimensions must agree")
        return Vector([self.coords[x] - u.coords[x] for x in range(len(u))])
    
    def __neg__(self):
        return Vector([-self.coords[x] for x in range(len(self))])

    def __mul__(self,d):
        if isinstance(d,int):
            return Vector([self.coords[x]*3 for x in range(len(self))])
        elif (len(self)!=len(d)):
            raise ValueError("dimensions must agree")
        else:
            return sum([self.coords[x]*d.coords[x] for x in range(len(self))])
    
    def __rmul__(self,d):
        return Vector([3*self.coords[x] for x in range(len(self))])

#Check the class and the related methods:
v1= Vector(3)
v1[1]=10
print(v1)
v2=Vector([2,4,6])
print(v2)
u1=v1+v2
print(u1)
u2=-v1
print(u2)
u3=3*v1
print(u3)
u4=v1*4
print(u4)
u5 = v1 * v2
print(u5)