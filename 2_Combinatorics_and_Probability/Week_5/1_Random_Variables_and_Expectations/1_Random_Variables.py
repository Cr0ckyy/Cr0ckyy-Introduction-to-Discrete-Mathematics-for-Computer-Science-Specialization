# Question 2: Probability of a random variable
# Suppose we toss a coin two times in a row.
# Consider the random variable that is equal to the number of heads in these throws.
# What is the probability of the event that this random variable has value 1?

# Define the possible outcomes when tossing a coin two times
coin_outcomes = ['HH', 'HT', 'TH', 'TT']

# Count the number of outcomes with one head
num_one_head = coin_outcomes.count('HT') + coin_outcomes.count('TH')

# Calculate the probability of the random variable having a value of 1
probability = num_one_head / len(coin_outcomes)

# Print the probability
print("\nThe probability of the random variable having a value of 1 is:", probability)
