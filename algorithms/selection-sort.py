def selection_sort(array):
    new_array = []

    for i in range(len(array)):
        smallest = find_smallest_index(array)
        new_array.append(array.pop(smallest))
    return new_array

def find_smallest_index(array):
    smallest = array[0]
    smallest_index = 0

    for i in range(1, len(array)):
        if array[i] < smallest:
            smallest = array[i]
            smallest_index = i
    return smallest_index

# array_1 = [1,3,4,5,2,1,2,3]
# array_2 = [6,3,4,5,2,4,2,3]
# array_3 = [1,3,2,5,2,1,1,3]
# array_4 = [1,3,7,5,2,1,8,3]
# print(array_1)
# print(selection_sort(array_1))
# print(array_2)
# print(selection_sort(array_2))
# print(array_3)
# print(selection_sort(array_3))
# print(array_4)
# print(selection_sort(array_4))
