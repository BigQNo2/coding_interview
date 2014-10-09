"""A module that contains the class to implement the data structure of queue
"""

from linkedlist import LinkedListNode

class Queue(object):
    """the linkedList implementation. Adding tail and Removing head."""

    def __init__(self):
        self.tail = None
        self.head = None

    def enqueue(self, data):
        """Add the data to the queue tail."""
        new_tail = LinkedListNode(data)
        if self.tail == None:
            self.tail = new_tail
            self.head = new_tail
        else:
            self.tail.next = new_tail
            self.tail = new_tail #Update the tail

    def dequeue(self):
        """Remove the data from queue head"""
        if self.head != None:
            item = self.head.data
            self.head = self.head.next #Update the head

            return item
        else:
            return None
