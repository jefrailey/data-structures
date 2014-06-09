from linked_list import LinkedList


class Queue(LinkedList):
    u"""Creates a queue object that holds values in a FiFo format."""
    def __init__(self):
        super(Queue, self).__init__()

    def enqueue(self, value):
        u"""Adds a value/node to the head of the Queue object."""
        self.insert(value)

    def dequeue(self):
        u"""Removes a value/node from the tail of the Queue object."""
        if self.head_node:
            node = self.head_node
            while node.the_next:
                node = node.the_next
            else:
                last_node = node
            a = last_node.value
            self.remove(last_node)
            return a
        else:
            raise LookupError
