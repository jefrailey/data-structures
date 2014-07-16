def merge_sort(list_):
    u"""Return a sorted list using the merge sort algorithm."""
    if len(list_) <= 1:
        return list_
    else:
        mid = len(list_)/2
        left, right = list_[:mid], list_[mid:]
        left = merge_sort(left)
        right = merge_sort(right)

    return _merge(left, right)


def _merge(left, right):
    u"""Return merged sublists."""
    sorted_ = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                next = left.pop(0)
            else:
                next = right.pop(0)
        elif len(left) > 0:
            next = left.pop(0)
        else:
            next = right.pop(0)
        sorted_.append(next)
    return sorted_