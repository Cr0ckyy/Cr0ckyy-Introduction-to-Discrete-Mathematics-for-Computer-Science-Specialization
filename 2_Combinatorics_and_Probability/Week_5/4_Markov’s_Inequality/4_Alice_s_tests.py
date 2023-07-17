# Question 1
# Alice makes 3 mistakes on average on a random test.
# What is the best upper bound we can get from Markov’s inequality
# on the probability that she will make at least 15 mistakes?

# This problem can be solved using Markov's inequality,
# which provides an upper bound on the probability
# that a non-negative random variable is greater than or equal to a certain value.

# Markov's inequality is defined as P(X >= a) <= E[X]/a,
# where P(X >= a) is the probability that the random variable X
# is greater than or equal to a, and E[X] is the expected value of X.

# In this problem, E[X] = 3 (since Alice makes 3 mistakes on average)
E_X = 3

# We're asked to find the upper bound on the probability that she will make at least 15 mistakes, so a = 15
a = 15

# Substituting these values into Markov's inequality gives us P(X >= 15) <= 3/15
P_X = E_X / a

# The best upper bound we can get from Markov's inequality on the
# probability that Alice will make at least 15 mistakes is P_X.
print("The upper bound probability is:", P_X)
