from queue import Queue, Node

value_tuple = (u'a', 1, True, None, False, 0)


def test_init_queue():
    q = Queue()
    assert isinstance(q, Queue)


def tests_init_node():
    for val in value_tuple:
        n = Node(val)
        assert isinstance(n, Node)


def test_enqueue():
    q = Queue()
    for val in value_tuple:
        q.enqueue(val)
        assert q.head.value == value_tuple[0]
        assert q.tail.value == val


def test_dequeue():
    q = Queue()
    for val in value_tuple:
        q.enqueue(val)
    for val in value_tuple:
        q.dequeue()
        assert q.head.value == val
        assert q.tail.value == value_tuple[-1]


def test_size():
    q = Queue()
    for i, val in enumerate(value_tuple, 1):
        q.enqueue(val)
        assert q.size() == i