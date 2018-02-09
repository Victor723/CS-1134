#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 21:39:43 2017

@author: Zhoukx.joseph
"""
def factors(num):
    L = []
    for x in range(1,int(num**(1/2))+1):
        if num % x == 0:
            yield x
            if x*x != num:
                L.append(int(num/x))
    for x in reversed(L):
        yield x
for i in factors(100):
    print(i)

def e_approx(n):
    e = 1
    factorial = 1
    for i in range(1,n+2):
        factorial *=i
        e += 1/factorial
    return e

for n in range(1):
    curr_approx = e_approx(n)
    approx_str = "{:.15f}".format(curr_approx)
    print("n =", n, "Approximation:", approx_str)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 22:03:30 2017

@author: Zhoukx.joseph
"""

def split_parity(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            lst.append(lst[i])
            count +=1
    for i in range(len(lst)):
        if lst[i] % 2 == 1:
            lst.append(lst[i])
            count +=1
    for i in range(count):
        lst[i]=lst.pop()
    return lst
L=[1,2,3,4,5,6,7,9,10,10,11]

def split_parity2(lst):
    n=len(lst)
    for i in range(n):
        if lst[i]%2==0:
            lst.append(lst[i])
    for i in range(n):
        if lst[i]%2!=0:
            lst.append(lst[i])
    for i in range(n):
        lst[i]=lst.pop()
    return lst
print(split_parity2(L))

def two_sum(lst,target):
    L={(target-lst[i]):i for i in range(len(lst))}
    I={i:lst[i]for i in range(len(lst))}
    for i in range(len(lst)):
        if I.get(i) in L:
            return (i,L.get(I.get(i)))
        
srt_lst=[-2, 7, 11, 15, 20, 21]
print(two_sum(srt_lst,22))

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