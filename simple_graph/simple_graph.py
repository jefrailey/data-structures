class Graph(object):
    """docstring for Graph"""
    def __init__(self):
        self._nodes = []
        self._edges = []

    def nodes(self):
        return self._nodes

    def edges(self):
        return self._edges

    def add_node(self, name):
        self._nodes.append(Node(name))



class Node(object):
    """docstring for Node"""
    def __init__(self, name):
        super(Node, self).__init__()
        self.name = name


class Edge(object):
    """docstring for Edge"""
    def __init__(self, name):
        super(Edge, self).__init__()
        self.name = name


"""
Graph contains nodes
Nodes contain edges
"""
