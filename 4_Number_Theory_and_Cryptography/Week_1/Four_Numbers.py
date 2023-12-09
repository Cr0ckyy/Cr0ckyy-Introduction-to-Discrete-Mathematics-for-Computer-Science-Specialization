# To demonstrate the pigeonhole principle with a Python program, we can write a function
# that takes four integers and checks if there are at least two numbers whose difference
# is divisible by 3. We expect this function always to find such a pair since we are applying
# the pigeonhole principle.

def find_divisible_pair(numbers):

    # Dictionary to store numbers by their remainder when divided by 3
    remainders = {0: [], 1: [], 2: []}

    # Assign each number to a list based on its remainder when divided by 3
    for number in numbers:
        remainder = number % 3
        remainders[remainder].append(number)

        # Check if we have found at least two numbers with the same remainder
        if len(remainders[remainder]) >= 2:
            return True, remainders[remainder][0], remainders[remainder][1]

    return False, None, None


# Test the function with a set of four numbers
print(find_divisible_pair([1, 2, 3, 4]) ) # This should return True with a pair of numbers whose difference is divisible by 3
