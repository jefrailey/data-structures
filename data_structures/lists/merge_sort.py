def merge_sort(list_):
    u"""Return a sorted list using the merge sort algorithm."""
    if len(list_) <= 1:
        return list_
    mid = len(list_)//2
    left, right = list_[:mid], list_[mid:]
    left = merge_sort(left)
    right = merge_sort(right)
    if left[-1] <= right[0]:
        return left + right
    return _merge(left, right)


def _merge(left, right):
    u"""Return merged sublists."""
    sorted_ = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                next = left.pop(0)
            else:
                next = right.pop(0)
        elif len(left) > 0:
            next = left.pop(0)
        else:
            next = right.pop(0)
        sorted_.append(next)
    return sorted_


if __name__ == '__main__':
    from data_structures import time_func
    time_func(merge_sort)

    # from functools import partial
    # import timeit
    # reps = 1000
    # length = 1000
    # print "\nAll tests run with " + str(reps) + " repetitions.\n"
    # unsorted_list = [1,5,3,8,6,2,0,4,7,9]
    # t= timeit.Timer(partial(merge_sort, unsorted_list))
    # print "A list of length ten takes: " + str(t.timeit(reps)) + " seconds to sort.\n"

    # unsorted_list = range(length)
    # t= timeit.Timer(partial(merge_sort, unsorted_list))
    # print "An already sorted list of length " + str(length) + " takes: " + str(t.timeit(reps)) + " seconds to sort.\n"

    # unsorted_list = range(length)
    # unsorted_list.reverse()
    # t= timeit.Timer(partial(merge_sort, unsorted_list))
    # print "A backwards sorted list of length " + str(length) + " takes: " + str(t.timeit(reps)) + " seconds to sort.\n"