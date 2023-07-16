# Python Program

# Importing the required libraries
import numpy as np

# Question 1
# We are asked to find the smallest possible average of two numbers a and b
# where 1 <= a <= 5 and 2 <= b <= 7
# The smallest possible average would be when both a and b are at their smallest values
a1 = 1
b1 = 2
average1 = (a1 + b1) / 2
print(f"The smallest possible average (μ) is: {average1}")

# Question 2
# We are asked to find the largest possible average of two numbers a and b
# where 1 <= a <= 5 and 2 <= b <= 7
# The largest possible average would be when both a and b are at their largest values
a2 = 5
b2 = 7
average2 = (a2 + b2) / 2
print(f"The largest possible average (μ) is: {average2}")

# Question 3
# We are given the grades of three students and asked to find the average
# We add the grades together and divide by the number of students
grades = np.array([78, 72, 87])
average3 = np.mean(grades)
print(f"The average grade is: {average3}")

# Question 4
# We are asked to find the approximate average outcome of a coin toss
# where 1 represents 'tails' and 0 represents 'heads'
# Since a fair coin has an equal chance of landing on 'heads' or 'tails', the average outcome would be 0.5
average4 = 0.5
print(f"The approximate average outcome of a coin toss is: {average4}")

# Question 5
# We are given that the average of four numbers a, b, c, d is 36
# and the average of the first three numbers a, b, c is 27
# We can find the value of d by subtracting the sum of a, b, c from the sum of a, b, c, d
# Since the average is the sum divided by the number of elements, we can find the sum by multiplying the average by the number of elements
sum_abc = 27 * 3
sum_abcd = 36 * 4
d = sum_abcd - sum_abc
print(f"The value of d is: {d}")
