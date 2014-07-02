from bst import Bst


def test_initalize_is_Bst():
    bst = Bst()
    assert isinstance(bst, Bst)


def test_initialize_empty():
    bst = Bst()
    assert bst._nodes == {}


def test_insert():
    raise AssertionError


def test_contains_true():
    bst = Bst()
    bst._nodes[1] = (0, None, 2)
    assert bst.contains(1) is True


def test_contains_false():
    bst = Bst()
    bst._nodes[1] = (0, None, 2)
    assert bst.contains(2) is False


def test_size():
    raise AssertionError


def test_depth():
    raise AssertionError


def test_balance():
    raise AssertionError