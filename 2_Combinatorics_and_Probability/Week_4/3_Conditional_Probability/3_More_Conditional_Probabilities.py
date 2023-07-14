# Question 1: Mary tosses the coin three times. What is the conditional probability of the event "all tails" under the condition "at least two tails"?

# Step 1: Calculate the total number of outcomes
total_outcomes = 2 ** 3  # Each toss can have 2 outcomes (head or tail), and we have 3 tosses

# Step 2: Calculate the number of outcomes for each event
outcomes_all_tails = 1  # There is only one outcome where we get all tails
outcomes_at_least_two_tails = 4  # These are: TTT, TTH, THH, HTH

# Step 3: Calculate the conditional probability
probability_all_tails_given_at_least_two_tails = outcomes_all_tails / outcomes_at_least_two_tails

# Print the result for Question 1
print("The conditional probability of getting all tails given at least two tails is:",
      probability_all_tails_given_at_least_two_tails)

# Question 2: The conditional probability Pr[B|A] is 4/5; the conditional probability P[B|not A] is 2/5, and the unconditional probability of B is 1/2. What is the probability of A?

# Given values
P_B_given_A = 4 / 5
P_B_given_not_A = 2 / 5
P_B = 1 / 2

# Import necessary module
from sympy import symbols, Eq, solve

# Define P(A) as a symbol
P_A = symbols('P_A')

# Create the equation for P(A)
eq = Eq(P_B, P_B_given_A * P_A + P_B_given_not_A * (1 - P_A))

# Solve the equation for P(A)
solution = solve(eq, P_A)

# Get the first (and only) solution
P_A_value = solution[0]

# Print the result for Question 2
print("The probability of event A is:", P_A_value)
