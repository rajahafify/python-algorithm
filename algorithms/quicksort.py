def quicksort(array):
    if len(array) < 2:
        return array

    else:
        pivot = array[0]

        less = [i for i in array[1:] if i <= pivot]

        greater = [i for i in array[1:] if i > pivot]

        return quicksort(less) + [pivot] + quicksort(greater)


# print('+' * 10)
# array_1 = [1]
# print(array_1)
# print(quicksort(array_1))
#
# print('+' * 10)
# array_2 = [2,1,3,2,2,1,1,10020,20,22]
# print(array_2)
# print(quicksort(array_2))
#
# print('+' * 10)
# array_3 = [3,1,5,1,5,1,5,6,1,6,12,23,42,45,11,23]
# print(array_3)
# print(quicksort(array_3))
