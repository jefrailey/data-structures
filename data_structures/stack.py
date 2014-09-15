class Stack(object):

    u"""An object representing a stack data structure."""

    def __init__(self):
        u"""Instantiate a Stack without Data."""
        self.head_data = None

    def push(self, data):
        u"""Push a new data element to the top of the Stack."""
        if self.head_data:
            new_data = Data(data, self.head_data)
        else:
            new_data = Data(data)
        self.head_data = new_data

    def pop(self):
        u"""Remove a data element from the top of the Stack."""
        if self.head_data:
            return_data = self.head_data.value
            self.head_data = self.head_data.above
            return return_data
        else:
            raise LookupError(u"Stack is empty")

    def __unicode__(self):
        u"""
        Return unicode represntation of all values in Stack.

        Values are returned from top to bottom.
        """
        output = [u"("]
        if self.head_data:
            node = self.head_data
            while node.above:
                output.append(u"{}, ".format(node.value))
                node = node.above
            output.append(u"{}".format(node.value))
        output.append(u")")
        return u"".join(output)

    def __str__(self):
        return unicode(self).encode('utf-8')


class Data(object):

    u"""An object representing data in a Stack."""

    def __init__(self, value, above=None):
        self.value = value
        self.above = above

    def __unicode__(self):
        return u"{}".format(self.value)

    def __str__(self):
        return unicode(self).encode('utf-8')
