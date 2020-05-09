# Made by Anirudh Lakra
# Insertion sort.


# @params: array to sort and size of the array.
def insertion_sort(array, size):

    for i in range(1, size):
        key = array[i]
        j = i - 1

        # Until you reach start element or find element
        # that is smaller than key. Insert key after smallest.
        while j >= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key



def test_insertion_sort():
    my_array = [0,-23,9,321,23.57,2]
    size = 6
    
    print("Unsorted: " + str(my_array))
    insertion_sort(my_array, size)
    print("Sorted: " + str(my_array))


test_insertion_sort()
    
