def recursive_adder(array):
    if len(array) == 0:
        return 0
    else:
        return array.pop(0) + recursive_adder(array)

# array = [1,2,3,4,5,6,7,8,9,10]
# print(array)
# print(recursive_adder(array))
