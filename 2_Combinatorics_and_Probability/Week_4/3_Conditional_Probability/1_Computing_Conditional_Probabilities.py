import math

# Q1: Conditional probability of an outcome being odd given it is even
# Since an outcome cannot be both odd and even, the conditional probability is 0
prob_Q1 = 0
print("Q1: Conditional probability of an outcome being odd given it is even")
print(f"Answer: {prob_Q1}\n")

# Q2: Probability that B is before A given that A is not the first
# For each position of A (2nd to 6th), number of valid positions for B is 1 less than position of A
# For each valid position of A and B, the other four people can be arranged in 4! ways
valid_arrangements = sum((position_A - 1) * math.factorial(4) for position_A in range(2, 7))
total_arrangements = math.factorial(6)  # Total number of arrangements is 6!
prob_Q2 = valid_arrangements / total_arrangements
print("Q2: Probability that B is before A given that A is not the first")
print(f"Answer: {prob_Q2}\n")

# Q3: Conditional probability to get 1 on first dice given sum is 6
# Out of the 5 pairs that sum to 6, only 1 pair (1,5) has 1 on the first dice
prob_Q3 = 1 / 5
print("Q3: Conditional probability to get 1 on first dice given sum is 6")
print(f"Answer: {prob_Q3}\n")

# Q4: Conditional probability of "king chooses second box" given "ball is white"
# Using Bayes' theorem, we calculate the probability of getting a white ball from each box
# and the total probability of getting a white ball.
# The desired probability is then the probability of getting a white ball from box 2 divided by the total probability
prob_white_box1 = 1 / 2 * 1  # Probability of drawing a white ball from the first box
prob_white_box2 = 1 / 2 * 14 / 29  # Probability of drawing a white ball from the second box
prob_white_total = prob_white_box1 + prob_white_box2  # Total probability of drawing a white ball
prob_Q4 = prob_white_box2 / prob_white_total  # Desired conditional probability
print("Q4: Conditional probability of 'king chooses second box' given 'ball is white'")
print(f"Answer: {prob_Q4}")



