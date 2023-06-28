#!/usr/bin/python3
"""This module defines:
    class: SinglyLinkedList
    class: Node used by the SinglyLinkedList class
"""


class SinglyLinkedList:
    """This class defines a SinglyLinkedList object"""

    def __init__(self):
        """Initialises the SinglyLinkedList instance"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node into the SinglyLinkedList instance in
        ascending order.

        Args:
            value (int): Data of the new node
        """
        if not self.__head:
            self.__head = Node(value)
        elif value <= self.__head.data:
            new_node = Node(value, self.__head)
            self.__head = new_node
        else:
            prev_node = self.__head
            next_node = self.__head.next_node
            while next_node:
                if value <= next_node.data:
                    break
                prev_node = next_node
                next_node = next_node.next_node
            new_node = Node(value, next_node)
            prev_node.next_node = new_node

    def __str__(self):
        """Prints the SinglyLinkedList"""
        sll_str = ""
        node = self.__head
        while node:
            if sll_str:
                sll_str += '\n'
            sll_str += f"{str(node.data)}"
            node = node.next_node
        return sll_str


class Node:
    """This class defines a Node in a singly-linked list"""

    def __init__(self, data, next_node=None):
        """Initialises a Node

        Args:
            data (int): The integer data held by the list element
            next_node (obj: `Node`, optional): The next node in the linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data (int): The integer data held by the Node instance

        Setter raises TypeError if data is not an int
        """
        return self.__data

    @data.setter
    def data(self, data):
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        """next_node (obj: `Node`): The next node in the list after this one

        TypeError is raised if next_node is not a Node object
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, next_node):
        if isinstance(next_node, Node) or next_node is None:
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")
