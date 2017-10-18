"""
@author: Zhoukx.joseph
"""

# Question 1

def split_by_sign(lst, low, high):
    if low > high:
        return []
    D = split_by_sign(lst,low+1,high)
    if lst[low] >= 0:
        D.append(lst[low])
    else:
        D.insert(0,lst[low])
    return D

# Question 2

def permutations(lst,low,high):
    if low == high == 0:
        return [[lst[low]]]
    elif len(lst)==1:
        return[lst]
    else:
        result=[]
        for i in range(high-low+1):
            e=lst[low+i]
            l=lst[low:low+i]+lst[low+i+1:high+1]#create a list that contains all elements except a certain one.
            for item in permutations(l,0,len(l)-1):
                result.append([e]+item)
        return result

print(permutations([1,2,3,4],1,3))

# Question 4(a)

def find_duplicates(lst):
    L=[0]*len(lst)#create a list contains 0
    R=[]
    for i in range(len(lst)):
        if L[lst[i]]==0:
            L[lst[i]]=1
        else:
            L[lst[i]]+=1
    for i in range(len(lst)):
        if L[i] > 1:#find the duplicate
            R.append(i)
    return R

# Question 5(b)

def remove_all(lst, value): 
    L=[]
    for i in range(0,len(lst)):
        if lst[i] != value:#check if the value is inside the list.
            L.append(lst[i])
    lst[:]=L#doesn't return the list

def remove_all(lst, value):
    count = 0
    for i in range(len(lst)):
        if lst[i]!=value:
            lst[i-count]=lst[i]
        else:
            count+=1
    for i in range(count):
        lst.pop()

# Question 3 MyList Class

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
            for j in range(self.n):
                nlst.append(self.data[j])
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
