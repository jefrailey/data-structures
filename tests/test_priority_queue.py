import random
from data_structures.priority_queue import PriorityQ, PQNode

NUMBERS = (
    2, 4, 3, 7, 8, 53,
    32, 45, 7, 52, 4,
    1, 3, 76, 34, 23,
    4, 3, 3, 6, 2, 55,
    234, 256, 144,
    999, 426, 2
)
BIRTHORDER = (1,) * 18

TEST_PRIORITY = zip(BIRTHORDER, xrange(18))


def _build_queue(numbers=NUMBERS):
    priorityQ = PriorityQ()
    while len(priorityQ) < len(numbers):
        priorityQ.push(random.choice(numbers))
    return priorityQ


def test_init():
    u"""Assert the succesful initiation of priorityQ object."""
    priorityQ = PriorityQ()
    assert isinstance(priorityQ, PriorityQ)


def test_push():
    u"""Assert that the priorityQ has correct head through multiple pushes."""
    priorityQ = PriorityQ()
    numsPushed = []
    for num in NUMBERS:
        priorityQ.push(num)
        numsPushed.append(PQNode(num))
        assert priorityQ[0] != max(numsPushed)


def test_pop_removes_head():
    u"""Assert that pop removes the head."""
    priorityQ = _build_queue()
    for num in NUMBERS:
        head_value = priorityQ[0]
        assert priorityQ.pop() == head_value
    assert priorityQ.pop() is None


def test_pop_reorganizes():
    u"""Assert that pop properly reorganizes."""
    priorityQ = _build_queue()
    nums_in_heap = priorityQ[:]
    nums_in_heap.sort(reverse=True)
    for i, _ in enumerate(NUMBERS):
        assert priorityQ.pop() == nums_in_heap[i]


def test_pop_reorganizes_birthorder():
    u"""Assert that pop properly reorganizes."""
    priorityQ = _build_queue(BIRTHORDER)
    nums_in_heap = priorityQ[:]
    nums_in_heap.sort(reverse=True)
    for i, _ in enumerate(BIRTHORDER):
        assert priorityQ.pop() == nums_in_heap[i]


def test_pop_reorganizes_priority():
    u"""Assert that pop properly reorganizes."""
    priorityQ = _build_queue(TEST_PRIORITY)
    nums_in_heap = priorityQ[:]
    nums_in_heap.sort(reverse=True)
    for i, _ in enumerate(TEST_PRIORITY):
        assert priorityQ.pop() == nums_in_heap[i]


def test_peak(numbers=NUMBERS):
    u"""Assert that pop removes the head."""
    priorityQ = PriorityQ()
    while len(priorityQ) < len(numbers):
        priorityQ.push(random.choice(numbers))
        assert priorityQ.peek() == max(priorityQ.core)
