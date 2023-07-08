from math import comb


def binomial_expansion_coefficients(n):
    # Coefficients for a and b in (3a-2b)
    coef_a = 3
    coef_b = -2

    # List to store the coefficients of the expansion
    coefficients = []

    # Using the binomial theorem to calculate the coefficients
    for k in range(n + 1):
        # Binomial coefficient (n choose k)
        binom_coef = comb(n, k)

        # Coefficient of a^(n-k) * b^k
        coef = binom_coef * (coef_a ** (n - k)) * (coef_b ** k)

        # Append the coefficient to the list
        coefficients.append(coef)

    # Return the coefficients as a comma-separated string
    return ",".join(str(coef) for coef in coefficients)


# Example usage:
# For Question 1
n1 = 3
print(f"Coefficients for (3a-2b)^{n1}: {binomial_expansion_coefficients(n1)}")

# For Question 2
n2 = 7
print(f"Coefficients for (3a-2b)^{n2}: {binomial_expansion_coefficients(n2)}")
