import random

def select_median_of_medians_pivot(array, k):
    '''
    Implementation of the Blum, Floyd, Pratt, Rivest, Tarjan SELECT
    algorithm as described by David Eppstein.

    CITATION: http://www.ics.uci.edu/~eppstein/161/960130.html

    This algorithm has worst case run time of O(N) where N is the
    number of entries in the array.

    Although this algorithm has better worst case performance than
    select_random_pivot(), that algorithm is preferred because it
    is much faster in practice.

    Here is how you might use it:

        # Create a list of pseudo random numbers.
        # Duplicates can occur.
        num = 10000
        array = [random.randint(1,1000) for i in range(num)]
        random.shuffle(array)
        random.shuffle(array)

        # Get the value of the kth item.
        k = 7
        kval = select_median_of_medians_pivot(array, k)

        # Test it.
        sorted_array = sorted(array)
        assert sorted_array[k] == kval

    @param array the list of values
    @param k     k-th item to select.
    '''

    # If the array is short, terminate the recursion and return the
    # value without partitioning.
    if len(array) <= 10:
        array.sort()
        return array[k]

    # Partition the array into subsets with a maximum of 5 elements
    # each.
    subset_size = 5  # max items in a subset
    subsets = []  # list of subsets
    num_medians = len(array) / subset_size
    if (len(array) % subset_size) > 0:
        num_medians += 1  # not divisible by 5
    for i in range(num_medians):
        beg = i * subset_size
        end = min(len(array), beg + subset_size)
        subset = array[beg:end]
        subsets.append(subset)

    # Find the medians in each subset.
    # Note that it calls select_median_of_medians_pivot() recursively taking
    # advantage of the fact that for len(array) <= 10, the select
    # operation simply sorts the array and returns the k-th item. This
    # could be done here but since the termination condition is
    # required to get an infinite loop we may as well use it.
    medians = []  # list of medians
    for subset in subsets:
        median = select_median_of_medians_pivot(subset, len(subset)/2)
        medians.append(median)

    # Now get the median of the medians recursively.
    # Assign it to the local pivot variable because
    # the pivot handling code is the same regardless
    # of how it was generated. See select_random_pivot() for
    # a different approach for generating the pivot.
    median_of_medians = select_median_of_medians_pivot(medians, len(medians)/2)
    pivot = median_of_medians  # pivot point value (not index)

    # Now select recursively using the pivot.
    # At this point we have the pivot. Use it to partition the input
    # array into 3 categories: items that are less than the pivot
    # value (array_lt), items that are greater than the pivot value
    # (array_gt) and items that exactly equal to the pivot value
    # (equals_array).
    array_lt = []
    array_gt = []
    array_eq = []
    for item in array:
        if item < pivot:
            array_lt.append(item)
        elif item > pivot:
            array_gt.append(item)
        else:
            array_eq.append(item)

    # The array values have been partitioned according to their
    # relation to the pivot value. The partitions look like this:
    #
    #   +---+---+---+...+---+---+---+...+---+---+---+...
    #   | 0 | 1 | 2 |   | e |e+1|e+2|   | g |g+1|g+2|
    #   +---+---+---+...+---+---+---+...+---+---+---+...
    #      array_lt        array_eq       array_gt
    #
    # If the value of k is in the range [0..e) then we know that
    # the desired value is in array_lt so we need to recurse.
    #
    # If the value of k in the range [e..g) then we know that the
    # desired value is in array_eq and we are done.
    #
    # If the value of k is >= g then we the desired value is in
    # array_gt and we need to recurse but we also have to make sure
    # that k is normalized with respect to array_gt so that it has the
    # proper offset in the recursion. We normalize it by subtracting
    # len(array_lt) and len(array_eq).
    #
    if k < len(array_lt):
        return select_median_of_medians_pivot(array_lt, k)
    elif k < len(array_lt) + len(array_eq):
        return array_eq[0]
    else:
        normalized_k = k - (len(array_lt) + len(array_eq))
        return select_median_of_medians_pivot(array_gt, normalized_k)

#testing
num = 10000
array = [random.randint(1,1000) for i in range(num)]
random.shuffle(array)
random.shuffle(array)

#checking 
sorted_array = sorted(array)
k = 7
kval = select_median_of_medians_pivot(array, k)

sorted_array = sorted(array)
assert sorted_array[k] == kval