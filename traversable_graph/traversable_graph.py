from simple_graph import Graph
from stack import Stack
from queue import Queue

class TraversableGraph(Graph):
    """docstring for TraversableGraph"""
    def __init__(self):
        super(TraversableGraph, self).__init__()

    def depth_first_traversal(self, start):
        if start not in self.nodes():
            raise KeyError
        node = start
        stack = Stack()
        stack.push(node)
        traversed = []
        while len(traversed) < len(self.nodes()):
            try:
                node = stack.pop()
                print node
                traversed.insert(0, node)
                children = self.neighbors(node)
                for child in children:
                    if child not in traversed:
                       stack.push(child)
            except LookupError:
                break
        return traversed

    def breadth_first_traversal(self, start):
        if start not in self.nodes():
            raise KeyError
        node = start
        q = Queue()
        q.enqueue(node)
        traversed = []
        while len(traversed) < len(self.nodes()):
            try:
                node = q.dequeue()
                print node
                traversed.insert(0, node)
                children = self.neighbors(node)
                for child in children:
                    if child not in traversed:
                       q.enqueue(child)
            except LookupError:
                break
        return traversed

if __name__ == "__main__":
    g = TraversableGraph()
    g.add_edge(u"A", u"C")
    g.add_edge(u"A", u"B")
    g.add_edge(u"A", u"D")
    g.add_edge(u"D", u"E")

    circle = TraversableGraph()
    circle.add_edge(u"A", u"B")
    circle.add_edge(u"B", u"C")
    circle.add_edge(u"C", u"D")
    circle.add_edge(u"D", u"E")

    d = TraversableGraph()
    d.add_edge(u"Head", u"A")
    d.add_edge(u"Head", 1)
    d.add_edge(1, 2)
    d.add_edge(2, 3)
    d.add_edge(u"A", u"B")
    d.add_edge(u"B", u"C")

    just_nodes = TraversableGraph()
    just_nodes.add_node(u"A")
    just_nodes.add_node(u"B")
    just_nodes.add_node(u"C")
    just_nodes.add_node(u"D")
