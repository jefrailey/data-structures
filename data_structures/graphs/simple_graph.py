class Graph(object):

    u"""A simple undirected graph."""

    def __init__(self):
        self._nodes = set()
        self._edges = set()

    def nodes(self):
        u"""Return a list of nodes in the graph."""
        return list(self._nodes)

    def edges(self):
        u"""Return a list of edges in the graph."""
        return list(self._edges)

    def add_node(self, name):
        u"""Add a node to the graph."""
        self._nodes.add(name)

    def add_edge(self, node1, node2):
        u"""Add an edge to the graph and corresponding nodes."""
        if node1 not in self.nodes():
            self.add_node(node1)
        if node2 not in self.nodes():
            self.add_node(node2)
        if (node1, node2) and (node2, node1) not in self.edges():
            self._edges.add((node1, node2))

    def del_node(self, node):
        u"""Remove node and corresponding edges from the graph."""
        if node in self.nodes():
            self._nodes.remove(node)
            edges = self.edges()
            for edge in edges:  # Can this be done without copying the set?
                if node in edge:
                    self._edges.remove(edge)
        else:
            raise ValueError(u"Node not found")

    def del_edge(self, node1, node2):
        u"""Remove edge between node1 and node2 from the graph."""
        try:
            self._edges.remove((node1, node2))
        except KeyError:
            self._edges.remove((node2, node1))

    def has_node(self, node):
        u"""Return True if node is in the graph; False if not."""
        return node in self.nodes()

    def adjacent(self, node1, node2):
        u"""Return True if node1 and node2 are adjacent; False if not."""
        if node1 not in self.nodes() or node2 not in self.nodes():
            raise KeyError
        elif (node1, node2) not in self.edges() and (
                (node2, node1) not in self.edges()):
            return False
        else:
            return True

    def neighbors(self, node):
        u"""Return a list of nodes adjacent to a node."""
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
