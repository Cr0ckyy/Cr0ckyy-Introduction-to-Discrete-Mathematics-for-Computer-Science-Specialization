import math

# Question 1
# Alice has 7 different textbooks. She would like to lend three books to Bob for a weekend.
# How many ways does she have to do it?
num_books_alice = 7
num_books_to_lend = 3
ways_q1 = math.comb(num_books_alice, num_books_to_lend)
print(f"\nAnswer to Question 1: {ways_q1} - Alice has to pick 3 books out of 7 books she has. The order does not matter, and she cannot pick the same book twice.\nSo we have combinations of size 3 out of 7 objects. There are 7x6x5/(3x2x1)=7x5=35 of them.\n")

# Question 2
# Alice has 7 textbooks and Bob has 5 textbooks. All textbooks are different.
# They would like to exchange three books each between each other for a weekend.
# That is, Alice gives Bob three of her books and Bob gives Alice three of his books.
# How many ways do they have to do it?
num_books_bob = 5
ways_q2 = math.comb(num_books_alice, num_books_to_lend) * math.comb(num_books_bob, num_books_to_lend)
print(f"Answer to Question 2: {ways_q2} - When each of them picks three books among their N books (N=7 for Alice and N=5 for Bob),\n we are dealing with combinations: unordered selection without repetitions.\nThus Alice can pick three books in 7x6x5/(3x2x1)=7x5=35 ways and Bob can pick three books in 5x4x3/(3x2x1)=10 ways.\nSince we want both Alice and Bob to choose books, we are dealing with pairs of choices, so we have to multiply variants for both people.\n")

# Question 3
# Five married couples are planning a barbecue. They need to pick three couples who will be responsible for bringing food.
# How many ways do they have to do it?
num_couples = 5
num_couples_to_pick = 3
ways_q3 = math.comb(num_couples, num_couples_to_pick)
print(f"Answer to Question 3: {ways_q3} - We pick three couples out of five without repetitions and order.\nThese are combinations of size three out of five options.\n")

# Question 4
# Five married couples are planning a barbecue. They need to hold a meeting dedicated to the planning.
# The meeting should consist of five people, one from each couple.
# How many possible ways do they have to pick people for the meeting?
ways_q4 = 2**num_couples  # Each couple has 2 choices (husband or wife), and there are 5 couples
print(f"Answer to Question 4: {ways_q4} - Indeed, in each couple, they have to pick one person.\nThere are two ways to do this.\nSince this has to be repeated five times separately, we have to apply the product rule and multiply 2 by itself five times.\nNote that we are dealing with tuples here: we pick a sequence of length 5, where each position in the sequence corresponds to one of the couples\n, and we have two options for each position, two members of the couple.\n")

# Question 5
# Five married couples gathered for a barbecue. They need to pick three people among them who will be responsible for preparing the table.
# But they do not want to pick two people from the same couple for this (this would not be fair).
# How many ways do they have to pick three people satisfying this requirement?
num_people_to_pick = 3
ways_q5 = math.comb(num_couples, num_people_to_pick) * 2**num_people_to_pick  # Each of the 3 chosen couples has 2 choices (husband or wife)
print(f"Answer to Question 5: {ways_q5} - Due to the restriction, we have to pick three persons from different couples.\nFor this, we first have to pick three couples, from which we are going to choose people for our task.\nAnd then we have to pick one person from each of the three couples.\nWe can make the first choice in 10 ways (compare with Question 3 of the test) and then we can pick one person in each of the three couples.\nWe can do it in 8 ways (compare with Question 4 of this test).\nEach pair of choices on two stages above results in a different pick of people to prepare the table.\nSo by the product rule, in total, we have 10x8=80 possibilities.\n")

# Question 6
# In a 6 number lottery, one is trying to guess an unordered subset of 6 numbers among 44 numbers without repetitions.
# For this, one picks 6 numbers out of 44 themselves. How many ways are there to do this?
num_total_numbers = 44
num_numbers_to_pick = 6
ways_q6 = math.comb(num_total_numbers, num_numbers_to_pick)
print(f"Answer to Question 6: {ways_q6} - We have to pick a subset of size 6 out of 44 options.\nThese are combinations, and the answer is a binomial coefficient.\n")

# Question 7
# In a 6 number lottery, one is trying to guess an unordered subset of 6 numbers among 44 numbers without repetitions.
# After the lottery, the organizers decided to count how many possible ways are there to guess correctly exactly three numbers.
# What is the answer to this question?
num_correct_numbers = 3
num_incorrect_numbers = num_numbers_to_pick - num_correct_numbers
num_remaining_numbers = num_total_numbers - num_numbers_to_pick
ways_q7 = math.comb(num_numbers_to_pick, num_correct_numbers) * math.comb(num_remaining_numbers, num_incorrect_numbers)
print(f"Answer to Question 7: {ways_q7} - Since the lottery has already happened, the set of winning numbers is fixed.\nSo to guess exactly three winning numbers, one has to pick three numbers among the 6 winning numbers and pick 3 other numbers among the remaining 44-6=38 numbers.\nChoices for both cases can be computed as binomial coefficients, and then we have to multiply the results by the product rule.\n")
