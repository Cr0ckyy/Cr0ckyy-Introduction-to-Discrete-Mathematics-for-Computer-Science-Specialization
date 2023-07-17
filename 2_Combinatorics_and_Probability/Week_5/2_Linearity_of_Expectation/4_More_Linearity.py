# Question 1: Expectation of having "Heads" followed by "Tails" in 20 coin tosses

# The question asks for the expected number of times we have an outcome "Heads" and the next outcome is "Tails"
# when tossing a coin 20 times in a row. This expectation is a statistical concept that essentially averages
# the possible outcomes based on their probabilities.

# We start by defining the constants of the problem:
# - The number of coin flips (20 in this case)
# - The probability of flipping "Heads" (0.5 since it's a fair coin)
# - The probability of flipping "Tails" (also 0.5 for the same reason)

num_flips = 20
prob_head = 0.5
prob_tail = 0.5

# We then calculate the expectation. This is done by multiplying the probability of each event ("Heads" then "Tails")
# by the number of possible times this event could occur. Since we can't have a "Tails" after the last flip,
# we subtract 1 from the total number of flips.

expectation = (prob_head * prob_tail) * (num_flips - 1)

# Finally, we print the calculated expectation.

print("Expectation of having 'Heads' followed by 'Tails' in 20 coin tosses:", expectation)
