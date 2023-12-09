# Since we are looking for the remainders of an odd number when divided by 4,
# let's calculate the remainders for the first few odd numbers when divided by 4.

# This will give us a pattern to determine the possible remainders.

# Initialise a list to store the first few odd numbers
odd_numbers = [1, 3, 5, 7, 9, 11, 13, 15]

# Dictionary to hold the remainder counts
remainder_counts = {}

# Calculate remainders for each odd number when divided by 4
for number in odd_numbers:
    remainder = number % 4
    # Count the occurrence of each remainder
    remainder_counts[remainder] = remainder_counts.get(remainder, 0) + 1

# The keys of remainder_counts dictionary are the possible remainders
possible_remainders = list(remainder_counts.keys())

print(possible_remainders)
