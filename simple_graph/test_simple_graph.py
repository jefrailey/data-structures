from simple_graph import Graph


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