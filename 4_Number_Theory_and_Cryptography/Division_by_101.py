# To solve the given problem, we can calculate the number of 3-digit non-negative numbers
# that have a remainder of 7 when divided by 101.

# A number that leaves a remainder of 7 when divided by 101 can be expressed as:
# number = 101 * k + 7, where k is an integer.

# The smallest 3-digit number is 100, and the largest is 999. We need to find the values of k
# for which 101 * k + 7 is within this range.

# Initialize the count of numbers
count = 0

# Calculate the minimum value of k for the smallest 3-digit number (100)
min_k = (100 - 7) // 101  # Using integer division to find the floor value of k

# Calculate the maximum value of k for the largest 3-digit number (999)
max_k = (999 - 7) // 101  # Using integer division to find the floor value of k

# Iterate through k values from min_k to max_k
for k in range(min_k, max_k + 1):
    number = 101 * k + 7
    count += 1

print(count)
