"""
heapsort
-jbs
"""
from minmax_heap import Heap
import random
import operator

def heapsort(L):
    heap = Heap(L, operator.gt)
    print("List after it has been heapified:")
    print(heap._data)
    print("Items as they are removed:")
    for i in range(len(heap)):
        item = heap.remove_min()
        print(item, end=' ')
        L[-1 - i] = item
    print()
    return L

L = random.sample(range(10), 10)
print("Randomly ordered list of numbers 0 to 9:")
print(L)
L = heapsort(L)
print("sorted list:")
print(L)
