# Python program to demonstrate the calculation of the Least Common Multiple (LCM) using the Greatest Common Divisor (GCD) method

def gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers.

    The GCD of two numbers is the largest number that divides both of them without leaving a remainder.
    This function implements the Euclidean algorithm to find the GCD.

    :param a: First number (int)
    :param b: Second number (int)
    :return: GCD of a and b (int)
    """
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    """
    Calculate the Least Common Multiple (LCM) of two numbers.

    The LCM of two numbers is the smallest number that is a multiple of both of them.
    This function uses the fact that lcm(a, b) * gcd(a, b) = a * b.

    :param a: First number (int), must be greater than 0
    :param b: Second number (int), must be greater than 0
    :return: LCM of a and b (int)
    """
    assert a > 0 and b > 0, "Both numbers must be positive integers."
    return a * b // gcd(a, b)

# Testing the lcm function with a pair of integers
test_pair = (21, 6)
test_lcm = lcm(*test_pair)

# Print the result in a formatted string for better understanding and readability
print(f"The Least Common Multiple (LCM) of {test_pair[0]} and {test_pair[1]} is {test_lcm}.")
