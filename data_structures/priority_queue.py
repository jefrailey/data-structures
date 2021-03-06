import datetime
from heap import Heap


class PQNode(object):
    def __init__(self, value, priority=0):
        self.value = value
        self.priority = priority
        self.birth = datetime.datetime.now()

    def __cmp__(self, other):
        if self.priority < other.priority:
            return -1
        elif self.priority > other.priority:
            return 1
        elif self.priority == other.priority:
            if self.birth > other.birth:
                return -1
            if self.birth < other.birth:
                return 1
            else:
                return 0

    def __unicode__(self):
        return u"(Value: {}, Priority: {}, Birthdate: {})".format(
            self.value, self.priority, self.birth)

    def __repr__(self):
        return u"(Value: {}, Priority: {}, Birthdate: {})".format(
            self.value, self.priority, self.birth)

    def __str__(self):
        return unicode(self).encode('utf-8')


class PriorityQ(Heap):
    def __init__(self):
        super(PriorityQ, self).__init__()

    def push(self, value, priority=0):
        node = PQNode(value, priority)
        Heap.push(self, node)

    def peek(self):
        return self.core[0]

    def __unicode__(self):
        retval = []
        for val in self.core:
            retval.append(u"{}".format(val))
        return u", ".join(retval)

    def __str__(self):
        return unicode(self).encode('utf-8')
