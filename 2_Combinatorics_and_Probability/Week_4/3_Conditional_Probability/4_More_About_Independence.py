# Define the probabilities of events A and B
p = 0.5  # Probability of event A, Pr[A]
q = 0.4  # Probability of event B, Pr[B]

# Question 1: What is the probability of the event "A and B"?
prob_A_and_B = p * q

# Question 2: What is the probability of the event "A or B"?
prob_A_or_B = p + q - prob_A_and_B

# Question 3: What is the probability of the event "neither A nor B"?
prob_neither_A_nor_B = 1 - prob_A_or_B

# Display the results
print("Question 1: What is the probability of the event 'A and B'?")
print(f"Answer: {prob_A_and_B}")

print("\nQuestion 2: What is the probability of the event 'A or B'?")
print(f"Answer: {prob_A_or_B}")

print("\nQuestion 3: What is the probability of the event 'neither A nor B'?")
print(f"Answer: {prob_neither_A_nor_B}")

# The answers to questions 4, 5, and 6 are theoretical and don't involve computation
print("\nQuestion 4: Does it imply that the events 'not A' and 'B' are independent?")
print("Answer: Yes, the events 'not A' and 'B' are independent.")

print("\nQuestion 5: Does it imply that the events 'not A' and 'not B' are independent?")
print("Answer: Yes, the events 'not A' and 'not B' are independent.")

print("\nQuestion 6: Does it imply that the event (A and B) and the event C are independent?")
print("Answer: No, it is not always that case.")
