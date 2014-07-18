def radix_sort(list_):
    u"""Return a sorted list by the radix sort algorithm."""
    depth = 0
    while True:
        bins = {}
        depth += 1
        for num in list_:
            dc = 10 ** (depth-1)
            bin_key = ((num % (10 ** depth))-(num % dc))/dc
            bins.setdefault(bin_key, []).append(num)
        list_ = []
        for bin_ in sorted(bins.keys()):
            for val in bins[bin_]:
                list_.append(val)

        if len(bins[bin_key]) == len(list_) and depth > 0:
            break
    return list_


if __name__ == '__main__':
    from data_structures import time_func
    time_func(radix_sort)
