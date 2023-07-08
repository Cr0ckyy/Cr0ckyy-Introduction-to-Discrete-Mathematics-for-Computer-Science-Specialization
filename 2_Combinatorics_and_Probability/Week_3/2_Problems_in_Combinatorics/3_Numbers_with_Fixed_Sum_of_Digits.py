from math import comb
import itertools as it

# Question 1
print("\nQuestion 1: How many non-negative integer numbers are there below 10000 such that their sum of digits is equal to 9?\n")

# Calculate the number of ways to distribute the weight of 9 among 4 digits
num_ways_1 = comb(9 + 4 - 1, 4 - 1)

print(f"Answer: There are {num_ways_1} such numbers.\n")

# Question 2
print("\nQuestion 2: How many non-negative four-digit numbers are there such that their sum of digits is equal to 10?\n")

# Count the number of four-digit numbers with a sum of digits equal to 10
count = 0
for d in it.product(range(10), repeat=4):
    if sum(d) == 10:
        count += 1

print(f"Answer: There are {count} such numbers.\n")
