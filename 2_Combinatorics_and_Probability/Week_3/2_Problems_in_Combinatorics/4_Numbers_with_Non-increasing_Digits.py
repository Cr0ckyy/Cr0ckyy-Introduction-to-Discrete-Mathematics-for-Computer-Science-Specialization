from math import comb

# Question 1: How many four-digit numbers are there such that their digits are non-increasing?
# Note: Three-digit numbers are also considered four-digit if they start with 0.

# This problem is equivalent to selecting 4 digits (with repetition allowed) from the set {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}.
# We can solve this problem using the formula for combinations with repetition, which is C(n + r - 1, r).
# Here, n is the number of options (10 digits) and r is the size of the selection (4 digits).

# Calculate the number of combinations with repetition
result = comb(13, 4)

# Print the result
print("The number of four-digit numbers with non-increasing digits is:", result)
