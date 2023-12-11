from sympy import symbols, Eq, solve

# Define the symbols
x, y = symbols('x y')

# Equation and constraints
eq1 = Eq(6*x + 9*y, 27)
constraints1 = (4, 6)

eq2 = Eq(5*x + 3*y, 22)
constraints2 = (5, 10)

# Function to find the integer solutions within the given constraints
def find_integer_solution(eq, constraints):
    solutions = []
    for y_value in range(constraints[0] + 1, constraints[1]):
        sol = solve((eq, Eq(y, y_value)), (x, y))
        if sol[x].is_integer:
            solutions.append((sol[x], y_value))
    return solutions

# Find solutions for both equations
solutions1 = find_integer_solution(eq1, constraints1)
solutions2 = find_integer_solution(eq2, constraints2)

# Improved printing format
def print_solutions(solutions, equation_number):
    print(f"Solutions for Equation {equation_number}:")
    for solution in solutions:
        print(f"  x = {solution[0]}, y = {solution[1]}")
    print()  # Add an empty line for better separation

# Print solutions in the improved format
print_solutions(solutions1, 1)
print_solutions(solutions2, 2)
