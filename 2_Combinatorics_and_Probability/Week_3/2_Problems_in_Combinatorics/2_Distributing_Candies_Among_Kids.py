from math import comb

# Question 1
print("\nQuestion 1: There are 15 identical candies. How many ways are there to distribute them among 7 kids?\n")
num_ways_1 = comb(15 + 7 - 1, 7 - 1)
print(f"Answer: \nThere are {num_ways_1} ways to do it."
      "\nGiving each candy we pick one of the kids."
      "\nThe order o our picks does not matter (candies are identical), "
      "\nthere are repetitions allowed (we can pick the same kid twice). "
      "\nSo we are dealing with combinations o size 15 out o 7 options with repetitions. "
      "")

# Question 2
print("\nQuestion 2: There are 15 identical candies. How many ways are there to distribute them among 7 kids in such a way that each kid receives at least 1 candy?\n")
num_ways_2 = comb(15 - 7 + 7 - 1, 7 - 1)
print(f"Answer: \nThere are {num_ways_2} ways to do it."
      "\nWe can just give one candy to each kid. "
      "\nThis way we will satisfy the requirement (note that we have to give out these candies). "
      "\nNow for the remaining candies we have exactly the same situation as in the previous problem. "
      "\nWith each of 8 remaining candies we pick one of the kids. Order does not matter, repetitions are allowed. "
      "\nThus we have combinations of size 8 out of 7 options with repetitions.")
