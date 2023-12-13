def FastModularExponentiation_v1(b, k, m):
    """
    Compute b^(2^k) mod m using the binary exponentiation algorithm.
    :param b: Base of the exponentiation.
    :param k: The exponent k in 2^k.
    :param m: The modulus for the operation.
    :return: The result of b^(2^k) mod m.
    """
    result = 1
    binary_k = bin(1 << k)[2:]  # This is 2^k in binary as a string

    for digit in binary_k:
        result = (result * result) % m  # Square the result
        if digit == '1':
            result = (result * b) % m  # Multiply by b if the bit is 1

    return result


def FastModularExponentiation_v2(b, e, m):
    """
    Compute b^e mod m using the binary exponentiation algorithm.
    :param b: Base of the exponentiation.
    :param e: The exponent e.
    :param m: The modulus for the operation.
    :return: The result of b^e mod m.
    """
    result = 1  # Initialize result
    b = b % m  # Update b if it is more than or equal to m

    while e > 0:
        # If e is odd, multiply b with result
        if e % 2 == 1:
            result = (result * b) % m

        # e must be even now
        e = e // 2
        b = (b * b) % m  # b = b^2 % m

    return result


# Example to test the first function
print(FastModularExponentiation_v1(2, 10, 1000))  # This should return the result of 2^(2^10) mod 1000

# Example to test the second function
print(FastModularExponentiation_v2(2, 10, 1000))  # This should return 24 as 2^10 mod 1000
