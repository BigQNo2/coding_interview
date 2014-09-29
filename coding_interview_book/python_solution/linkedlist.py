"""A module contains the linkedlist class for chapter 2.
"""

class LinkedListNode(object):
    """ the LinkedList class"""

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def __str__(self):
        return str(self.data)

    def append_to_tail(self, data):
        """append a node to the end of a linkedlist.
        Args:
            data: the data in new end.
        Return:
            head: the head of updated linkedlist
        """
        head = self
        end = LinkedListNode(data=data)
        while self.next != None:
            self = self.next
        self.next = end
        return head

    def append_to_head(self, data):
        """append a node to the head of a linkedlist.
        Args:
            data: the data in new head.
        Return:
            head: the head of the updated linkedlist
        """
        head = LinkedListNode(data=data)
        head.next = self
        self = head
        return self

    def delete_head(self):
        """delete the head of a linkedlist.
        Return:
            the head of the updated linkedlist
        """
        return self.next

    def delete_a_node(self, data):
        """delete a specified node in a linkedlist.
        Args:
            data: the data of specified node.
        Return:
            head: the head of the updated linkedlist
        """
        head = self
        if self.data == data:
            return self.next

        while self.next != None:
            if self.next.data == data:
                self.next = self.next.next
                return head # head doesn't change
            self = self.next

        return head

    def to_list(self):
        """convert a linkedlist to a list
        """
        results = list()
        while self.next != None:
            results.append(str(self.data))
            self = self.next
        results.append(str(self.data))

        return results

    def to_str(self):
        """covert a linkedlist to a string
        """
        return ''.join(self.to_list())
