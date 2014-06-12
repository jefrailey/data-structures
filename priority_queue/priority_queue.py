import datetime
from heap import Heap

class PQNode(object):
    def __init__(self, value, priority=0):
        self.value = value
        self.priority = priority
        self.birth = datetime.datetime.now()

    def __cmp__(self, other):
        if self.priority<other.priority:
            return -1
        elif self.priority>other.priority:
            return 1
        elif self.priority == other.priority:
            if self.birth > other.birth:
                return -1
            if self.birth < other.birth:
                return 1
            else:
                return 0

    def __str__(self):
        return u"(Value: {}, Priority: {}, Birthdate: {})".format(
            self.value, self.priority, self.birth)

    def __repr__(self):
        return u"(Value: {}, Priority: {}, Birthdate: {})".format(
            self.value, self.priority, self.birth)

class PriorityQ(Heap):
    def __init__(self):
        super(PriorityQ, self).__init__()


    def push(self, value, priority=0):
        node = PQNode(value, priority)
        Heap.push(self, node)

    def __str__(self):
        retval = []
        for val in self.core:
            retval.append("{}".format(val))
        return ", ".join(retval)
        # return retval


"""
     __cmp__ should return a negative integer if self < other, zero if self == other, and 
     positive if self > other. It's usually best to define each comparison you need rather 
     than define them all at once, but __cmp__ can be a good way to save repetition and improve
      clarity when you need all comparisons implemented with similar criteria.
__eq__(self, other)

Defines behavior for the equality operator, ==.
__ne__(self, other)
Defines behavior for the inequality operator, !=.
__lt__(self, other)
Defines behavior for the less-than operator, <.
__gt__(self, other)
Defines behavior for the greater-than operator, >.
__le__(self, other)
Defines behavior for the less-than-or-equal-to operator, <=.
__ge__(self, other)
Defines behavior for the greater-than-or-equal-to operator, >=.
"""