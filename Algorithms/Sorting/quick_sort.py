# Made by Anirudh Lakra
# Quick sort (uses geeksforgeeks partition algorithm).


# @params: array = array to search.
#          l_index = lower index.
#          r_index = upper index.
def quick_sort(array, l_index, r_index):

    if l_index < r_index:
        partition_index = partition(array, l_index, r_index)
        quick_sort(array, l_index, partition_index - 1)
        quick_sort(array, partition_index + 1, r_index)


# Auxiliary function for quick_sort.
# Helps to partition array by picking highest element as pivot.
# @params: array = array to search.
#          l_index = lower index.
#          r_index = upper index.
# @returns: index of where array has been partitioned.
def partition(array, l_index, r_index):

    partition_index = l_index
    pivot = array[r_index]

    for i in range(l_index, r_index):
        if array[i] <= pivot:
            # Swap array[i] and array[partition_index]
            array[i], array[partition_index] = array[partition_index], array[i]
            partition_index += 1

    # Swap array[partition_index] and array[r_index].
    array[partition_index], array[r_index] = array[r_index], array[partition_index]
    return partition_index


def test_quick_sort():
    my_array = [-1233,-223.324,29032,593,20,5,7,1]
    l_index = 0
    r_index = len(my_array) - 1

    print("Unsorted: " + str(my_array))
    quick_sort(my_array, l_index, r_index)
    print("Sorted: " + str(my_array))

test_quick_sort()

