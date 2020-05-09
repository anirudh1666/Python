# Made by Anirudh Lakra
# Merge sort

# @params: array to sort, size of array.
def merge_sort(array, size):

    # If array can't be split any further.
    if size < 2:
        return
    
    else:
        # Find midpoint and partition array into left and right.
        mid = size // 2
        left = array[:mid]
        right = array[mid:]

        # Sort both sides and insert them into array.
        merge_sort(left, mid)
        merge_sort(right, mid)
        merge(left, right, array, len(left), len(right))


# Auxiliary function for merge_sort.
# @params: left partition, right partition, overall array, len(left_partition),
#          len(right_partition).
def merge(left, right, array, left_size, right_size):

    # i = left index, j = right index, k = array index.
    i, j, k = 0, 0, 0

    while i < left_size and j < right_size:

        # Choose smallest from left[i], right[j] and put that into array.
        if left[i] <= right[j]:
            array[k] = left[i]
            k += 1
            i += 1
        else:
            array[k] = right[j]
            k += 1
            j += 1

    if i < left_size:
        array[k] = left[i]
        i += 1
        k += 1
    elif j < right_size:
        array[k] = right[j]
        j += 1
        k += 1


def test_merge_sort():

    my_array = [-203,0.42,230,548,3,501,23,-504]
    size = len(my_array)

    print("Unsorted: " + str(my_array))
    merge_sort(my_array, size)
    print("Sorted: " + str(my_array))


test_merge_sort()
    
    
