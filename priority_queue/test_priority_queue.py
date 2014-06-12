from priority_queue import PriorityQ, PQNode
import random

sample_numbers = [
    2, 4, 3, 7, 8, 53,
    32, 45, 7, 52, 4,
    1, 3, 76, 34, 23,
    4, 3, 3, 6, 2, 55,
    234, 256, 144,
    999, 426, 2
    ]
_test_birthorder = [
    1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1
]

_test_priority = zip(_test_birthorder, xrange(18))

def _build_a_heap(numbers=sample_numbers):
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
    for num in sample_numbers:
        priorityQ.push(num)
        numsPushed.append(PQNode(num))
        assert priorityQ[0] != max(numsPushed)


def test_pop_removes_head():
    u"""Assert that pop removes the head."""
    priorityQ = _build_a_heap()
    # print priorityQ[0]
    for num in sample_numbers:
        a = priorityQ[0]
        assert priorityQ.pop() == a
    assert priorityQ.pop() is None


def test_pop_reorganizes():
    u"""Assert that pop properly reorganizes."""
    priorityQ = _build_a_heap()
    nums_in_heap = priorityQ[:]
    nums_in_heap.sort()
    nums_in_heap = nums_in_heap[::-1]
    for i, num in enumerate(sample_numbers):
        print u"PriorityQ: {}".format(priorityQ[:])
        print u"Nums_in_heap: {}".format(nums_in_heap[i:])
        removed = priorityQ.pop()
        print "Removed: {}\n nums_in_heap[i]: {}\n".format(removed, nums_in_heap[i])
        print len(nums_in_heap)
        print len(priorityQ)
        while i>0:
            assert removed == nums_in_heap[i]
            break


        #AFRAID that tests might not be valid, last shift to left when popping a value COULD
        # put values into improper locations, use a slightly different push method to check for NONE values.

def test_pop_reorganizes_birthorder():
    u"""Assert that pop properly reorganizes."""
    priorityQ = _build_a_heap(_test_birthorder)
    nums_in_heap = priorityQ[:]
    nums_in_heap.sort()
    nums_in_heap = nums_in_heap[::-1]
    for i, num in enumerate(_test_birthorder):
        print u"PriorityQ: {}".format(priorityQ[:])
        print u"Nums_in_heap: {}".format(nums_in_heap[i:])
        removed = priorityQ.pop()
        print "Removed: {}\n nums_in_heap[i]: {}\n".format(removed, nums_in_heap[i])
        print len(nums_in_heap)
        print len(priorityQ)
        while i>0:
            assert removed == nums_in_heap[i]
            break

def test_pop_reorganizes_priority():
    u"""Assert that pop properly reorganizes."""
    priorityQ = _build_a_heap(_test_priority)
    nums_in_heap = priorityQ[:]
    nums_in_heap.sort()
    nums_in_heap = nums_in_heap[::-1]
    for i, num in enumerate(_test_priority):
        print u"PriorityQ: {}".format(priorityQ)
        print u"Nums_in_heap: {}".format(nums_in_heap[i:])
        removed = priorityQ.pop()
        print "Removed: {}\n nums_in_heap[i]: {}\n".format(removed, nums_in_heap[i])
        print len(nums_in_heap)
        print len(priorityQ)
        while i>0:
            assert removed == nums_in_heap[i]
            break
