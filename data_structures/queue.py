from data_structures.lists.linked_list import LinkedList


class Queue(object):
    u"""Creates a queue object that holds values in a FiFo format."""
    def __init__(self):
        self.list = LinkedList()

    def enqueue(self, value):
        u"""Adds a value/node to the head of the Queue object."""
        self.list.insert(value)

    def dequeue(self):
        u"""Removes a value/node from the tail of the Queue object."""
        if self.list.head_node:
            node = self.list.head_node
            while node.next_node:
                node = node.next_node
            else:
                last_node = node
            a = last_node.value
            self.list.remove(last_node)
            return a
        else:
            raise LookupError

    def size(self):
        u"""Return the number of values stored in the Queue."""
        return self.list.size()

    def __str__(self):
        u"""Return a unicode string representation of data held in Queue."""
        q_str = u")"
        if self.list.head_node:
            node = self.list.head_node
            while node.next_node:
                if len(q_str) == 1:
                    q_str = u"{}".format(node.value) + q_str
                else:
                    q_str = u"{},".format(node.value) + q_str
                node = node.next_node
            q_str = u"{},".format(node.value) + q_str
        return u"({}".format(q_str)
