class DoublyLinked(object):
    u"""An object that represents a doubly linked list."""
    def __init__(self):
        u"""Instantiate an empty DoublyLinked list."""
        self.head, self.tail = None, None

    def insert(self, value):
        u"""Insert a value at the head of the doubly linked list."""
        node = Node(value)
        if not self.h:
            self.h = self.t = node
        elif self.h:
            node.twards, self.h.hwards, self.h = self.h, node, node

    def append(self, value):
        u"""Append a value to the tail of the doubly linked list."""
        node = Node(value)
        if not self.h:
            self.h = self.t = node
        elif self.h:
            node.hwards, self.t.twards, self.t = self.t, node, node

    def pop(self):
        u"""Removes and returns the h value from the list."""
        returnValue = None
        try:
            returnValue, self.h, self.h.hwards = (
                self.h.value,
                self.h.twards,
                None
                )
        except AttributeError:
            returnValue, self.h, self.t = self.h.value, None, None
        finally:
            return returnValue

    def shift(self):
        u"""Removes and returns the t value from the list."""
        returnValue = None
        try:
            returnValue, self.t, self.t.twards = (
                self.t.value,
                self.t.hwards,
                None
                )
        except AttributeError:
            returnValue, self.t, self.h = self.t.value, None, None
        finally:
            return returnValue

    def remove(self, value):
        u"""Removes the first matching value from the list."""
        if self.h is None:
            raise LookupError
        elif self.h is self.t and self.h.value == value:
            self.h = None
            self.t = None
        elif self.h.value == value:
            self.h = self.h.twards
        elif self.t.value == value:
            self.t = self.t.hwards
        else:
            cur_node = self.h
            while True:
                if cur_node.value == value:
                    cur_node.hwards.twards = cur_node.twards
                    cur_node.twards.hwards = cur_node.hwards
                    break
                else:
                    if cur_node.twards is None:
                        raise LookupError
                    else:
                        cur_node = cur_node.twards


class Node(object):
    u"""An object that represents a node for use in a doubly linked list."""
    def __init__(self, value):
        self.headwards, self.tailwards, self.value = None, None, value
