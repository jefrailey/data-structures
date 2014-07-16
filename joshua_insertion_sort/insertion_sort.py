def insertion_sort(unsorted):
    u"""Return list sorted via insertion sort."""
    for i, val in enumerate(unsorted):
        while val < unsorted[i-1] and i > 0:
            unsorted[i] = unsorted[i-1]
            i -= 1
        unsorted[i] = val
    return unsorted


if __name__ == '__main__':
    from functools import partial
    import timeit
    reps = 10000
    length = 1000
    print "\nAll tests run with " + str(reps) + " repetitions.\n"
    unsorted_list = [1,5,3,8,6,2,0,4,7,9]
    t= timeit.Timer(partial(insertion_sort, unsorted_list))
    print "A list of length ten takes: " + str(t.timeit(reps)) + " seconds to sort.\n"

