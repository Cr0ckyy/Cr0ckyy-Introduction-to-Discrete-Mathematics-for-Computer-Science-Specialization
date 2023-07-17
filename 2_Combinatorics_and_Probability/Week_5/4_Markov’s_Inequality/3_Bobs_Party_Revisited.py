# Here's how your Python program should look to avoid division by zero:

# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np

# Function to calculate upper bound on probability using Markov's Inequality
def markov_upper_bound(expected_value, threshold):
    """
    This function uses Markov's Inequality to calculate the upper bound on the probability
    of a non-negative random variable exceeding a certain threshold.

    Parameters:
    expected_value (float): The expected value of the random variable.
    threshold (float): The value which we want the random variable to exceed.

    Returns:
    float: Upper bound on the probability that the random variable will exceed the threshold.

    The function works as follows:
    1. It takes in two parameters - the expected value of a random variable and a threshold value.
    2. It calculates the upper bound on the probability that the random variable will exceed
       the threshold using the formula of Markov's Inequality: P(X >= a) <= E[X] / a
       where E[X] is the expected value of the random variable and a is the threshold.
    3. It returns this upper bound as a float.
    """

    # Calculate the upper bound on the probability using Markov's Inequality
    probability_upper_bound = expected_value / threshold

    # Return the upper bound
    return probability_upper_bound


# Define the expected number of guests at the party
E_X = 12

# Define the threshold number of guests
a = 18

# Use the function to calculate the upper bound on the probability using Markov's Inequality
upper_bound_probability = markov_upper_bound(E_X, a)

# Print the result
print(f"The upper bound probability that there will be at least {a} people at the party is: {upper_bound_probability}")


# Generate x values - start from 1 to avoid division by zero
x = np.arange(1, 31, 1)

# Generate corresponding y values according to Markov's inequality
y = E_X / x

# Create a new figure
plt.figure(figsize=(8, 6))

# Plot the values
plt.plot(x, y, label="Markov's Inequality")

# Highlight the point of interest
plt.scatter([a], [markov_upper_bound(E_X, a)], color='red')
plt.text(a, markov_upper_bound(E_X, a), '  (18, 0.67)', verticalalignment='bottom', fontsize=12, color='red')

# Add a legend
plt.legend()

# Set the x and y axis labels
plt.xlabel('Number of People')
plt.ylabel('Upper Bound on Probability')

# Add a title
plt.title("Upper Bound on the Probability of Attendance using Markov's Inequality")

# Display the plot
plt.show()
