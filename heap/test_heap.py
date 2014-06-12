from heap import Heap

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
    for num in sample_numbers:
        heap.push(num)
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
    nums_in_heap = sample_numbers[:]
    for num in sample_numbers:
        removed = heap.pop()
        print heap[:]
        assert removed == max(nums_in_heap)
        nums_in_heap.remove(removed)
