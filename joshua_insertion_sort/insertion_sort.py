import timeit

def insertion_sort(unsorted):
    u"""Return list sorted via insertion sort."""
    for i, val in enumerate(unsorted):
        while val < unsorted[i-1] and i > 0:
            unsorted[i] = unsorted[i-1]
            i -= 1
        unsorted[i] = val
    return unsorted
