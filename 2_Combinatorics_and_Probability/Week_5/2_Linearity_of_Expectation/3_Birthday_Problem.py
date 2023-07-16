# Import required libraries
from sympy import Symbol, solve
from math import ceil, sqrt

# Define the number of people and days in a year
n = Symbol('n', positive=True, integer=True)
days = 365

# Question 1
# We want to calculate the probability of at least two people sharing a birthday in a group of 35
# We start with the probability of all people having different birthdays, which is the product of the probabilities
# of each new person not sharing a birthday with the ones before
prob_q1 = 1
for i in range(35):
    prob_q1 *= (days - i) / days
# The probability of at least two people sharing a birthday is one minus the probability of all people having different birthdays
prob_q1 = 1 - prob_q1
print(f"Question 1: The probability that there are two of them having the same birthday in a group of 35 people is {prob_q1}")

# Question 2
# We want to calculate the expected value of the number of pairs of people having the same birthday
# The expected number of pairs is n*(n-1)/2, where n is the number of people
# We multiply this by the probability of any two people sharing a birthday, which is 1/365
expected_pairs_q2 = 35*(35-1)/2 * (1/days)
print(f"Question 2: The expected value of the number of pairs of people having the same birthday is {expected_pairs_q2}")

# Question 3
# We want to calculate the number of people needed for the probability of two people having the same birthday to be at least 1/2
# This is known as the birthday paradox, and the number is known to be 23
num_people_q3 = 23
print(f"Question 3: The number of people needed for the probability of two people having the same birthday to be at least 1/2 is {num_people_q3}")

# Question 4
# We want to calculate the number of people needed for the expected number of pairs with the same birthday to be at least one
# We solve the equation n*(n-1)/2 * (1/365) = 1, which gives n = sqrt(730), approximately 27
num_people_q4 = ceil(sqrt(730))
print(f"Question 4: The number of people needed for the expected number of pairs with the same birthday to be at least one is {num_people_q4}")
