import queue


def _make_empty_queue():
    q = Queue()
    return q


def _enqueue(q):
    q.enqueue('a')
    q.enqueue(1)
    q.enqueue(True)
    q.enqueue(None)
    q.enqueue(False)
    q.enqueue(0)
    return q


def test_init_queue():
    pass


def tests_init_node():
    pass


def test_enqueue():
    pass


def test_dequeue():
    # Need to test dequeue() on an empty queue, queue of 1 value, and a queue
    # with multiple values
    pass


def test_size():
    pass