class DoublyLinked(object):
    u"""An object that represents a doubly linked list."""
    def __init__(self):
        u"""Instantiate an empty DoublyLinked list."""
        self.head, self.tail = None, None

    def insert(self, value):
        u"""Insert a value at the head of the doubly linked list."""
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        elif self.head is not None:
            node.tailwards, self.head.headwards = self.head, node
            self.head = node

    def append(self, value):
        u"""Append a value to the tail of the doubly linked list."""
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        elif self.head is not None:
            node.headwards, self.tail.tailwards = self.tail, node
            self.tail = node

    def pop(self):
        u"""Remove and return the head value from the list."""
        return_value = None
        if self.head is not None:
            return_value, self.head = self.head.value, self.head.tailwards
            if self.head is not None:
                self.head.headwards = None
        return return_value

    def shift(self):
        u"""Remove and return the tail value from the list."""
        return_value = None
        if self.tail is not None:
            return_value, self.tail = self.tail.value, self.tail.headwards
            if self.tail is not None:
                self.tail.tailwards = None
        return return_value

    def remove(self, value):
        u"""Remove the first matching value from the list."""
        error_msg = "'{}' not found in list!".format(value)
        if self.head is None:
            raise LookupError(error_msg)
        elif (self.head is self.tail) and (self.head.value == value):
            self.head, self.tail = None, None
        elif self.head.value == value:
            self.head = self.head.tailwards
        elif self.tail.value == value:
            self.tail = self.tail.headwards
        else:
            cur_node = self.head
            while True:
                if cur_node.value == value:
                    cur_node.headwards.tailwards = cur_node.tailwards
                    cur_node.tailwards.headwards = cur_node.headwards
                    break
                else:
                    if cur_node.tailwards is None:
                        raise LookupError(error_msg)
                    else:
                        cur_node = cur_node.tailwards


class Node(object):
    u"""An object that represents a node for use in a doubly linked list."""
    def __init__(self, value):
        self.headwards, self.tailwards, self.value = None, None, value
