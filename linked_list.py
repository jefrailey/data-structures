class LinkedList(object):
    u"""Create an object to represent a linked list."""
    def __init__(self, head_node=None):
        self.head_node = head_node
        pass

    def insert(self, val):
        u"""Instantiate a Node at the head of the list."""
        if self.head_node:
            self.head_node = Node(val, self.head_node)
        else:
            self.head_node = Node(val)

    def pop(self):
        u"""Pop the head off the linked list."""
        if self.head_node:
            value = self.head_node.value
            self.head_node = self.head_node.the_next
            return value

    def size(self):
        u"""Return the length of the linked list."""
        if self.head_node:
            size = 1
            node = self.head_node
            while True:
                if node.the_next:
                    size += 1
                    node = node.the_next
                else:
                    break
            return size
        else:
            return 0

    def search(self, val):
        u"""Return the first Node that contains val; None if not found."""
        if self.head_node:
            node = self.head_node
            while True:
                if node.value == val:
                    return node
                node = node.the_next

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
                    self.head_node = node.the_next
                    break
                elif cur_node.the_next is None:
                    prev_node.the_next = None
                    break
                else:
                    prev_node.the_next = cur_node.the_next
                    break
            else:
                try:
                    prev_node, cur_node = cur_node, cur_node.the_next
                except AttributeError:
                    prev_node = cur_node

    def __str__(self):
        u"""Return string representation of the linked list."""
        node = self.head_node
        if not node:
            return u"()"
        output = u"(%s" % node.value
        node = node.the_next
        while node.value:
            output = u"%s, %s" % (output, node.value)
            if node.the_next:
                node = node.the_next
            else:
                break
        output = u"%s)" % output
        return output


class Node(object):
    def __init__(self, value, the_next=None):
        self.value = value
        self.the_next = the_next

    def __str__(self):
        return str(self.value)
