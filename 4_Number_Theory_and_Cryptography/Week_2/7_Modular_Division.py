def extended_gcd(a, b):
    """
    Extended Euclidean Algorithm that computes the gcd of a and b,
    as well as the coefficients of Bézout's identity.
    """
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = extended_gcd(b % a, a)
        return (g, y - (b // a) * x, x)

def modinv(a, b):
    """
    Computes the modular multiplicative inverse a^-1 mod b using the extended GCD algorithm.
    """
    g, x, y = extended_gcd(a, b)
    if g != 1:
        raise Exception('gcd(a, b) != 1, no mod inverse exists')
    else:
        return x % b

def divide(a, b, n):
    """
    Function to perform division in modular arithmetic.
    It finds an integer x such that b/a = x (mod n), given gcd(a, n) = 1.
    """
    assert n > 1 and a > 0 and extended_gcd(a, n)[0] == 1
    # Calculate the modular inverse of a mod n
    a_inv = modinv(a, n)
    # Return the result of b times the modular inverse of a mod n
    return (b * a_inv) % n

# Let's test the divide function with an example
print(divide(7, 1, 13))  # This should compute 1/7 mod 13, which should give us 2 because 2 * 7 mod 13 is 1.
