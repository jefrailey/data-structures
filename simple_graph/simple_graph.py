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


# class Node(object):
#     """docstring for Node"""
#     def __init__(self, name):
#         super(Node, self).__init__()
#         self.name = name


# class Edge(object):
#     """docstring for Edge"""
#     def __init__(self, name):
#         super(Edge, self).__init__()
#         self.name = name


"""
Graph contains nodes
Nodes contain edges
"""
