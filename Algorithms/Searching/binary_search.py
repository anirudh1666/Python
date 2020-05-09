# Binary search made by Anirudh Lakra. Only works if input array is
# already sorted.

# @params: array to search in, size of array and target value.
# @returns: index of target value, -1 if not found.
def binary_search(array, size, value):

    size_temp = size
    cur_index = 0
    
    while (cur_index <= size_temp):

        # Find midpoint of size_temp and cur_index.
        mid = (size_temp + cur_index) // 2
        if array[mid] == value:
            return mid

        # If value is in first half, discard second half of array.
        elif array[mid] != value and array[mid] > value:
            size_temp = mid - 1

        # Value is in second half so discard first half of array.
        else:
            cur_index = mid + 1

    return -1


def test_binary_search():

    my_array = [0,5,2,3,4,1]
    target_val = 3

    print("Array: " + str(my_array))
    print("Target value: " + str(target_val))
    print("Expected index: 3")
    index_of = binary_search(my_array, 6, 3)

    if index_of == -1:
        print("Target value was not found.")
    else:
        print("Value is at index " + str(index_of))


test_binary_search()
    
