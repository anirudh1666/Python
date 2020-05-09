# Made by Anirudh Lakra
# Selection sort


# Picks smallest element from i - size and puts it at front.
# @params: array = array to be sorted.
#          size = size of array.
def selection_sort(array, size):

    for i in range(size):
        min_index = i
        j = i + 1

        while j < size:
            # If smaller element is found.
            if array[j] < array[min_index]:
                min_index = j
            j += 1

        array[min_index], array[i] = array[i], array[min_index]


def test_selection_sort():

    my_array = [-239,3,459,12,59,232,75]
    size = len(my_array)

    print("Unsorted: " + str(my_array))
    selection_sort(my_array, size)
    print("Sorted: " + str(my_array))


test_selection_sort()
        
