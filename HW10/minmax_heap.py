# -*- coding: utf-8 -*-
"""
Created June 19, 2017
minmax_heap.py

Heap in which it is assumed that the keys are the same as the values,
so entries only consist of a single item, not a (key,value) pair.

Constructor allows for min or max heap. Defaults to min.

@author: John Sterling
"""

import operator

class Heap:
    def __init__(self, seq=None, cmp=operator.lt):
        self._data = seq if seq else []
        self._size = len(self._data)
        self._cmp = cmp
        if len(self._data): self.heapify()

    def __len__(self):
        """Return the size of the heap"""
        return self._size

    def is_empty(self):
        """Return True is the heap is empty and False otherwise"""
        return self._size == 0

    def min(self):
        """Return the 'smallest' value"""
        return self._data[0]           # so simple!

    def add(self, value):
        """add value to the heap"""
        # Does the underlying "array" have enough space? If not
        # increase its size Note, we are really using a Python list as
        # our underlying data structure, so any "doubling" is handled
        # for us.
        if len(self) == len(self._data): self._data.append(None)
        self._data[self._size] = value   # insert new item at end of arry
        self.up_heap(self._size)         # "bubble" the new item up.
        self._size += 1                  # bump the sze

    def remove_min(self):
        """Remove the smallest value"""
        # Should raise an exception of size is 0...
        result = self._data[0]         # remember the smallest
        self._data[0] = None           # don't maintain a reference.
        self._size -= 1                # don't forget we have one less
        self.swap(0, self._size)       # bring the last to the front
                                       # and stick the None at the end
        self.down_heap(0)              # drift down item inserted at the front
        return result                  # finally return what was the minimum

    def up_heap(self, index):
        """Bubble up the item at index, as needed"""
        while index:                       # while not at the root
            parent = self._parent(index)   # who is my parent?
            # Am I smaller than my parent?
            if self._cmp(self._data[index], self._data[parent]):
                self.swap(index, parent)          # if so, swap me and my parent
                index = parent                    # and continue bubbling up
            else:
                return                            # otherwise we are done

    def down_heap(self, index):
        """
        down_heap: 'Sift' the item at index down, as needed
        """
        while not self._is_leaf(index):   # Room to sift down to
            min_child = index * 2 + 1     # Assuming left is the smaller child
            if self._has_right(index):    # If I have a right child, then check 
                # is it is smaller
                if self._cmp(self._data[self._right(index)], self._data[min_child]):
                    min_child = self._right(index)     # right is smaller
            if self._cmp(self._data[min_child], self._data[index]):
                # child is smaller
                self.swap(index, min_child) # Swapping with the smaller child
                index = min_child           # And continue sifting down
            else:
                return

    def heapify(self):
        """
        Convert data into a heap
        """
        if self._size:
            start = self._parent(len(self._data)-1)
            for index in range(start, -1, -1):
                self.down_heap(index)

    # Possible convenience functions
    def swap(self, i, j):
        """Swap items at indices i and j"""
        self._data[i], self._data[j] = self._data[j], self._data[i]


    def _is_leaf(self, index):
        """Is index a leaf? Check if it has a left child"""
        return 2*index+1 > self._size - 1

    def _parent(self, index):
        """Where is index's parent?"""
        # Making the "root" its own parent since we don't have a None / nullptr to use.
        return (index - 1) // 2 if index else 0

    def _has_left(self, index):
        """Does index have a left child?"""
        return 2*index+1 < len(self)

    def _left(self, index):
        """Where will index's left child be, if it exists?"""
        return 2*index + 1

    def _has_right(self, index):
        """Does index have a right child?"""
        return 2*index+2 < len(self)

    def _right(self, index):
        """Where will index's right child be, if it exists?"""
        return 2*index + 2


if __name__ == '__main__':
    heap = Heap()
    print('Inserting the numbers from 7 down to 0 into the heap, in that order')
    for i in range(7, -1, -1): heap.add(i)
    print('The resulting array in the heap:')
    print(heap._data)
    print('The items in the heap, removed one by one with remove_min:')
    while not heap.is_empty():
        print(heap.remove_min(), end=' ')
    print('\n==================')
    
    print('Using heapify to turn a Python list of the same numbers [7 down to 0] into a heap.')
    heap = Heap([i for i in range(7, -1, -1)])
    print('The resulting array in the heap:')
    print(heap._data)
    print('The items in the heap, removed one by one with remove_min:')
    while not heap.is_empty():
        print(heap.remove_min(), end=' ')
    print('\n==================')
    print('Max Heap!')
    heap = Heap(None, operator.gt)
    print('Inserting the numbers from 7 down to 0 into the heap, in that order')
    for i in range(7, -1, -1): heap.add(i)
    print('The resulting array in the heap:')
    print(heap._data)
    print('The items in the heap, removed one by one with remove_min:')
    while not heap.is_empty():
        print(heap.remove_min(), end=' ')
    print('\n==================')
    
    print('Using heapify to turn a Python list of the same numbers [7 down to 0] into a heap.')
    heap = Heap([i for i in range(7, -1, -1)], operator.gt)
    print('The resulting array in the heap:')
    print(heap._data)
    print('The items in the heap, removed one by one with remove_min:')
    while not heap.is_empty():
        print(heap.remove_min(), end=' ')
    print('\n==================')
    
