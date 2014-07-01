from weighted_graph import WeightedGraph
from shortest_path import dijkstra


def test_shortest_path_simple():
    wg = WeightedGraph()
    wg.add_edge('S', 'A', 1)
    wg.add_edge('A', 'E', 3)
    wg.add_edge('S', 'E', 3)
    path, distance = dijkstra(wg, 'S', 'E')
    assert path == ['S', 'E']
    assert distance == 3
