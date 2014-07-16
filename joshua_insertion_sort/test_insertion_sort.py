from insertion_sort import insertion_sort

def test_short_sort():
    unsorted_list = [1,5,3,8,6,2,0,4,7,9]
    sorted_list = insertion_sort(unsorted_list)
    assert sorted_list == range(10)

