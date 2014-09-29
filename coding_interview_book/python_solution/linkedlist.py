"""A module contains the linkedlist class for chapter 2 
"""

class LinkedListNode(object):
    """ the LinkedList class"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

    def append_to_tail(self, data):
        head = self
        end = LinkedListNode(data=data)
        while self.next != None:
            self = self.next
        self.next = end
        return head

    def append_to_head(self, data):
        head = LinkedListNode(data=data)
        head.next = self
        self = head
        return self

    def delete_head(self):
        return self.next

    def delete_a_node(self, data):
        head = self
        if self.data == data:
            return self.next

        while self.next != None:
            if self.next.data == data:
                self.next = self.next.next
                return head # head doesn't change
            self = self.next

        return head



    