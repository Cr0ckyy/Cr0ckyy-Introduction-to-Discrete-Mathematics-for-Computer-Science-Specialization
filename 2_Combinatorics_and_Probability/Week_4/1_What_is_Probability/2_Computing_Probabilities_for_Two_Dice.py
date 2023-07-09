# Question 1
# Consider again the setting with red and blue dice where all 36 pairs are equiprobable.
# Consider the event "red and blue numbers are different".
# How many favourable outcomes do we have for this event (out of 36)
favourable_outcomes_q1 = 6*5  # For each outcome of the red die, there are 5 outcomes of the blue die that are different
print(f"Answer to Question 1: {favourable_outcomes_q1} - For each outcome of the red die, there are 5 outcomes of the blue die that are different.")

# Question 2
# In the same setting with 36 (red, blue) outcomes we consider the sum of two numbers (on two dice).
# What is the most probable value of this sum?
# To find the most probable sum, we can consider the possible sums and how many ways each can be achieved
possible_sums = range(2, 13)  # The smallest possible sum is 2 (1+1) and the largest is 12 (6+6)
ways_to_achieve_sum = [len([(i, j) for i in range(1, 7) for j in range(1, 7) if i+j==sum_]) for sum_ in possible_sums]
most_probable_sum = possible_sums[ways_to_achieve_sum.index(max(ways_to_achieve_sum))]
print(f"Answer to Question 2: {most_probable_sum} - The most probable sum of two dice is the one that can be achieved in the most number of ways.")

# Question 3
# What is more probable while rolling two dice: to get at least one six, or to have no sixes?
# To answer this question, we can calculate the probabilities of both events
total_outcomes = 6*6
outcomes_with_at_least_one_six = 2*5 + 1  # There are 5 outcomes where one die is 6 and the other is not, and 1 outcome where both are 6
outcomes_with_no_sixes = total_outcomes - outcomes_with_at_least_one_six
more_probable_event = "Having at least one six is more probable" if outcomes_with_at_least_one_six > outcomes_with_no_sixes else "Having no sixes is more probable"
print(f"Answer to Question 3: {more_probable_event} - We calculate the number of outcomes for both events and compare them.")
