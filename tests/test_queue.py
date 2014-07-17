from data_structures.queue import Queue
import pytest

value_tuple = (u'a', 1, True, None, False, 0)


def test_init_queue():
    u"""Test Queue init."""
    q = Queue()
    assert isinstance(q, Queue)


def test_enqueue():
    u"""Asserts nodes are added and hold their own value."""
    q = Queue()
    for val in value_tuple:
        q.enqueue(val)
        assert q.list.head_node.value == val


def test_dequeue():
    u"""Asserts nodes are properly removed."""
    q = Queue()
    for val in value_tuple:
        q.enqueue(val)
    for val in value_tuple:
        if q.list.head_node:
            assert q.dequeue() == val
        else:
            with pytest.raises(LookupError):
                q.dequeue()


def test_size():
    u"""Asserts size of Queue remains as expected during enqueue process."""
    q = Queue()
    for i, val in enumerate(value_tuple, 1):
        q.enqueue(val)
        assert q.size() == i
