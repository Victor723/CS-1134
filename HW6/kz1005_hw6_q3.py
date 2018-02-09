#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 09:59:18 2017

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

class CompactString:
    def __init__(self,orig_str):
        self.data=DoublyLinkedList()
        counter=1
        if len(orig_str)==1:
            self.data.add_first((orig_str),1)
        elif len(orig_str)>1:
            for i in range(len(orig_str)-1):
                if orig_str[i]!=orig_str[i+1]:
                    self.data.add_last((orig_str[i],counter))
                    counter=1
                    continue
                counter +=1
            if orig_str[len(orig_str)-1]==orig_str[len(orig_str)-2]:
                self.data.add_last((orig_str[len(orig_str)-1],counter))
    def __add__(self,other):
        n=CompactString('')
        p1=self.data.last_node()
        p2=other.data.first_node()
        if p1.data[0]==p2.data[0]:
            n.data.add_first((p1.data[0],p1.data[1]+p2.data[1]))
        else:
            n.data.add_first((p1.data[0],p1.data[1]))
            n.data.add_last((p2.data[0],p2.data[1]))
        p1=p1.prev
        p2=p2.next
        while p1.data is not None:
            n.data.add_first((p1.data[0],p1.data[1]))
            p1=p1.prev
        while p2.data is not None:
            n.data.add_last((p2.data[0],p2.data[1]))
            p2=p2.next
        return n
    def __lt__(self,other):
        p1=self.data.first_node()
        p2=other.data.first_node()
        v1=p1.data[1]
        v2=p2.data[1]
        while p1.data is not None:
            if p1.data[0]<p2.data[0]:
                return True
            if p1.data[0]>p2.data[0]:
                return False
            if v1>v2:
                if p2.next.data is None:
                    return False
                p2=p2.next
                v2+=p2.data[1]
            elif v1<v2:
                if p1.next.data is None:
                    return True
                p1=p1.next
                v1+=p1.data[1]
            elif v1==v2:
                if p2.next.data is not None and p1.next.data is None:
                    return True
                if p2.next.data is None:
                    return False
                p1=p1.next
                p2=p2.next
                v1+=p1.data[1]
                v2+=p2.data[1]
        if p2.next.data is not None and v1<=v2:
            return True
        elif v1>=v2:
            return False
        return True
    def __le__(self,other):
        p1=self.data.first_node()
        p2=other.data.first_node()
        v1=p1.data[1]
        v2=p2.data[1]
        while p1.data is not None:
            if p1.data[0]<p2.data[0]:
                return True
            if p1.data[0]>p2.data[0]:
                return False
            if v1>v2:
                if p2.next.data is None:
                    return False
                p2=p2.next
                v2+=p2.data[1]
            elif v1<v2:
                if p1.next.data is None:
                    return True
                p1=p1.next
                v1+=p1.data[1]
            elif v1==v2:
                if p2.next.data is not None and p1.next.data is None:
                    return True
                if p2.next.data is None and p1.next.data is None:
                    return True
                if p2.next.data is None:
                    return False
                p1=p1.next
                p2=p2.next
                v1+=p1.data[1]
                v2+=p2.data[1]
        if p2.next.data is not None and v1<=v2:
            return True
        elif v1>v2:
            return False
        return True
    def __gt__(self,other):
        return other<self
    def __ge__(self,other):
        return other<=self
    def __str__(self):return ''.join([str(elem) for elem in self.data])
    def __repr__(self): return str(self)



















