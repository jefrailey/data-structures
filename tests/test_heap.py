from data_structures.heap import Heap
import random

NUMBERS = (
    9, 10, 11, 12, 8, 53,
    32, 45, 7, 52, 13, 0,
    1, 14, 76, 34, 15,
    4, 16, 3, 6, 17, 55,
    234, 256, 144, 999,
    426, 2, 337, 23, 25
)


def _build_a_heap():
    heap = Heap()
    while len(heap) < len(NUMBERS):
        heap.push(random.choice(NUMBERS))
    return heap


def test_init():
    u"""Assert the succesful initiation of heap object."""
    heap = Heap()
    assert isinstance(heap, Heap)


def test_push():
    u"""Assert that the heap has correct head through multiple pushes."""
    heap = Heap()
    numsPushed = []
    for num in NUMBERS:
        heap.push(num)
        numsPushed.append(num)
        assert heap[0] == max(numsPushed)


def test_pop_removes_head():
    u"""Assert that pop removes the head."""
    heap = _build_a_heap()
    for num in NUMBERS:
        a = heap[0]
        assert heap.pop() == a
    assert heap.pop() is None


def test_pop_reorganizes():
    u"""Assert that pop properly reorganizes."""
    heap = _build_a_heap()
    nums_in_heap = heap[:]
    nums_in_heap.sort(reverse=True)
    for i, _ in enumerate(NUMBERS):
        assert heap.pop() == nums_in_heap[i]
