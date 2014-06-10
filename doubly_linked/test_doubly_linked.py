from doubly_linked import DoublyLinked, Node
import pytest
import random

values = (u'a', 1, True, None, False, 0)


def test_Node_init():
    u"""Assert a Node instantiates with a given value."""
    for val in values:
        node = Node(val)
        assert isinstance(node, Node)
        assert node.value == val


def test_DoublyLinked_init():
    u"""Assert a DoublyLinked list instantiates with a given values."""
    doubly_linked = DoublyLinked()
    assert isinstance(doubly_linked, DoublyLinked)


def test_insert():
    u"""Assert .insert() adds a value to the head of the doubly linked list."""
    doubly_linked = DoublyLinked()
    for val in values:
        doubly_linked.insert(val)
        assert doubly_linked.head.value == val
    assert doubly_linked.head.val == values[-1]


def test_append():
    u"""Assert .append() adds a value to the tail of the doubly linked list."""
    doubly_linked = DoublyLinked()
    for val in values:
        doubly_linked.append(val)
        assert doubly_linked.tail.value == val
    assert doubly_linked.tail.value == values[0]


def test_pop():
    u"""Assert .pop() removes and returns the head value from the list."""
    doubly_linked = DoublyLinked()
    for val in values:
        doubly_linked.append(val)
    for val in values:
        assert doubly_linked.pop() == val
    with pytest.raises(LookupError):  # Do we want pop to return None instead?
        doubly_linked.pop()


def test_shift():
    u"""Assert .shift() removes and returns the tail value from the list."""
    doubly_linked = DoublyLinked()
    for val in values:
        doubly_linked.insert(val)
    for val in values:
        assert doubly_linked.shift() == val
    with pytest.raises(LookupError):  # Do we want shift to return None ?
        doubly_linked.shift()


def test_remove():
    u"""Assert .remove() removes the first matching value from the list."""
    doubly_linked = DoublyLinked()
    for val in values:
        doubly_linked.insert(val)
    test_vals = values[:]
    while test_vals:
        val = random.choice(test_vals)
        removed_node = doubly_linked.remove(val)
        assert removed_node.value == val
        test_vals.remove(val)
    doubly_linked.insert(1)
    with pytest.raises(LookupError):
        doubly_linked.remove("test value")