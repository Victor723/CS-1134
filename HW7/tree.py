#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  5 11:16:36 2017

@author: Zhoukx.joseph
"""

class LinkedBinaryTree:
    class Node:
        def __init__(self,element,parent=None,left=None,right=None):
            self.element=element
            self.parent=parent
            self.left=left
            self.right=right
    class Position:
        def __init__(self,container,node):
            self.container=container
            self.node=node
        def element(self):
            return self.node.element
        def __eq__(self,other):
            return type(other) is type(self) and other.node is self.node
    
    def validate(self,p):
        if not isinstance(p,self.Position):
            raise TypeError('p must be proper Position type')
        if p.container is not self:
            raise ValueError('p does not belong to this container')
        if p.node.parent is p.node:
            raise ValueError('p is no longer valid')
        return p.node
    
    def make_position(self,node):
        return self.Position(self,node) if node is not None else None
    def __init__(self):
        self.root=None
        self.size=0
    
    def __len__(self):
        return self.size
    def root(self):
        return self.make_position(self.root)
    def parent(self,p):
        node=self.validate(p)
        return self.make_position(node.parent)
    def left(self,p):
        node=self.validate(p)
        return self.make_position(node.left)
    def right(self,p):
        node=self.validate(p)
        return self.make_position(node.right)
    def num_children(self,p):
        node=self.validate(p)
        count=0
        if node.left is not None:
            count+=1
        if node.right is not None:
            count+=1
        return count
    def add_root(self,e):
        if self.root is not None: raise ValueError('Root exists')
        self.size=1
        self.root=self.Node(e)
        return self.make_position(self.root)
    def add_left(self,p,e):
        node = self.validate(p)
        if node.left is not None: raise ValueError('Left child exists')
        self.size+=1
        node.left= self.Node(e,node)
        return self.make_position(node.left)
    def add_right(self,p,e):
        node=self.validate(p)
        if node.right is not None: raise ValueError('Right child exists')
        self.size+=1
        node.right=self.Node(e,node)
        return self.make_position(node.right)
p=LinkedBinaryTree()
p.add_root(3)
p.add_left(p.root(),2)
p.add_right(p.root(),7)


