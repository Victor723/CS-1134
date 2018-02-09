#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 09:29:11 2017

@author: Zhoukx.joseph
"""

class SeparateChaining:
    def __init__(self,size=7):
        self.table=[[] for _ in range(size)]
        self.size=0
        
        
    def __len__(self):
        return self.size
    
    
    def __setitem__(self,key,value):
        index = hash(key) % len(self.table)
        bucket = self.table[index]
        for key_val in bucket:
            if key_val[0]==key:
                key_val[1]=value
                return
        bucket.append([key,value])
        self.size+=1
    
    def __getitem__(self,key):
        index=hash(key) % len(self.table)
        bucket = self.table[index]
        for k, v in bucket:
            if k == key:
                return v
        raise KeyError
    
    def __delitem__(self,key):
        index=hash(key) % len(self.table)
        bucket=self.table[index]
        for key_val in bucket:
            if key_val[0]==key:
                
    