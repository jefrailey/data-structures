class LinkedList(object):

    u"""An object representing a linked list."""

    def __init__(self, head_node=None):
        self.head_node = head_node

    def insert(self, val):
        u"""Instantiate a Node with the given value at the head of the list."""
        if self.head_node:
            self.head_node = Node(val, self.head_node)
        else:
            self.head_node = Node(val)

    def pop(self):
        u"""Return the value of the head node and remove it from the list."""
        if self.head_node:
            value = self.head_node.value
            self.head_node = self.head_node.next_node
            return value

    def size(self):
        u"""Return the length of the linked list."""
        size = 0
        if self.head_node:
            node = self.head_node
            while True:
                try:
                    node = node.next_node
                except AttributeError:
                    break
                size += 1
        return size

    def search(self, val):
        u"""Return the first Node that contains val; None if not found."""
        if self.head_node:
            node = self.head_node
            while True:
                if node.value == val:
                    return node
                node = node.next_node

    def remove(self, node):
        u"""Remove the node from the list; assumes node is in list."""
        if self.head_node:
            prev_node = None
            cur_node = self.head_node
        else:
            return None
        while True:
            if cur_node == node:
                if prev_node is None:
                    self.head_node = node.next_node
                    break
                elif cur_node.next_node is None:
                    prev_node.next_node = None
                    break
                else:
                    prev_node.next_node = cur_node.next_node
                    break
            else:
                try:
                    prev_node, cur_node = cur_node, cur_node.next_node
                except AttributeError:
                    prev_node = cur_node

    def __unicode__(self):
        u"""Return string representation of the linked list."""
        node = self.head_node
        output = [u"("]
        while node is not None:
            if node.next_node is not None:
                output.append(u"{}, ".format(node.value))
                node = node.next_node
            else:
                output.append(node.value)
                break
        output.append(u")")
        return u"".join(output)

    def __str__(self):
        return unicode(self).encode('utf-8')


class Node(object):
    def __init__(self, value, next_node=None):
        self.value, self.next_node = value, next_node

    def __unicode__(self):
        return u"{}".format(self.value)

    def __str__(self):
        return unicode(self).encode('utf-8')
