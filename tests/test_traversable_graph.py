from data_structures.graphs.traversable_graph import TraversableGraph

g = TraversableGraph()
g.add_edge(u"A", u"C")
g.add_edge(u"A", u"B")
g.add_edge(u"A", u"D")
g.add_edge(u"D", u"E")

circle = TraversableGraph()
circle.add_edge(u"A", u"B")
circle.add_edge(u"B", u"C")
circle.add_edge(u"C", u"D")
circle.add_edge(u"D", u"A")
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


def test_depth_reg():
    ans = g.depth_first_traversal(u"B")
    expected = (
        [u"B", u"A", u"C", u"D", u"E"],
        [u"B", u"A", u"D", u"E", u"C"]
    )
    assert ans in expected


def test_breadth_reg():
    ans = g.breadth_first_traversal(u"B")
    expected = (
        [u"B", u"A", u"C", u"D", u"E"],
        [u"B", u"A", u"D", u"C", u"E"]
    )
    assert ans in expected


def test_depth_circle():
    ans = circle.depth_first_traversal(u"A")
    expected = (
        [u"A", u"B", u"C", u"D", u"E"],
        [u"A", u"D", u"C", u"B", u"E"]
    )
    assert ans in expected


def test_breadth_circle():
    ans = circle.breadth_first_traversal(u"A")
    expected = (
        [u"A", u"B", u"D", u"C", u"E"],
        [u"A", u"D", u"B", u"C", u"E"]
    )
    assert ans in expected


def test_depth_spider():
    ans = d.depth_first_traversal(u"Head")
    expected = (
        [u"Head", u"A", u"B", u"C", 1, 2, 3],
        [u"Head", 1, 2, 3, u"A", u"B", u"C"]
    )
    assert ans in expected


def test_breadth_spider():
    ans = d.breadth_first_traversal(u"Head")
    expected = (
        [u"Head", 1, u"A", 2, u"B", 3, u"C"],
        [u"Head",  u"A", 1, u"B", 2, u"C", 3]
    )
    assert ans in expected


def test_depth_just_node():
    ans = just_nodes.depth_first_traversal(u"A")
    assert ans == [u"A"]


def test_breadth_just_nodes():
    ans = just_nodes.breadth_first_traversal(u"B")
    assert ans == [u"B"]
