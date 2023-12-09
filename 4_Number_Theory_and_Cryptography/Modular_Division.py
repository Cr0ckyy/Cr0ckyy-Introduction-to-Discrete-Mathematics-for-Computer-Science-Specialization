# Manually input the data from the multiplication table for modulo 7
# This table is used to solve both questions by finding the 'x' that satisfies each equation

multiplication_table_mod_7 = [
    [0, 0, 0, 0, 0, 0, 0], # 0 * x
    [0, 1, 2, 3, 4, 5, 6], # 1 * x
    [0, 2, 4, 6, 1, 3, 5], # 2 * x
    [0, 3, 6, 2, 5, 1, 4], # 3 * x
    [0, 4, 1, 5, 2, 6, 3], # 4 * x
    [0, 5, 3, 1, 6, 4, 2], # 5 * x
    [0, 6, 5, 4, 3, 2, 1]  # 6 * x
]

# Question 1: Find 'x' such that 3 * x % 7 == 5
# We look in the 3rd row of the table since that corresponds to 3 * x
x_value_q1 = multiplication_table_mod_7[3].index(5)

# Question 2: Find 'x' such that 12 * x % 7 == 3
# First, we reduce 12 mod 7, which is 5 because 12 = 7 * 1 + 5, so we look in the 5th row of the table
x_value_q2 = multiplication_table_mod_7[5].index(3)

# Print the results neatly on separate lines
print("Question 1: Find 'x' such that 3 * x % 7 == 5")
print(f"x = {x_value_q1}\n")

print("Question 2: Find 'x' such that 12 * x % 7 == 3")
print(f"x = {x_value_q2}")
