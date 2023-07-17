# Inquiry: Determine if it is possible for 10% of citizens in a certain country
# to earn at least 15 times more money than the average income.

# Calculation to determine if the statement is possible

average_income = 1  # We can take any number, here we take 1 for simplicity
total_income = 100 * average_income  # Total income for 100% of the population

income_high_earners = 15 * average_income  # Income for the top 10% earners
total_income_high_earners = 10 * income_high_earners  # Total income for the top 10% earners

is_possible = total_income_high_earners <= total_income  # Check if the total income of the high earners is not more than the total income

# Output the result
print(is_possible)

# The program calculates the total income for 100% of the population and the income for the top 10% earners.
# It then compares the total income of the high earners to the total income for the entire population to determine if the statement is possible.
# If the total income of the high earners is not more than the total income, it indicates that it is impossible for 10% of citizens to earn at least 15 times more money than the average income.
# The program outputs the result, which is either True (if it is possible) or False (if it is impossible).
