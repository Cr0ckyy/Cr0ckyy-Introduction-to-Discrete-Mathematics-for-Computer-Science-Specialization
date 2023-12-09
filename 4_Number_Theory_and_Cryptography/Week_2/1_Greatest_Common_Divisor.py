# Define a function to calculate the Greatest Common Divisor (GCD) using Euclid's algorithm
def calculate_gcd(a, b):
    """
    Calculate the Greatest Common Divisor (GCD) of two numbers using Euclid's algorithm.

    Parameters:
    a (int): First number
    b (int): Second number

    Returns:
    int: GCD of the two numbers
    """
    while b:
        a, b = b, a % b
    return a

# Now, we will calculate the GCD for each pair of numbers asked in the questions

# Question 1: GCD of 2 and 3
gcd_1 = calculate_gcd(2, 3)

# Question 2: GCD of 15 and 24
gcd_2 = calculate_gcd(15, 24)

# Question 3: GCD of 20 and 100
gcd_3 = calculate_gcd(20, 100)

# Print out the GCD for each question with proper formatting
answers = {
    'Question 1': gcd_1,
    'Question 2': gcd_2,
    'Question 3': gcd_3
}

for question, gcd in answers.items():
    print(f'{question}: {gcd}')
