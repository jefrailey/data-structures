class Graph(object):
    """docstring for Graph"""
    def __init__(self):
        self._nodes = set()
        self._edges = set()
        self.edgeWeights = {}

    def nodes(self):
        return self._nodes

    def edges(self):
        return self._edges

    def add_node(self, name):
        self._nodes.add(name)

    def add_edge(self, node1, node2, weight):
        if node1 not in self.nodes():
            self.add_node(node1)
        if node2 not in self.nodes():
            self.add_node(node2)
        if (node1, node2) and (node2, node1) not in self.edges():
            self._edges.add((node1, node2))
            self.edgeWeights[(node1, node2)] = weight
            return True
        self.edgeWeights[(node1, node2)] = weight
        return False

    def del_node(self, node):
        if node in self.nodes():
            self._nodes.remove(node)
            edges = self.edges().copy()
            for edge in edges:  # Can this be done without copying the set?
                if node in edge:
                    self._edges.remove(edge)
        else:
            raise ValueError(u"Node not found")

    def del_edge(self, node1, node2):
        self.edgeWeights.pop((node1, node2), False)
        self.edgeWeights.pop((node2, node1), False)
        try:
            self._edges.remove((node1, node2))
        except KeyError:
            self._edges.remove((node2, node1))

    def has_node(self, node):
        return node in self.nodes()

    def adjacent(self, node1, node2):
        if node1 not in self.nodes() or node2 not in self.nodes():
            raise KeyError
        elif (node1, node2) not in self.edges() and (node2, node1)\
                not in self.edges():
            return False
        else:
            return True

    def neighbors(self, node):
        if node not in self.nodes():
            raise KeyError
        else:
            retlist = []
            for node1, node2 in self.edges():
                if node1 == node:
                    retlist.append(node2)
                elif node2 == node:
                    retlist.append(node1)
        return retlist
