class Graph(object):
    """docstring for Graph"""
    def __init__(self):
        self._nodes = []
        self._edges = []

    def nodes(self):
        return self._nodes

    def edges(self):
        return self._edges


class Node(object):
    """docstring for Node"""
    def __init__(self, arg):
        super(Node, self).__init__()
        self.arg = arg


class Edge(object):
    """docstring for Edge"""
    def __init__(self, arg):
        super(Edge, self).__init__()
        self.arg = arg


"""
Graph contains nodes
Nodes contain edges
"""
