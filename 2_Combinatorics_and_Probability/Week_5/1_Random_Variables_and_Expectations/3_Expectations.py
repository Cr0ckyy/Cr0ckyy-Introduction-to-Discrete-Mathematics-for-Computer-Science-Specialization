# Python Program

# Question 1
# We are asked to find the expected value of a random variable with outcomes 0 and 1
# having probabilities 1/3 and 2/3 respectively
# The expected value is calculated by multiplying each outcome by its probability and summing these products
outcome1 = [0, 1]
probability1 = [1/3, 2/3]
expected_value1 = sum([outcome1[i]*probability1[i] for i in range(len(outcome1))])
print(f"The expected value of the random variable for Question 1 is: {expected_value1}")

# Question 2
# We are asked to find the expected value of a random variable with outcomes 1, 3, and 4
# having probabilities 1/4, 1/2, and 1/4 respectively
# The expected value is calculated by multiplying each outcome by its probability and summing these products
outcome2 = [1, 3, 4]
probability2 = [1/4, 1/2, 1/4]
expected_value2 = sum([outcome2[i]*probability2[i] for i in range(len(outcome2))])
print(f"The expected value of the random variable for Question 2 is: {expected_value2}")
