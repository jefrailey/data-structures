from data_structures.lists.linked_list import LinkedList


class Queue(object):
    u"""A queue object that holds values in a FiFo format."""
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
            last_node = node
            value = last_node.value
            self.list.remove(last_node)
        else:
            raise LookupError(u"The queue is empty!")
        return value

    def size(self):
        u"""Return the number of values stored in the Queue."""
        return self.list.size()

    def __str__(self):
        u"""Return a unicode string representation of data held in Queue."""
        output = [u")"]
        if self.list.head_node:
            node = self.list.head_node
            output.append(u"{}".format(node.value))
            while node.next_node:
                node = node.next_node
                output.append(u"{}, ".format(node.value))
        output.append(u"(")
        output.reverse()
        return u"".join(output)
