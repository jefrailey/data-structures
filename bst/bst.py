class Bst(object):
    """docstring for Bst"""
    def __init__(self):
        super(Bst, self).__init__()
        self._nodes = {}  # nodes[node] = [Left, Right, Parent]

    def insert(self, val):
        pass

    def contains(self, val):
        return bool(self._nodes.get(val, False))

    def size(self):
        pass

    def depth(self):
        pass

    def balance(self):
        pass