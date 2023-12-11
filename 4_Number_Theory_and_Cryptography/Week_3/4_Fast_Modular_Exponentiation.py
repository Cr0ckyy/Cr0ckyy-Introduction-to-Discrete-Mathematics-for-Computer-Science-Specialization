def FastModularExponentiation(b, k, m):
    """
    Compute b^(2^k) mod m using the method of repeated squaring.
    """
    # Initialize result to 1 (b^0)
    result = 1

    # Compute b^(2^k) by repeated squaring
    for _ in range(k):
        # Square the base b and take mod m
        b = (b * b) % m
        # Multiply result by the current base b mod m
        result = (result * b) % m

    return result

# Test the function with an example
FastModularExponentiation(3, 4, 1000)  # Example to test the implementation, this should compute 3^(2^4) mod 1000
