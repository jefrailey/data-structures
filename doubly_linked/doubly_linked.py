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





class Node(object):
    """docstring for Node"""
    def __init__(self, value, hwards=None, twards=None):
        self.hwards = hwards
        self.twards = twards
        self.value = value
