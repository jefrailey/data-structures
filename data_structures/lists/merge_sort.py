def merge_sort(list_):
    u"""Return a sorted list using the merge sort algorithm."""
    if len(list_) <= 1:
        return list_
    mid = len(list_)/2
    left, right = list_[:mid], list_[mid:]
    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)


# def _merge(left, right):
#     u"""Return merged sublists."""
#     sorted_ = []

#     while len(left) > 0 or len(right) > 0:
#         if len(left) > 0 and len(right) > 0:
#             if left[0] <= right[0]:
#                 next = left.pop(0)
#             else:
#                 next = right.pop(0)
#         elif len(left) > 0:
#             next = left.pop(0)
#         else:
#             next = right.pop(0)
#         sorted_.append(next)
#     return sorted_


def merge(left, right):
    result = []
    left_idx, right_idx = 0, 0
    while left_idx < len(left) and right_idx < len(right):
        # change the direction of this comparison to change the direction of the sort
        if left[left_idx] <= right[right_idx]:
            result.append(left[left_idx])
            left_idx += 1
        else:
            result.append(right[right_idx])
            right_idx += 1
 
    if left:
        result.extend(left[left_idx:])
    if right:
        result.extend(right[right_idx:])
    return result











if __name__ == '__main__':
    from functools import partial
    import timeit
    reps = 1000
    length = 1000
    print "\nAll tests run with " + str(reps) + " repetitions.\n"
    unsorted_list = [1,5,3,8,6,2,0,4,7,9]
    t= timeit.Timer(partial(merge_sort, unsorted_list))
    print "A list of length ten takes: " + str(t.timeit(reps)) + " seconds to sort.\n"

    unsorted_list = range(length)
    t= timeit.Timer(partial(merge_sort, unsorted_list))
    print "An already sorted list of length " + str(length) + " takes: " + str(t.timeit(reps)) + " seconds to sort.\n"

    unsorted_list = range(length)
    unsorted_list.reverse()
    t= timeit.Timer(partial(merge_sort, unsorted_list))
    print "A backwards sorted list of length " + str(length) + " takes: " + str(t.timeit(reps)) + " seconds to sort.\n"