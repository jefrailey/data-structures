from simple_graph import Graph
import pytest


def test_nodes_empty():
    g = Graph()
    assert g.nodes() == []


def test_nodes():
    g = Graph()
    nodes = g.nodes()
    pass
