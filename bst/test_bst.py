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
    assert bst._nodes[7] == [None, float('inf'), 6]
    assert bst._nodes[10] == [9, float('inf'), 8]


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
    bst = Bst()
    bst.insert(8)
    bst.insert(10)
    bst.insert(3)
    bst.insert(6)
    bst.insert(7)
    bst.insert(9)
    assert bst.balance() == 1


def test_balance_long_right_side():
    bst = Bst()
    bst.insert(8)
    bst.insert(10)
    bst.insert(11)
    bst.insert(13)
    bst.insert(15)
    bst.insert(19)
    assert bst.balance() == 5


def test_balance_long_left_side():
    bst = Bst()
    bst.insert(8)
    bst.insert(7)
    bst.insert(6)
    bst.insert(5)
    bst.insert(4)
    bst.insert(3)
    assert bst.balance() == -5


def test_balance_three_nodes():
    bst = Bst()
    bst.insert(7)
    bst.insert(8)
    bst.insert(6)
    assert bst.balance() == 0


def test_in_order():
    bst = Bst()
    vals = [37, 22, 6, 28, 17, 14]
    for val in vals:
        bst.insert(val)
    vals.sort()
    for i, g in enumerate(bst.in_order(37)):
        assert g == vals[i]


def test_in_order_2():
    bst = Bst()
    vals = [44, 19, 6, 7, 8]
    for val in vals:
        bst.insert(val)
    vals.sort()
    for i, g in enumerate(bst.in_order(44)):
        assert g == vals[i]


def test_in_order_long():
    bst = Bst()
    vals = range(100, 0, -3)
    for val in vals:
        bst.insert(val)
    vals.sort()
    for i, g in enumerate(bst.in_order(100)):
        assert g == vals[i]


def test_breadth_all_left():
    bst = Bst()
    bst.insert(8)
    bst.insert(7)
    bst.insert(6)
    bst.insert(5)
    bst.insert(4)
    bst.insert(3)
    _list = []
    for node in bst.breadth_first_traversal():
        _list.append(node)

    assert _list == [8, 7, 6, 5, 4, 3]


def test_breadth_complex():
    bst = Bst()
    bst.insert(8)
    bst.insert(10)
    bst.insert(4)
    bst.insert(15)
    bst.insert(7)
    bst.insert(3)
    _list = []
    for node in bst.breadth_first_traversal():
        _list.append(node)

    assert _list == [8, 4, 10, 3, 7, 15]
