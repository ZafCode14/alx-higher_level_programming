#!/usr/bin/python3
"""Define classes"""


class Node:
    """Node for a singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next = value


class SinglyLinkedList:
    """Singly linked list"""
    def __init__(self):
        self.head = None

    def sorted_insert(self, value):
        new = Node(value)
        if self.head is None:
            new.next = None
            self.head = new
        elif self.head.data > value:
            new.next = self.head
            self.head = new
        else:
            temp = self.head
            while (temp.next is not None and temp.next.data < value):
                temp = temp.next
            new.next = temp.next
            temp.next = new

    def __str__(self):
        values = []
        temp = self.head
        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next
        return ('\n'.join(values))
