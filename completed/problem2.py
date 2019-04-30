# This problem was asked by Uber.
# Given an array of integers, return a new array such that each element at
# index i of the new array is the product of all the numbers in the original
# array except the one at i.
# For example, if our input was [1, 2, 3, 4, 5], the expected output would be
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
# be [2, 3, 6].
# Follow-up: what if you can't use division?

input = [1, 2, 3, 4, 5]
input2 = [3, 2, 1]


def product_of_other_numbers(input):
    results = []
    for number in input:
        product = 0
        for factor in input:
            if number != factor:
                # print(f"{factor} is not equal to {number} so it is a factor")
                product = product * factor if product > 0 else factor
        results.append(product)
    return results


print(product_of_other_numbers(input))
print(product_of_other_numbers(input2))
