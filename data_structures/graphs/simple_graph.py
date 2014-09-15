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
        if node1 not in self._nodes:
            self.add_node(node1)
        if node2 not in self._nodes:
            self.add_node(node2)
        if (node1, node2) and (node2, node1) not in self._edges:
            self._edges.add((node1, node2))

    def del_node(self, node):
        u"""Remove node and corresponding edges from the graph."""
        if node in self._nodes:
            self._nodes.remove(node)
            edges = self.edges()
            for edge in edges:
                if node in edge:
                    self._edges.remove(edge)
        else:
            raise ValueError(u"Node, {}, not found".format(node))

    def del_edge(self, node1, node2):
        u"""Remove edge between node1 and node2 from the graph."""
        edge1, edge2 = (node1, node2), (node2, node1)
        try:
            self._edges.remove(edge1)
        except KeyError:
            try:
                self._edges.remove(edge2)
            except KeyError:
                raise ValueError(
                    u"Edge, {} and {}, not found".format(edge1, edge2)
                )

    def has_node(self, node):
        u"""Return True if node is in the graph; False if not."""
        return node in self._nodes

    def adjacent(self, node1, node2):
        u"""Return True if node1 and node2 are adjacent; False if not."""
        edge1, edge2 = (node1, node2), (node2, node1)
        if not self.has_node(node1):
            raise KeyError(u"Node, {}, not found".format(node1))
        elif not self.has_node(node2):
            raise KeyError(u"Node, {}, not found".format(node2))
        return edge1 in self._edges or edge2 in self._edges

    def neighbors(self, node):
        u"""Return a list of nodes adjacent to a node."""
        if node not in self._nodes:
            raise KeyError(u"Node, {}, not found".format(node))
        else:
            neighbors = []
            for node1, node2 in self._edges:
                if node1 == node:
                    neighbors.append(node2)
                elif node2 == node:
                    neighbors.append(node1)
        return neighbors
