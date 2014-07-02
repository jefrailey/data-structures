from bst import Bst


def test_initalize_is_Bst():
    bst = Bst()
    assert isinstance(bst, Bst)


def test_initialize_empty():
    bst = Bst()
    assert bst._nodes == {}


def test_insert_no_root():
    bst = Bst()
    bst.insert(8)
    assert bst._root == 8


def test_insert_smaller_than_root():
    bst = Bst()
    bst.insert(8)
    bst.insert(3)
    assert bst._root == 8


def test_insert_bigger_than_root():
    bst = Bst()
    bst.insert(8)
    bst.insert(10)
    assert bst._root == 8


def test_insert_smaller_and_bigger_than_root():
    bst = Bst()
    bst.insert(8)
    bst.insert(10)
    bst.insert(3)
    assert bst._nodes[bst._root] == [3, 10, None]


def test_insert_multiple_vals():
    bst = Bst()
    bst.insert(8)
    bst.insert(10)
    bst.insert(3)
    bst.insert(6)
    bst.insert(7)
    bst.insert(9)
    assert bst._nodes[7] == [6, float('inf'), 8]
    assert bst._nodes[9] == [None, 10, 8]


def test_contains_true():
    bst = Bst()
    bst._nodes[1] = (0, None, 2)
    assert bst.contains(1) is True


def test_contains_false():
    bst = Bst()
    bst._nodes[1] = (0, None, 2)
    assert bst.contains(2) is False


def test_size():
    bst = Bst()
    bst.insert(8)
    bst.insert(10)
    bst.insert(3)
    bst.insert(6)
    bst.insert(7)
    bst.insert(9)
    assert bst.size() == 6


def test_depth():
    bst = Bst()
    bst.insert(8)
    bst.insert(10)
    bst.insert(3)
    bst.insert(6)
    bst.insert(7)
    bst.insert(9)
    assert bst.depth() == 3


def test_balance():
    raise AssertionError