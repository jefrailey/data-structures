class Graph(object):
    """docstring for Graph"""
    def __init__(self):
        self._nodes = set()
        self._edges = set()

    def nodes(self):
        return self._nodes

    def edges(self):
        return self._edges

    def add_node(self, name):
        self._nodes.add(name)

    def add_edge(self, node1, node2):
        if node1 not in self.nodes():
            self.add_node(node1)
        if node2 not in self.nodes():
            self.add_node(node2)
        if (node1, node2) and (node2, node1) not in self.edges():
            self._edges.add((node1, node2))

    def del_node(self, node):
        if node in self.nodes():
            self._nodes.remove(node)
            edges = self.edges().copy()
            for edge in edges:  # Del while iterating? Or does the return val make thisokay?
                if node in edge:
                    self._edges.remove(edge)
        else:
            raise ValueError(u"Node not found")

    def del_edge(self, node1, node2):
        try:
            self._edges.remove((node1, node2))
        except KeyError:
            self._edges.remove((node2, node1))

    def has_node(self, node):
        return node in self.nodes()
