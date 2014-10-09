"""A module that contains the class to implement the data structure of stack
"""

from linkedlist import LinkedListNode

class Stack(object):
    """the LinkedList implementation by adding or removing LinkedList head"""

    def __init__(self):
        self.top = None 

    def push(self, data):
        """Push data to the stack top. Add new head.
        """
        new_top = LinkedListNode(data)
        new_top.next = self.top
        self.top = new_top

    def pop(self):
        """Pop data from the stack top. Remove current head.
        """
        if self.top != None:
            item = self.top.data
            self.top = self.top.next

            return item
        else:
            return None

    def peek(self):
        """Peek the stack top"""
        return self.top.data


 