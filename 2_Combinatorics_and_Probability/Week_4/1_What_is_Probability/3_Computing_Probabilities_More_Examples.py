import math

# Question 1
# Six people, including A,B, and C, form a queue in a random order (all 6! orderings are equiprobable).
# Consider the event "A is the first in the queue".
# What is its probability?
total_orderings_q1 = math.factorial(6)
favourable_orderings_q1 = math.factorial(5)  # Once A is placed first, the remaining 5 people can be arranged in any order
prob_q1 = favourable_orderings_q1 / total_orderings_q1
print(f"Answer to Question 1: {prob_q1} - All queues can be split into six classes depending on who is the first. All the classes have the same cardinality, so each is 1/6 of the total space.")

# Question 2
# Again six people, including A,B, and C, form a queue in a random order (all 6! orderings are equiprobable).
# Consider the event "A precedes B in the queue".
# What is the probability of this event?
# This event is symmetrical (it's equally likely that A precedes B as it is that B precedes A), so its probability is 1/2
prob_q2 = 1/2
print(f"Answer to Question 2: {prob_q2} - Indeed, there are two types of queues: where A precedes B and vice versa. For symmetry reasons these two classes have the same number of elements.")

# Question 3
# Again six people, including A,B, and C, form a queue in a random order (all 6! orderings are equiprobable).
# Consider the event "B is between A and C in the queue".
# What is its probability?
# To calculate this probability, we can consider the number of ways to place A, B, and C in a queue such that B is between A and C, and then multiply by the number of ways to arrange the other 3 people
favourable_orderings_q3 = 2 * math.factorial(3) * math.factorial(3)  # There are 2 ways to arrange A, B, and C such that B is between A and C, and 3! ways to arrange the other 3 people before and after them
prob_q3 = favourable_orderings_q3 / total_orderings_q1
print(f"Answer to Question 3: {prob_q3} - There are three possibilities for the middle person in the queue...")

# Question 4
# Again six people, including A,B, and C, form a queue in a random order (all 6! orderings are equiprobable).
# Consider the event "A and B are neighbors in the queue".
# What is its probability?
# To calculate this probability, we can consider A and B as a single entity, and then calculate the number of ways to arrange this entity and the other 4 people
favourable_orderings_q4 = 2 * math.factorial(5)  # There are 2 ways to arrange A and B within the entity, and 5! ways to arrange the entity and the other 4 people
prob_q4 = favourable_orderings_q4 / total_orderings_q1
print(f"Answer to Question 4: {prob_q4} - Here we cannot use the symmetry (at least I don't see how this helps). If the position of A and B (their ordinal numbers in the queue) are fixed, then there are 4! outcomes. To fix the position where A and B are neighbors, we choose between 5*2 positions (there could be 0..4 people before them and there are two orderings of A and B - A may be before B or after). So we get 5*2*4!/6!=1/3.")
