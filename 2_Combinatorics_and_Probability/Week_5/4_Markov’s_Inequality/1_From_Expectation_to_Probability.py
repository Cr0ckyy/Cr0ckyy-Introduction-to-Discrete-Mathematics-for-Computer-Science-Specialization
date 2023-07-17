# Problem: Chances of winning $500 or more in a lottery

# Assume the contrary: the probability to win at least $500 is at least 1%

# Denote the number of tickets sold by 'n'
n = 1000  # Example value, you can adjust it accordingly

# Calculate the budget of the lottery and the amount spent on prizes
lottery_budget = 10 * n  # 10000
prize_amount = lottery_budget * 0.4  # 4000

# Calculate the minimum number of tickets that need to win at least $500 to contradict the assumption
minimum_winning_tickets = 0.01 * n # 10

# Calculate the total amount won by the minimum number of winning tickets
total_winning_amount = minimum_winning_tickets * 500

# Check if the total winning amount exceeds the prize amount
if total_winning_amount > prize_amount:
    print("Contradiction: The assumption is false.")
    print("Total winning amount:", total_winning_amount)
    print("Prize amount:", prize_amount)
else:
    print("The assumption holds true.")
    print("Total winning amount:", total_winning_amount)
    print("Prize amount:", prize_amount)

# The above program demonstrates the proof by contradiction.
# It assumes that the probability to win at least $500 is at least 1%.
# It then calculates the budget and prize amount of the lottery based on the number of tickets sold.
# It calculates the minimum number of winning tickets required to contradict the assumption.
# Finally, it checks if the total winning amount exceeds the prize amount.
# If the total winning amount is greater, it implies a contradiction, indicating that the assumption is false.
# Otherwise, it indicates that the assumption holds true.
