from weighted_graph import WeightedGraph
import pytest


def test_nodes_empty():
    g = WeightedGraph()
    assert g.nodes() == set()


def test_edges_empty():
    g = WeightedGraph()
    assert g.edges() == set()


def test_add_node():
    g = WeightedGraph()
    g.add_node("A")
    assert "A" in g.nodes()


def test_add_edge():
    g = WeightedGraph()
    g.add_node(u"A")
    g.add_node(u"B")
    g.add_edge(u"A", u"B")
    assert (u"A", u"B") in g.edges()


def test_add_edge_one_new_node():
    g = WeightedGraph()
    g.add_node(u"A")
    g.add_edge(u"A", u"C")
    assert u"C" in g.nodes()
    assert (u"A", u"C") in g.edges()


def test_add_edge_two_new_nodes():
    g = WeightedGraph()
    g.add_edge(u"A", u"C")
    assert u"A" in g.nodes()
    assert u"C" in g.nodes()
    assert (u"A", u"C") in g.edges()


def test_del_node():
    g = WeightedGraph()
    g.add_edge(u"A", u"C")
    g.del_node(u"A")
    assert u"A" not in g.nodes()
    assert (u"A", u"C") not in g.edges()


def test_del_edge():
    g = WeightedGraph()
    g.add_edge(u"A", u"C")
    g.del_edge(u"A", u"C")
    assert (u"A", u"C") not in g.edges()
    assert u"A" in g.nodes()
    assert u"C" in g.nodes()
    assert g.edgeWeights.pop((u"A", u"C"), False) == False


def test_has_node():
    g = WeightedGraph()
    g.add_node(u"A")
    g.add_node(u"B")
    assert g.has_node(u"A") is True
    assert g.has_node(u"C") is False


def test_adj():
    g = WeightedGraph()
    g.add_edge(u"A", u"C")
    g.add_node(u"B")
    print g.edges()
    assert g.adjacent(u"A", u"C") is True
    assert g.adjacent(u"C", u"A") is True
    assert g.adjacent(u"B", u"C") is False
    assert g.adjacent(u"B", u"A") is False
    with pytest.raises(KeyError):
        g.adjacent(u"A", u"D")


def test_neighbors():
    g = WeightedGraph()
    g.add_edge(u"A", u"C")
    g.add_edge(u"A", u"B")
    g.add_edge(u"A", u"D")
    g.add_edge(u"D", u"E")
    assert u"B" in g.neighbors(u"A")
    assert u"C" in g.neighbors(u"A")
    assert u"D" in g.neighbors(u"A")


def test_add_edge_weight():
    g = WeightedGraph()
    g.add_node(u"A")
    g.add_edge(u"A", u"C", 10)
    assert g.edgeWeights[(u"A", u"C")] == 10


def test_add_multiple_edge_weight():
    g = WeightedGraph()
    g.add_node(u"A")
    g.add_edge(u"A", u"C", 10)
    g.add_edge(u"C", u"D", 5)
    g.add_edge(u"A", u"B", 1)
    g.add_edge(u"C", u"A", 5)
    assert g.edgeWeights[(u"A", u"C")] == 10
    assert g.edgeWeights[(u"C", u"A")] == 5
