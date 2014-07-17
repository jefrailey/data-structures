from data_structures.graphs.weighted_graph import WeightedGraph
from data_structures.graphs.shortest_path import dijkstra, bellman_ford_moore


def test_shortest_path_triangle_one_edge_path():
    wg = WeightedGraph()
    wg.add_edge('S', 'A', 1)
    wg.add_edge('A', 'E', 3)
    wg.add_edge('S', 'E', 3)
    path, distance = dijkstra(wg, 'S', 'E')
    assert path == ['S', 'E']
    assert distance == 3


def test_shortest_path_triangle_two_edge_path():
    wg = WeightedGraph()
    wg.add_edge('S', 'A', 1)
    wg.add_edge('A', 'E', 1)
    wg.add_edge('S', 'E', 3)
    path, distance = dijkstra(wg, 'S', 'E')
    assert path == ['S', 'A', 'E']
    assert distance == 2


def test_shortest_path_triangle_one_edge_path_bfm():
    wg = WeightedGraph()
    wg.add_edge('S', 'A', 1)
    wg.add_edge('A', 'E', 3)
    wg.add_edge('S', 'E', 3)
    path, distance = bellman_ford_moore(wg, 'S', 'E')
    assert path == ['S', 'E']
    assert distance == 3


def test_shortest_path_triangle_two_edge_path_bfm():
    wg = WeightedGraph()
    wg.add_edge('S', 'A', 1)
    wg.add_edge('A', 'E', 1)
    wg.add_edge('S', 'E', 3)
    path, distance = bellman_ford_moore(wg, 'S', 'E')
    assert path == ['S', 'A', 'E']
    assert distance == 2
