#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a nodes object")
        self.__next_node = value

class SinglyLinkedList:
    def __init__(self):
        self.__head = None

    def __str__(self):
        _var = self.__head
        _print = []
        while _var:
            _print.append(str(_var.data))
            _var = _var.next_node
        return ("\n".join(sorted(_print, key=int)))

    def sorted_insert(self, value):
        new_node = Node(value)
        if self.__head is None or value < self.__head.data:
            new_node.next = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
