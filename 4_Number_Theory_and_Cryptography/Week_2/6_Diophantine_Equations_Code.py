def gcd(a, b):
    """
    This function calculates the greatest common divisor (GCD) of two integers a and b.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The GCD of a and b.
    """
    assert a >= 0 and b >= 0 and a + b > 0, "Both a and b must be non-negative and their sum must be positive."

    while a > 0 and b > 0:
        # We can keep dividing the larger number by the smaller number until one of them becomes 0.
        if a >= b:
            a = a % b
        else:
            b = b % a

    # The GCD is the larger of the two numbers after the loop finishes.
    return max(a, b)


def extended_gcd(a, b):
    """
    This function calculates the extended greatest common divisor (GCD) of two integers a and b,
    which also returns the Bézout coefficients x and y such that ax + by = gcd(a, b).

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        tuple: A tuple containing the GCD (g), x, and y.
    """

    if a == 0:
        # If a is 0, then b is the GCD and x and y are 1 and 0, respectively.
        return b, 0, 1
    else:
        # Otherwise, we can use the Euclidean algorithm recursively to find the GCD of b % a and a.
        g, x, y = extended_gcd(b % a, a)

        # Then, we can use the following equations to find x and y for the original equation ax + by = gcd(a, b).
        return g, y - (b // a) * x, x


def diophantine(a, b, c):
    """
    This function solves the Diophantine equation ax + by = c for integers x and y.

    Args:
        a (int): The coefficient of x.
        b (int): The coefficient of y.
        c (int): The constant term.

    Returns:
        tuple: A tuple containing the solution (x, y) or None if no solution exists.
    """

    assert c % gcd(a, b) == 0, "The constant term must be divisible by the GCD of the coefficients."

    g, x, y = extended_gcd(a, b)

    # If the constant term is not divisible by the GCD, then there is no solution.
    if c % g != 0:
        return None

    # Otherwise, we can find the solution by scaling x and y by c / g.
    return c // g * x, c // g * y


# Test the function with an example
diophantine_example = diophantine(10, 6, 14)
print("Solution to the Diophantine equation 10x + 6y = 14 is:", diophantine_example)
