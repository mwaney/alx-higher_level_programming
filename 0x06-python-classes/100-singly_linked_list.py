#!/usr/bin/python3
"""Node class for a singly linked list"""


class Node:
    """A node to be in the list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """A private instance to get data"""
        return self.__data

    @data.setter
    def data(self, value):
        """A private instance to set data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """A Setter method to the next node"""
        if type(value) is not Node and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    A singly linked list class
    """

    def __init__(self):
        """
        Creates instance of Singly Linked list
        """
        self.__head = None

    def __str__(self):
        """
        A getter method to return
        the list in stdout line by line
        """
        insert = self.__head
        list = ""

        while insert is not None:
            list += str(insert.data)
            insert = insert.next_node

            if insert is not None:
                list += "\n"

        return list

    def sorted_insert(self, value):
        """sorts and inserts Node into the correct
        position in the list
        The sort is in increasing order
        """

        insert = Node(value)
        if self.__head is None:
            self.__head = insert
            return

        tmp = self.__head

        if insert.data < tmp.data:
            insert.next_node = self.__head
            self.__head = insert
            return

        while tmp.next_node:
            if insert.data < tmp.next_node.data:
                break
            tmp = tmp.next_node

        insert.next_node = tmp.next_node
        tmp.next_node = insert

        return
