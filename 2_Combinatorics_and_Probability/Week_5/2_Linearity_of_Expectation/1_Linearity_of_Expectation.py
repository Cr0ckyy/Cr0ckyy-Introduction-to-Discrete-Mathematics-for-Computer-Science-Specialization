# Importing the necessary library
import numpy as np

# Question 1: Expected number of tails in 4 coin tosses
# A coin has 2 outcomes: heads or tails. So, the probability of getting tails is 0.5.
# The expected value is calculated by multiplying the probability of an event by the number of trials.
# Therefore, for 4 coin tosses, the expected number of tails is:

num_tosses = 4
prob_tails = 0.5
expected_tails = num_tosses * prob_tails
print(f"Expected number of tails in 4 coin tosses: {expected_tails}")

# Question 2: Expected number of outcomes '1' in 4 dice throws
# A dice has 6 outcomes: 1, 2, 3, 4, 5, 6. So, the probability of getting '1' is 1/6.
# Again, the expected value is calculated by multiplying the probability of an event by the number of trials.
# Therefore, for 4 dice throws, the expected number of outcomes '1' is:

num_throws = 4
prob_one = 1 / 6
expected_ones = num_throws * prob_one
print(f"Expected number of outcomes '1' in 4 dice throws: {expected_ones}")

# Question 3: Expected value of the sum of two numbers in 2 dice throws
# The expected value of a single dice throw is the sum of each outcome multiplied by its probability.
# For a fair six-sided dice, the expected value is:

expected_value_single_throw = np.sum([i * (1 / 6) for i in range(1, 7)])

# Therefore, for 2 dice throws, the expected value of the sum of the two numbers is:

expected_sum = 2 * expected_value_single_throw
print(f"Expected value of the sum of two numbers in 2 dice throws: {expected_sum}")
