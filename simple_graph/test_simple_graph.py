from simple_graph import Graph as g
import pytest


def test_nodes_empty():
    with pytest.raises(AttributeError):
        nodes = g.nodes()


def test_nodes():
    nodes = g.nodes()
    pass
