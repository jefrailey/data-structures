class DoublyLinked(object):
    """docstring for DoublyLinked"""
    def __init__(self, head=None, tail=None):
        self.h = head
        self.t = tail

    def insert(self,value):
        node = Node(value)
        if not self.h:
            self.h = self.t = node
        elif self.h:
            node.twards, self.h.hwards, self.h = self.h, node, node

    def append(self,value):
        node = Node(value)
        if not self.h:
            self.h = self.t = node
        elif self.h:
            node.hwards, self.t.twards, self.t = self.t, node, node

    def pop(self):
        """Removes and returns the h value from the list."""
        returnValue = None
        try:
            returnValue, self.h, self.h.hwards = self.h.value, self.h.twards, None
        except AttributeError:
            returnValue, self.h, self.t = self.h.value, None, None
        finally:
            return returnValue

    def shift(self):
        """Removes and returns the t value from the list."""
        returnValue = None
        try:
            returnValue, self.t, self.t.twards = self.t.value, self.t.hwards, None
        except AttributeError:
            returnValue, self.t, self.h = self.t.value, None, None
        finally:
            return returnValue


class Node(object):
    """docstring for Node"""
    def __init__(self, value, hwards=None, twards=None):
        self.hwards = hwards
        self.twards = twards
        self.value = value
