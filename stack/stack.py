class Stack(object):

    u"""Create an object representing a stack data structure."""

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
            self.head_data = self.head_data.is_above
            return return_data
        else:
            raise LookupError

    def __str__(self):
        u"""
        Return unicode represntation of all values in Stack.

        Values are returned from top to bottom.
        """
        if self.head_data:
            node = self.head_data
            output = u"("
            while node.is_above:
                output += u"{}, ".format(unicode(node.value))
                node = node.is_above
            output += u"{})".format(unicode(node.value))
            return output
        else:
            return u"()"


class Data(object):

    u"""Create an object representing data in a Stack."""

    def __init__(self, value, is_above=None):
        self.value = value
        self.is_above = is_above

    def __str__(self):
        u"""Return unicode represenation of Data.value."""
        return unicode(self.value)