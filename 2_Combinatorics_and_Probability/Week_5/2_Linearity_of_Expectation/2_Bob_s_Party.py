# Python program to calculate the expected number of guests at a party

# Import the math library to use the binomial function
import math

# Define the number of people invited
num_invited = 30

# Define the probability of each friend showing up
prob_showing_up = 2 / 5

# The expected value (mean) of a binomial distribution is calculated by multiplying the number of trials
# (in this case, the number of people invited) by the probability of success
# (in this case, the probability of a friend showing up).
# This is based on the formula E[X] = np, where E[X] is the expected value,
# n is the number of trials, and p is the probability of success.

# Calculate the expected number of guests
expected_guests = num_invited * prob_showing_up

# Print the expected number of guests
print("The expected number of guests at Bob's party is:", expected_guests)
