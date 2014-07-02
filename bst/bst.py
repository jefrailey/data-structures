class Bst(object):
    """docstring for Bst"""
    def __init__(self):
        super(Bst, self).__init__()
        self._nodes = {}  # nodes[node] = [Left, Right, Parent]
        self._root = None

    def contains(self, val):
        return bool(self._nodes.get(val, False))

    def insert(self, val):
        if not self.contains(val):
            if self._root is None:
                self._nodes[val], self._root = [None, float('inf'), None], val
            else:
                node = self._root
                while True:
                    if isinstance(node, list):
                        print node
                    left, right, parent = self._nodes[node]
                    if (left < val) and (val < node):
                        try:
                            self._nodes[left][2] = val
                        except KeyError:
                            pass
                        self._nodes[node][0] = val
                        self._nodes[val] = [left, float('inf'), node]
                        break
                    elif (right > val) and (val > node):
                        try:
                            self._nodes[right][2] = val
                        except KeyError:
                            pass
                        self._nodes[node][1] = val
                        self._nodes[val] = [None, right, node]
                        break
                    elif val < left:
                        node = left
                        print node
                    elif val > right:
                        node = right
                        print node

    def size(self):
        return len(self._nodes.keys())

    def depth(self):
        depth = 0
        for k, v in self._nodes.items():
            left, right, parent = v
            if left is None and right == float('inf'):
                node = k
                count = 0
                while node != self._root:
                    node = self._nodes[node][2]
                    count += 1
                if count > depth:
                    depth = count
        return depth

    def balance(self, node=None, balance=0):
        if node is None:
            node = self._root
        left, right, parent = self._nodes[node]
        if left is not None:
            balance -= 1
            balance = self.balance(left, balance)
        if right != float('inf'):
            balance += 1
            balance = self.balance(right, balance)

        return balance
