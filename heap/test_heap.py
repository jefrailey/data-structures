from heap import Heap
import random

sample_numbers = [
    2, 4, 3, 7, 8, 53,
    32, 45, 7, 52, 4,
    1, 3, 76, 34, 23,
    4, 3, 3, 6, 2, 55,
    234, 256, 144,
    999, 426, 2
    ]


def _build_a_heap():
    heap = Heap()
    while len(heap) < len(sample_numbers):
        heap.push(random.choice(sample_numbers))
    return heap


def test_init():
    u"""Assert the succesful initiation of heap object."""
    heap = Heap()
    assert isinstance(heap, Heap)


def test_push():
    u"""Assert that the heap has correct head through multiple pushes."""
    heap = Heap()
    numsPushed = []
    for num in sample_numbers:
        heap.push(num)
        numsPushed.append(num)
        assert heap[0] == max(numsPushed)


def test_pop_removes_head():
    u"""Assert that pop removes the head."""
    heap = _build_a_heap()
    # print heap[0]
    for num in sample_numbers:
        a = heap[0]
        assert heap.pop() == a
    assert heap.pop() is None


def test_pop_reorganizes():
    u"""Assert that pop properly reorganizes."""
    heap = _build_a_heap()
    nums_in_heap = heap[:]
    nums_in_heap.sort()
    nums_in_heap = nums_in_heap[::-1]
    for i, num in enumerate(sample_numbers):
        print u"Heap: {}".format(heap[:])
        print u"Nums_in_heap: {}".format(nums_in_heap[i:])
        removed = heap.pop()
        print "Removed: {}\n nums_in_heap[i]: {}\n".format(removed, nums_in_heap[i])
        print len(nums_in_heap)
        print len(heap)
        while i>0:
            assert removed == nums_in_heap[i]
            break


        #AFRAID that tests might not be valid, last shift to left when popping a value COULD
        # put values into improper locations, use a slightly different push method to check for NONE values.
