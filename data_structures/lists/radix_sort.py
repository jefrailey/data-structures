def radix_sort(list_):
    """Return a sorted list by the radix sort algorithm."""
    bins={}
    depth = 0
    while True:
        depth += 1
        for num in list_:
            bin_key = ((num % (10 ** depth))-(num % (10 ** (depth-1))))/10
            bins.setdefault(bin_key, [num]).append(num)
        # list_ = [x for bins[x] in [l for l in sorted(bins.keys())]]
        list_ = []
        for bin_ in sorted(bins.keys()):
            for val in bins[bin_]:
                list_.append(val)


        if len(bins[bin_key])==len(list_):
            break
    return list_