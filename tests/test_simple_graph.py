import pytest
from data_structures.graphs.simple_graph import Graph


def test_nodes_empty():
    g = Graph()
    assert g.nodes() == []


def test_edges_empty():
    g = Graph()
    assert g.edges() == []


def test_add_node():
    g = Graph()
    g.add_node("A")
    assert "A" in g.nodes()


def test_add_edge():
    g = Graph()
    g.add_node(u"A")
    g.add_node(u"B")
    g.add_edge(u"A", u"B")
    assert (u"A", u"B") in g.edges()


def test_add_edge_one_new_node():
    g = Graph()
    g.add_node(u"A")
    g.add_edge(u"A", u"C")
    assert u"C" in g.nodes()
    assert (u"A", u"C") in g.edges()


def test_add_edge_two_new_nodes():
    g = Graph()
    g.add_edge(u"A", u"C")
    assert u"A" in g.nodes()
    assert u"C" in g.nodes()
    assert (u"A", u"C") in g.edges()


def test_del_node():
    g = Graph()
    g.add_edge(u"A", u"C")
    g.del_node(u"A")
    assert u"A" not in g.nodes()
    assert (u"A", u"C") not in g.edges()


def test_del_edge():
    g = Graph()
    g.add_edge(u"A", u"C")
    g.del_edge(u"A", u"C")
    assert (u"A", u"C") not in g.edges()
    assert u"A" in g.nodes()
    assert u"C" in g.nodes()


def test_has_node():
    g = Graph()
    g.add_node(u"A")
    g.add_node(u"B")
    assert g.has_node(u"A") is True
    assert g.has_node(u"C") is False


def test_adjacent():
    g = Graph()
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
    g = Graph()
    g.add_edge(u"A", u"C")
    g.add_edge(u"A", u"B")
    g.add_edge(u"A", u"D")
    g.add_edge(u"D", u"E")
    assert u"B" in g.neighbors(u"A")
    assert u"C" in g.neighbors(u"A")
    assert u"D" in g.neighbors(u"A")


def test_del_node_node_not_found():
    g = Graph()
    g.add_edge(u"D", u"E")
    with pytest.raises(ValueError):
        g.del_node(u"A")


def test_del_edge_edge_not_found():
    g = Graph()
    g.add_edge(u"A", u"C")
    with pytest.raises(ValueError):
        g.del_edge(u"B", u"D")


def test_adjacent_node_not_found():
    g = Graph()
    g.add_edge(u"A", u"C")
    with pytest.raises(KeyError):
        g.adjacent(u"B", u"D")
        g.adjacent(u"A", u"D")
        g.adjacent(u"B", u"C")


def test_neighbors_node_not_found():
    g = Graph()
    g.add_edge(u"A", u"C")
    with pytest.raises(KeyError):
        g.neighbors(u"B")
