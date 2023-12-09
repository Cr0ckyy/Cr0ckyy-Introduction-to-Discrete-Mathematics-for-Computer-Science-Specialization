# To solve the given questions, we'll check the divisibility of the provided numbers by 10, 5, and 2 respectively.

def check_divisibility(numbers, divisor):
    # Check divisibility for each number and return the result as a list of booleans
    return [number % divisor == 0 for number in numbers]


# Divisibility by 10 - Q1
q1_numbers = [25, 70, -20, 0]
q1_divisible_by_10 = check_divisibility(q1_numbers, 10)

# Divisibility by 5 - Q2
q2_numbers = [56, 30, -5, 1]
q2_divisible_by_5 = check_divisibility(q2_numbers, 5)

# Divisibility by 2 - Q3
q3_numbers = [276, 15, -233, 2]
q3_divisible_by_2 = check_divisibility(q3_numbers, 2)

# Combine results with question labels and print neatly
print("Divisibility by 10 - Q1:")
for number, divisible in zip(q1_numbers, q1_divisible_by_10):
    print(f"{number} is divisible by 10: {divisible}")

print("\nDivisibility by 5 - Q2:")
for number, divisible in zip(q2_numbers, q2_divisible_by_5):
    print(f"{number} is divisible by 5: {divisible}")

print("\nDivisibility by 2 - Q3:")
for number, divisible in zip(q3_numbers, q3_divisible_by_2):
    print(f"{number} is divisible by 2: {divisible}")
