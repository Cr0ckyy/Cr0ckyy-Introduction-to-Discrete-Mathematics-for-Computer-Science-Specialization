import math  # Import the math library to use the GCD function


# Define a function to calculate the Least Common Multiple (LCM) using the GCD function
def calculate_lcm(a, b):
    """
    Calculate the Least Common Multiple (LCM) of two numbers based on the GCD.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: LCM of the two numbers
    """
    return abs(a * b) // math.gcd(a, b)


# Calculate the LCM for each pair of numbers asked in the questions

# Question 1: LCM of 2 and 3
lcm_1 = calculate_lcm(2, 3)

# Question 2: LCM of 10 and 15
lcm_2 = calculate_lcm(10, 15)

# Question 3: LCM of 35 and 70
lcm_3 = calculate_lcm(35, 70)

# Print out the LCM for each question with proper formatting
lcm_answers = {
    'Question 1': lcm_1,
    'Question 2': lcm_2,
    'Question 3': lcm_3
}

# Display the LCM answers
for question, answer in lcm_answers.items():
    print(f'{question}: {answer}')
