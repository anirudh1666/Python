# Made by Anirudh Lakra.
# Linear search that stops when it reaches value or end.


# @params: array to search in, size of the search (length of search - 1)
#          and target value to search for.
# @returns: index of target value or -1 if not found.
def sentinel_linear_search(array, size, value):

    # Store last value in last.
    last = array[size]

    # Bound the search by inserting target value at the end.
    array[size] = value
    count = 0

    while array[count] != value:
        count += 1

    array[size] = last
    if count < size or array[size] == value:
        return count
    return -1


def test_sentinel_search():

    my_array = [10,12,219,20329,-39,0.32,5,320,123,-201,3.32]
    target_val = 123
    
    print("Array: " + str(my_array))
    print("Target value: " + str(target_val))
    print("Expected index: 8")
    print("Index of: " + str(sentinel_linear_search(my_array, 10, target_val)))


test_sentinel_search()

