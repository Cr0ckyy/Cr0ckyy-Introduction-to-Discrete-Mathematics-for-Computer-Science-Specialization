# Question:
# There are two boxes; the first one contains 10 white balls and 5 black balls;
# the other one contains 10 black balls and 5 white balls.
# King randomly selects a box (with equal probabilities) and then randomly takes a ball from this box (with equal probabilities).
# What is the probability that King selected the first box under the condition that the ball he selected is white?

# Step 1: Define prior probabilities
prior_box1 = 0.5  # Prior probability of choosing box 1
prior_box2 = 0.5  # Prior probability of choosing box 2

# Step 2: Define likelihoods
likelihood_white_box1 = 10 / 15  # Likelihood of drawing a white ball from box 1
likelihood_white_box2 = 5 / 15  # Likelihood of drawing a white ball from box 2

# Step 3: Calculate the marginal probability of drawing a white ball
marginal_white = prior_box1 * likelihood_white_box1 + prior_box2 * likelihood_white_box2

# Step 4: Apply Bayes' theorem
# P(Box 1 | White) = P(White | Box 1) * P(Box 1) / P(White)
posterior_box1_white = likelihood_white_box1 * prior_box1 / marginal_white

# Step 5: Print the result
print("The probability that King selected the first box given that the ball he selected is white is:", posterior_box1_white)
