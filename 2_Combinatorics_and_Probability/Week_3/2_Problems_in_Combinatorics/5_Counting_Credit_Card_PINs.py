from math import comb
from itertools import product

# Problem 1: What is the number of PINs with sum of digits equal to 9?
# This problem is equivalent to selecting 4 digits (with repetition allowed) from the set {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} such that their sum is 9.
# We can solve this problem using the formula for combinations with repetition, which is C(n + r - 1, r).
# Here, n is the number of options (10 digits) and r is the sum of the digits (9).

# Calculate the number of combinations with repetition
result1 = comb(13, 4)

# Print the result
print("The number of PINs with sum of digits equal to 9 is:", result1)

# Confirm the result by generating all possible PINs and counting those with sum of digits equal to 9
pins = product(range(10), repeat=4)
print("Confirmed result:", len([pin for pin in pins if sum(pin) == 9]))


# Problem 2: What is the number of PINs with sum of digits equal to 10?
# This problem is similar to the previous one, but now the sum of the digits is 10.

# Calculate the number of combinations with repetition
result2 = comb(14, 4)

# However, this includes illegal PINs where all ten ones are assigned to the same position.
# There are 4 such illegal PINs, so we subtract them from the result.
result2 -= 4

# Print the result
print("The number of PINs with sum of digits equal to 10 is:", result2)

# Confirm the result by generating all possible PINs and counting those with sum of digits equal to 10
pins = product(range(10), repeat=4)
print("Confirmed result:", len([pin for pin in pins if sum(pin) == 10]))


# Problem 3: What is the number of PINs with non-increasing digits?
# This problem is equivalent to selecting 4 digits (with repetition allowed) from the set {0, 1, 2, 3, 4, 5, 6, 7, 8, 9} such that the digits are non-increasing.

# Calculate the number of combinations with repetition
result3 = comb(13, 9)

# Print the result
print("The number of PINs with non-increasing digits is:", result3)

# Confirm the result by generating all possible PINs and counting those with non-increasing digits
pins = product(range(10), repeat=4)
print("Confirmed result:", len([pin for pin in pins if all(pin[i] <= pin[i + 1] for i in range(3))]))
