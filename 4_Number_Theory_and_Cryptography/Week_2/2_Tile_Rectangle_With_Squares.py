# The problem statement suggests that we need to find the minimum number of squares to tile a grid of size n x m.
# This can be done by finding the greatest common divisor (GCD) of n and m, which will give us the size of the largest
# square that can tile the grid without overlap or gaps. The number of such squares will be (n*m) / (gcd(n,m))^2.

# We will use the math library which provides the gcd function.
import math

# Define the squares function with a docstring explaining its purpose and parameters
def squares(n, m):
    """
    Calculate the minimum number of same size squares required to tile a grid of size n x m.

    Parameters:
    n (int): The number of rows in the grid.
    m (int): The number of columns in the grid.

    Returns:
    int: The minimum number of squares required to tile the grid.
    """
    # Find the greatest common divisor of n and m
    gcd_value = math.gcd(n, m)

    # Calculate the number of squares needed
    # The area of the grid is n * m
    # The area of one square is gcd_value^2
    # So the number of squares is (n * m) / (gcd_value^2)
    return (n * m) // (gcd_value ** 2)

# Now we can test the function with the given example of a 6 x 10 grid
# According to the problem statement, the expected result is 15 squares of size 2 x 2
test_n = 6
test_m = 10
test_result = squares(test_n, test_m)

# Print the result
print(test_result)
