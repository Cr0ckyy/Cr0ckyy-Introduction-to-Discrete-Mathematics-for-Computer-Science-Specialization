import math
# TODO: Q1. Is number 101 prime?
def is_prime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


print("Is 101 prime?", is_prime(101))

# TODO: Q2. Is number 737 prime?
print("\nIs 737 prime?", is_prime(737))


# TODO: Q3. Does 105 = 3 . 5 . 7 divide 1260 = 2^2 . 3^2 . 5 . 7?
def is_divisible(a, b):
    return a % b == 0

# Correctly representing the numbers
num1 = 2 ** 2 * 3 ** 2 * 5 * 7  # 1260
num2 = 3 * 5 * 7  # 105

# Check if 1260 is divisible by 105
print("\nDoes 105 = 3 . 5 . 7 divide 1260 = 2^2 . 3^2 . 5 . 7?", is_divisible(num1, num2))

# TODO: Q4. Which of the numbers 6 = 2 . 3 , 10 = 2 . 5, 15 = 3 . 5 and 35 = 5 . 7
def is_coprime(a, b):
    """Returns True if a and b are coprime, False otherwise."""
    # Correct GCD calculation using Euclidean algorithm
    while b:
        a, b = b, a % b
    return a == 1

def test_coprimality(pairs):
    """Test coprimality for a list of number pairs."""
    results = []
    for pair in pairs:
        results.append(is_coprime(pair[0], pair[1]))
    return results

# List of pairs to test
pairs_to_test = [(6, 10), (6, 35), (15, 35), (10, 15)]

# Testing coprimality for each pair in the list
coprime_results = test_coprimality(pairs_to_test)
print()
# Displaying the results
for pair, result in zip(pairs_to_test, coprime_results):
    print(f"Are {pair[0]} and {pair[1]} coprime? {result}")

# TODO: Q5.Compute GCD(1990, 1848) given that 1990 = 2^2 . 3^2 . 5 . 11 and 1848 = 2^3 . 3 . 7 . 11
def compute_gcd(a, b):
    """Computes the greatest common divisor of two numbers."""
    while b > 0:
        a, b = b, a % b
    return a

# Compute the GCD of 1980 and 1848
gcd = compute_gcd(1980, 1848)

# Print the result
print()
print(gcd)


# TODO: Q6. Compute the LCM of 1980 and 1848: LCM(1980, 1848)
num1 = 1980
num2 = 1848

lcm_result = math.lcm(num1, num2)

print(f"\nLCM of {num1} and {num2} is: {lcm_result}")