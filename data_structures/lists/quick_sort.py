def quick_sort(list_):
    u"""Return a list sorted by the quick sort algorithm."""
    if list_:
        pivot = _median(list_[0], list_[len(list_)//2], list_[-1])
        left = quick_sort([x for x in list_ if x < pivot])
        right = quick_sort([x for x in list_ if x > pivot])
        pivots = [x for x in list_ if x == pivot]
        return left + pivots + right
    else:
        return []


def _median(a, b, c):
    u"""Return the median of three values."""
    if (a <= b <= c) or (c <= b <= a):
        return b
    elif (a <= c <= b) or (b <= c <= a):
        return c
    else:
        return a

if __name__ == '__main__':
    from data_structures import time_func
    time_func(quick_sort)
