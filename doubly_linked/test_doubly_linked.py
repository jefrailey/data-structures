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
    u"""Assert .insert() adds a value/node to the h of the doubly linked list."""
    doubly_linked = DoublyLinked()
    for val in values:
        doubly_linked.insert(val)
        assert doubly_linked.h.value == val
    assert doubly_linked.h.value == values[-1]


def test_append():
    u"""Assert .append() adds a value to the t of the doubly linked list."""
    doubly_linked = DoublyLinked()
    for val in values:
        doubly_linked.append(val)
        assert doubly_linked.t.value == val
    assert doubly_linked.t.value == values[-1]


def test_pop():
    u"""Assert .pop() removes and returns the h value from the list."""
    doubly_linked = DoublyLinked()
    for val in values:
        doubly_linked.append(val)
    for val in values:
        assert doubly_linked.pop() == val
    assert doubly_linked.pop() == None


def test_shift():
    u"""Assert .shift() removes and returns the t value from the list."""
    doubly_linked = DoublyLinked()
    for val in values:
        doubly_linked.insert(val)
    for val in values:
        assert doubly_linked.shift() == val
    assert doubly_linked.shift() == None


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