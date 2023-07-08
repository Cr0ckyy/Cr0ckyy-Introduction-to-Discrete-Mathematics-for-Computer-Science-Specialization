from math import factorial

# Calculate the number of ways to split 12 students into working groups of size 2
# This is equivalent to the number of ways to pair 12 students, which can be calculated using the formula 12! / (2!)^6 / 6!
result = factorial(12) // (factorial(2) ** 6 * factorial(6))

print(result)  # Output: 10395
