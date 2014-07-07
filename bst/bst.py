from queue import Queue


class Bst(object):
    u"""A representation of a binary search tree."""
    def __init__(self):
        super(Bst, self).__init__()
        self._nodes = {}  # nodes[node] = [Left, Right, Parent]
        self._root = None

    def contains(self, val):
        u"""Return True if val is in the tree and False otherwise."""
        return bool(self._nodes.get(val, False))

    def insert_poorly(self, val):
        u"""Add a val to the tree if it is not already in the tree."""
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

    def insert(self, val):
        u"""Add a val to the tree if it is not already in the tree."""
        if not self.contains(val):
            if self._root is None:
                self._root = val
                self._nodes[val] = [None, float('inf'), None]
                return

            node = self._root

            while True:
                if node is None:
                    self._nodes[val] = [None, float('inf'), parent]
                    self._nodes[parent][0] = val
                    return
                if node == float('inf'):
                    self._nodes[val] = [None, float('inf'), parent]
                    self._nodes[parent][1] = val
                    return
                left, right = self._nodes[node][0:2]
                parent = node
                if val > node:
                    node = right
                elif val < node:
                    node = left

    def size(self):
        u"""Return the number of nodes in the tree."""
        return len(self._nodes.keys())

    def depth(self):
        u"""Return the number of nodes in the deepest branch."""
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
        u"""Return an int representing how well balanced the tree is."""
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

    def pre_order(self, node):
        u"""Return a generator with nodes traversed in pre-order."""
        if node is None or node == float('inf'):
            return
        else:
            yield node
            left, right = self._nodes[node][0:2]
            for i in self.pre_order(left):
                yield i
            for i in self.pre_order(right):
                yield i

    def in_order(self, node):
        u"""Return a generator with nodes traversed in order."""
        if node is None or node == float('inf'):
            return
        else:
            left, right = self._nodes[node][0:2]
            for i in self.in_order(left):
                yield i
            yield node
            for i in self.in_order(right):
                yield i

    def post_order(self, node):
        u"""Return a generator with nodes traversed in post-order."""
        if node is None or node == float('inf'):
            return
        else:
            left, right = self._nodes[node][0:2]
            for i in self.post_order(left):
                yield i
            for i in self.post_order(right):
                yield i
            yield node

    def breadth_first_traversal(self):
        u"""Return a generator with nodes traversed in level-order."""
        node = self._root
        q = Queue()
        q.enqueue(node)
        traversed = []
        while len(traversed) < self.size():
            try:
                node = q.dequeue()
                traversed.append(node)
                children = self._nodes[node][0:2]
                for child in children:
                    if child is not None and child != float('inf'):
                        q.enqueue(child)
                yield traversed[-1]
            except KeyError:
                break



    def display(self):
        node = self._root

        q = Queue()
        q.enqueue(node)
        traversed = []
        while len(traversed) < self.size():
            try:
                node = q.dequeue()
                traversed.append(node)
                children = self._nodes[node][0:2]
                for child in children:
                    if child is not None and child != float('inf'):
                        q.enqueue(child)
                yield traversed[-1]
            except KeyError:
                break


if __name__ == '__main__':
    bst = Bst()
    bst.insert(8)
    bst.insert(10)
    bst.insert(4)
    bst.insert(15)
    bst.insert(7)
    bst.insert(3)
    _list = []
    for node in bst.breadth_first_traversal():
        _list.append(node)
