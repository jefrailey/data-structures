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