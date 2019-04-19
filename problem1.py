# Given a list of numbers and a number k, return whether any two numbers from
# the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17
# Bonus: Can you do this in one pass?

input = [10, 15, 3, 7]
k = 17


def do_two_numbers_equal_k(num1, num2):
    return num1 + num2 == k


def main():
    new_input = input
    for num1 in input:
        new_input = new_input[1:]
        for num2 in new_input:
            sum = do_two_numbers_equal_k(num1, num2)
            if sum:
                print(f"Found one: {num1} + {num2} = {k}")
                return True


main()
