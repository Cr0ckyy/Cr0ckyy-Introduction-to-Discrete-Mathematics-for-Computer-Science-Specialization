# Question 2: Probability of winning in a dice game between Alice and Bob

from random import randint, seed

seed(27)

# Define the numbers on Alice's and Bob's dice
dice1 = [2, 2, 2, 2, 3, 3]
dice2 = [1, 1, 1, 1, 6, 6]

num_rounds = 10 ** 5
num_dice1_wins = 0

# Simulate the game for a large number of rounds (10^5 in this case)
for _ in range(num_rounds):
    # Alice rolls dice1
    alice_result = dice1[randint(0, 5)]
    # Bob rolls dice2
    bob_result = dice2[randint(0, 5)]

    # Check who has the larger result and increment the corresponding win counter
    if alice_result > bob_result:
        num_dice1_wins += 1

# Calculate the probability of dice1 (Alice) winning
win_probability = num_dice1_wins / num_rounds

# Print the result
print("Out of", num_rounds, "throws, dice1 (Alice) won", num_dice1_wins, "times")
print("Probability of dice1 (Alice) winning:", win_probability)

# Why the larger expected value does not help Bob to win?
# Note that when Bob wins, he wins by far: he gets 6 against 2 or 3.
# But when Bob loses, he loses just slightly: he gets 1 against 2 or 3.
# This difference affects the expected value, but it does not affect the game:
# it does not matter if your outcome is substantially larger.
