sample_numbers=[2,4,3,7,8,53,32,45,7,52,4,1,3,76,34,23,4,3,3,6,2,55,234,256,144,999,426,2]





def test_init():
    u"""Assert the initiation of heap object"""
    heap = Heap()
    assert isinstance(heap, Heap())

def test_push():
    heap= Heap()
    for num in sample_numbers:
        head.push(num)
    assert len(heap) == len(sample_numbers)
    assert heap[0] == max(sample_numbers)

def test_pop():
    heap= Heap()
    for num in sample_numbers:
        head.push(num)
    for num in sample_numbers:
        assert heap.pop() = heap[0]