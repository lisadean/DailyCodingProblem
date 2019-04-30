# Given an array of integers, find the first missing positive integer in linear
# time O(n) and constant space O(1). In other words, find the lowest positive
# integer that does not exist in the array. The array can contain duplicates
# and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0]
# should give 3.

# You can modify the input array in-place.

input1 = [3, 4, -1, 1]
input2 = [1, 2, 0]


def find_missing_int(input):
    temp_array = []
    for number in input:
        if number > 0:
            temp_array.insert(number, number)
    for index, value in enumerate(temp_array):
        print('index: {} value: {}'.format(index, value))


find_missing_int(input1)
# print(find_missing_int(input1))
# print(find_missing_int(input2))
# assert find_missing_int(input1) == 2
# assert find_missing_int(input2) == 3
