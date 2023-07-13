# Problem Description:
# A king decides to give a prisoner a chance of being set free. The king
# places two boxes, 15 white, and 15 black balls on the table. The
# prisoner can distribute the balls between two boxes in any way with the
# only constraint that no box is empty. After this, the king picks one of
# the boxes with probability 1/2 each, and picks a random ball from that
# box (each ball is picked with equal probability). If the ball happens to
# be white, then the prisoner is freed. We aim to distribute the balls
# between the two boxes to maximize the prisoner’s chances.

# Solution:
# We put one white ball in one box, and the rest of the balls (14 white and 15 black) in the other box.
# This way, one box gives a 100% chance of picking a white ball, and the other one gives a 14/29 chance.
# Given the king can choose either box with equal probability, the overall chance of the prisoner being freed is
# (1/2)*(1) + (1/2)*(14/29) = 71.5%.

# Python Implementation:

import random  # Import the required module

total_balls = 30  # Define the total number of balls
white_balls = 15
black_balls = 15

# Distribute the balls between the boxes
box1 = ['white']  # one box with one white ball
box2 = ['white']*14 + ['black']*15  # the other box with the rest of the balls

trials = 100000  # number of trials for our simulation
successful_trials = 0  # counter for successful trials (when a white ball is drawn)

# We simulate the process over many trials to empirically confirm the probability
for i in range(trials):
    chosen_box = random.choice([box1, box2])  # randomly select a box
    drawn_ball = random.choice(chosen_box)  # draw a ball from the chosen box
    if drawn_ball == 'white':  # if the ball is white, it's a successful trial
        successful_trials += 1

# Calculate and print the empirical probability of the prisoner being freed
print("The empirical probability of prisoner being freed is ", successful_trials / trials)
