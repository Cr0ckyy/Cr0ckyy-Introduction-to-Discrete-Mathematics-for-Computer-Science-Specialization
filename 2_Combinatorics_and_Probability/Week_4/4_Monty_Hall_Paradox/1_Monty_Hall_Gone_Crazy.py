import random


def monty_hall_game(strategy):
    # Step 1: Host randomly puts a prize behind one of the doors
    prize_door = random.randint(1, 3)

    # Step 2: Guest makes a guess
    guest_guess = random.randint(1, 3)

    # Step 3: Host opens a door
    if guest_guess != prize_door:  # Guest's initial guess was wrong
        dice_roll = random.randint(1, 6)
        if dice_roll <= 2:  # With probability 1/3, game ends
            return False
        else:  # With probability 2/3, guest is asked to change guess
            if strategy == "change":
                return True  # Guest wins
            else:
                return False  # Guest loses
    else:  # Guest's initial guess was correct
        if strategy == "change":
            return False  # Guest loses
        else:
            return True  # Guest wins


def simulate_games(num_games, strategy):
    wins = 0
    for _ in range(num_games):
        if monty_hall_game(strategy):
            wins += 1
    return wins / num_games  # Return fraction of games won


# Simulate 10000 games for each strategy
num_games = 10000
print("Probability of winning with 'change' strategy:", simulate_games(num_games, "change"))
print("Probability of winning with 'keep' strategy:", simulate_games(num_games, "keep"))
