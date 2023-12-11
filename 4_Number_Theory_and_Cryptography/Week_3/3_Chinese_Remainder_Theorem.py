def ChineseRemainderTheorem(n1, r1, n2, r2):
    """
    This function finds a number r that satisfies the following two congruences:

    r ≡ r1 (mod n1)
    r ≡ r2 (mod n2)

    where n1 and n2 are coprime (meaning they have no common factors other than 1).

    Args:
        n1: The first modulus.
        r1: The residue modulo n1.
        n2: The second modulus.
        r2: The residue modulo n2.

    Returns:
        The number r that satisfies the given congruences.
    """

    def extended_euclid(a, b):
        """
        This function implements the extended Euclidean algorithm, which finds the
        greatest common divisor (gcd) of two integers a and b, along with the coefficients
        x and y such that ax + by = gcd(a, b).

        Args:
            a: The first integer.
            b: The second integer.

        Returns:
            A tuple (gcd, x, y) where:
                - gcd is the greatest common divisor of a and b.
                - x and y are the coefficients such that ax + by = gcd(a, b).
        """
        if a == 0:
            return b, 0, 1
        gcd, x, y = extended_euclid(b % a, a)
        # Recursive call to find gcd and coefficients
        return gcd, y - (b // a) * x, x

    # Calculate the extended Euclidean GCD of n1 and n2
    _, x, y = extended_euclid(n1, n2)

    # Apply the Chinese Remainder Theorem formula
    # r = (r1 * y * n2 + r2 * x * n1) % (n1 * n2)
    # This is the solution for the linear congruences r ≡ r1 (mod n1) and r ≡ r2 (mod n2)

    return (r1 * y * n2 + r2 * x * n1) % (n1 * n2)

# Test the function
n1, r1, n2, r2 = 3, 2, 5, 3
result = ChineseRemainderTheorem(n1, r1, n2, r2)
print(f"The number r satisfying the given congruences is: {result}")
