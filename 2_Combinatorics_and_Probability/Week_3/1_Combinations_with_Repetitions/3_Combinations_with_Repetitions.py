from math import comb

# Question 1
print("\nQuestion 1: Twenty people are voting for one of 5 candidates. \nThey have secret ballot, each voter votes for one of 5 candidates. \nThe result of an election is the number of votes for each of the candidate. How many possible results can this vote have?")
num_vote_results = comb(20 + 5 - 1, 5 - 1)
print(f"Answer: The number of possible results of the vote is {num_vote_results}.\n")

# Question 2
print("Question 2: We have 9 identical candies and we want to distribute them between 3 different sections of our bag.\n It does not matter which candies go to which section.\n How many ways do we have to do it?")
num_candy_distributions = comb(9 + 3 - 1, 3 - 1)
print(f"Answer: The number of ways to distribute 9 identical candies between 3 different sections of the bag is {num_candy_distributions}.\n")
