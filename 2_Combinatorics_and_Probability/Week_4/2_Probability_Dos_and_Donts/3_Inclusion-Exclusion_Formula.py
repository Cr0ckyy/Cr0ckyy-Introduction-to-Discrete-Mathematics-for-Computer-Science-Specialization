# Problem Description 1:
# We are given two events A and B in a probability space with probabilities 0.7 and 0.8 respectively.
# We need to find the minimum possible probability of the intersection of these two events.

# Given probabilities
prob_A = 0.7
prob_B = 0.8

# The sum of probabilities of A and B exceeds 1, which indicates that these events are not disjoint.
# The minimum possible intersection is the amount by which the sum of the probabilities of A and B exceeds 1
min_intersection = prob_A + prob_B - 1
print("The minimum possible probability of the intersection of A and B is", min_intersection)

# Problem Description 2:
# We are given two events A and B in a probability space with probabilities 0.7 and 0.8 respectively.
# We need to find the maximum possible probability of the intersection of these two events.

# The maximum possible intersection is the minimum of the probabilities of A and B
# The intersection of two events cannot be more probable than either of the events.
# This maximum probability happens when A is a part of B (or vice versa).
max_intersection = min(prob_A, prob_B)
print("The maximum possible probability of the intersection of A and B is", max_intersection)
