from simple_graph import Graph
from simple_graph import Node
from simple_graph import Edge


def test_nodes_empty():
    g = Graph()
    assert g.nodes() == []


def test_nodes():
    g = Graph()
    nodes = g.nodes()
    pass


def test_edges_empty():
    g = Graph()
    assert g.edges() == []


def test_node_init():
    n = Node("A")
    assert n.name == "A"


def test_add_node():
    g = Graph()
    g.add_node("A")
    assert g.nodes()[0].name == u"A"


def test_add_edge():
    g = Graph()
    g.add_node(u"A")
    g.add_node(u"B")
    g.add_edge(u"A", u"B")
    assert g.edges()[0].name == (u"A", u"B")


def test_add_edge_one_new_node():
    g = Graph()
    g.add_node(u"A")
    g.add_edge(u"A", u"C")
    assert u"C" in g.nodes()
    assert g.edges()[0].name == (u"A", u"C")


def test_add_edge_two_new_nodes():
    g = Graph()
    g.add_edge(u"A", u"C")
    assert u"A" in g.nodes()
    assert u"C" in g.nodes()
    assert g.edges()[0].name == (u"A", u"C")