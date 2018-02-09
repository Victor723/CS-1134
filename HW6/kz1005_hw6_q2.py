4#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 18:20:41 2017

@author: Zhoukx.joseph
"""

class EmptyCollection(Exception):
    pass


class DoublyLinkedList:
    class Node:
        def __init__(self, data=None, next=None, prev=None):
            self.data = data
            self.next = next
            self.prev = prev

        def disconnect(self):
            self.data = None
            self.next = None
            self.prev = None

    def __init__(self):
        self.header = DoublyLinkedList.Node()
        self.trailer = DoublyLinkedList.Node()
        self.header.next = self.trailer
        self.trailer.prev = self.header
        self.size = 0

    def __len__(self):
        return self.size

    def is_empty(self):
        return (len(self) == 0)

    def first_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
        return self.header.next

    def last_node(self):
        if (self.is_empty()):
            raise EmptyCollection("List is empty")
        return self.trailer.prev

    def add_first(self, elem):
        return self.add_after(self.header, elem)

    def add_last(self, elem):
        return self.add_after(self.trailer.prev, elem)

    def add_after(self, node, elem):
        prev = node
        succ = node.next
        new_node = DoublyLinkedList.Node()
        new_node.data = elem
        new_node.prev = prev
        new_node.next = succ
        prev.next = new_node
        succ.prev = new_node
        self.size += 1
        return new_node

    def add_before(self, node, elem):
        return self.add_after(node.prev, elem)

    def delete(self, node):
        prev = node.prev
        succ = node.next
        prev.next = succ
        succ.prev = prev
        self.size -= 1
        data = node.data
        node.disconnect()
        return data

    def __iter__(self):
        if(self.is_empty()):
            return
        cursor = self.first_node()
        while(cursor is not self.trailer):
            yield cursor.data
            cursor = cursor.next

    def __str__(self):
        return '[' + '<-->'.join([str(elem) for elem in self]) + ']'

    def __repr__(self):
        return str(self)

class Integer:
    def __init__(self, num_str):
        self.data=DoublyLinkedList()
        for i in num_str:
            self.data.add_last(int(i))
    def __add__(self, other):
        n=Integer('')
        difference = abs(len(self.data)-len(other.data))
        if len(self.data)<len(other.data):
            for i in range(difference):
                self.data.add_first(0)
        else:
            for i in range(difference):
                other.data.add_first(0)
        pointer1,pointer2=self.data.last_node(),other.data.last_node()
        carry=0
        while(pointer1.data !=None or pointer1.data!=None):
            addition=0
            remainder=0
            addition=pointer1.data+pointer2.data+carry
            carry = 0
            remainder=addition%10
            carry=addition//10
            n.data.add_first(remainder)
            pointer1=pointer1.prev
            pointer2=pointer2.prev
        if carry > 0:
            n.data.add_first(carry)
        return n
    def __str__(self):
        return ''.join([str(elem) for elem in self.data])
    def __repr__(self): 
        return str(self)
    def __mul__(self,other):
        n=Integer('')
        if self.data.first_node().data==0 or other.data.first_node().data==0:
            n.data.add_last(0)
            return n
        digit=0
        pointer=other.data.last_node()
        while (pointer.data != None):
            p=Integer('')
            if pointer.data==0:
                digit+=1
                pointer=pointer.prev
                continue
            for i in range(pointer.data):
                p=self+p
            for i in range(digit):
                p.data.add_last(0)
            n=p+n
            pointer=pointer.prev
            digit+=1
        return n
n7 = Integer('007')
n8 = Integer('20')
n9 = n7 + n8
n9_other = n8 + n7
#self.assertEqual(str(n9), '27')
print(n9)
print(n9_other)

n1 = Integer('3')
n2 = Integer('6')
n3 = n1 * n2
n3_other = n2 * n1
#self.assertEqual(str(n3), '18')
print(n3)
#self.assertEqual(str(n3_other), '18')
print(n3_other)
