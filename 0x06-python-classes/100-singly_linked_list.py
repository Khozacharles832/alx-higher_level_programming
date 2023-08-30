#!/usr/bin/python3
""" Defines the classes, Node and SinglyLinkedList """

class Node:
    """ a class that defines the node's properties
        
        Attributes:
            data: data field of the node
    """
    def __init__(self, data, next_node=None):
        """ creates an instance of node
            
            Args:
                data: the data field of the node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """ collects the data from the class
        Returns: the data of tthe node
        """
        return (self.__data)

    @data.setter
    def data(self, value):
        """ property setter for node
            
            Agrs:
                value: the new value

            Returns: the new value
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ collects data for new node
            
            Returns: the instance of the new node
        """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        """ property setter for node

            Args: 
                value: the new value

            Raises:
                TypeError: next node must be a nodes object
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a nodes object")
        self.__next_node = value

class SinglyLinkedList:
    """ class that defines properties of a singlylinkedList

        Attributes:
            head: the head of the singly linked list
    """
    def __init__(self):
        """ creates a new instance of a linked list

            Attributes:
                head: the head of the singly linked list
        """
        self.__head = None

    def __str__(self):
        """ creates a new instance of a singly linked list

            Attributes:
                head: the head of linked list
        """
        _var = self.__head
        _print = []
        while _var:
            _print.append(str(_var.data))
            _var = _var.next_node
        return ("\n".join(sorted(_print, key=int)))

    def sorted_insert(self, value):
        """ inserts a new node at a given position

            Args:
                value: the new value
        """
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
