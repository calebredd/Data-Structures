"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys

sys.path.append('../stack')
from stack import Stack

from collections import deque 

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None #Other Binary Search Trees
        self.right = None #Other Binary Search Trees

    # Insert the given value into the tree
    def insert(self, value):
    #Thought behind tracking to end position:
        if self.value:
            if self.value > value:
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)
            else:
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)
        else:
            self.value = BSTNode(value)
    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Does the current value exist
        if self.value:
            # Compare current value to the target
            if self.value == target:
                return True
            # If target is less than current value  
            if self.value > target:
            # if left value exists check left
                if self.left:
                    return self.left.contains(target)
                # If left value doesn't exist Else Return False
                else: return False

            # If target is greater than current value 
            else:
            # if right value exists check right
                if self.right:
                    return self.right.contains(target)
                # If right value doesn't exist Else Return False
                else: return False
        # Return False
        else:
            return False


    # Return the maximum value found in the tree
    def get_max(self):
        if self.value:
            if self.right:
                return self.right.get_max()
            else: return self.value
        else: return None

    # Call the function `fn` on the value of each node
    def for_each(self, fn):

        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)
        

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):

        if self.left:
            self.left.in_order_print(node)

        print(self.value)

        if self.right:
            self.right.in_order_print(node)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):

        queue = deque()
        queue.append(self)

        while len(queue):
            current = queue.popleft()
            if current.right:
                queue.append(current.right)
            if current.left:
                queue.append(current.left)
            print(current.value)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):

        print(self.value)
        stack = Stack()
        if self.left:
            stack.push(self.left)
        if self.right:
            stack.push(self.right)
        while stack.__len__():
            newNode = stack.pop()
            newNode.dft_print(node)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):

        print(self.value)

        if self.left:
            self.left.pre_order_dft(node)

        if self.right:
            self.right.pre_order_dft(node)

    # Print Post-order recursive DFT
    def post_order_dft(self, node):

        if self.left:
            self.left.post_order_dft(node)

        if self.right:
            self.right.post_order_dft(node)

        print(self.value)

