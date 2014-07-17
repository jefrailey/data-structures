from functools import partial
import timeit

def time_func(func):
    reps = 1000
    length = 1000

    print "\nAll tests run with " + str(reps) + " repetitions.\n"
    unsorted_list = [1,5,3,8,6,2,0,4,7,9]
    t= timeit.Timer(partial(func, unsorted_list))
    print "A list of length ten takes: " + str(t.timeit(reps)) + \
    " seconds to sort.\n"

    unsorted_list = range(length)
    t= timeit.Timer(partial(func, unsorted_list))
    print "An already sorted list of length " + str(length) + \
    " takes: " + str(t.timeit(reps)) + " seconds to sort.\n"

    unsorted_list = range(length)
    unsorted_list.reverse()
    t= timeit.Timer(partial(func, unsorted_list))
    print "A backwards sorted list of length " + str(length) + \
       " takes: " + str(t.timeit(reps)) + " seconds to sort.\n"