def solve_1(n):
  return n % 3

def solve_2(n):
  """Function to solve n mod 5 for n ≡ 1 mod 6"""

  if n % 6 != 1:
    raise ValueError("n must be congruent to 1 mod 6")
  return n % 5

def solve_3(n):
  """Function to solve n mod 6 for n ≡ 2 mod 10"""

  # The possible remainders of n when divided by 6 are 0, 2, and 4.

  if n % 10 != 2:
    raise ValueError("n must be congruent to 2 mod 10")
  return n % 6

def solve_4():
    # Start with the smallest number greater than 0 that satisfies n ≡ 3 mod 11
    n = 3
    while True:
        # If n also satisfies n ≡ 7 mod 17, then we've found our smallest n
        if n % 17 == 7:
            return n
        # Otherwise, we try the next number that satisfies n ≡ 3 mod 11
        n += 11

# Print solutions
print("Question 1:")
print(f"If n ≡ 5 mod 9, n mod 3 can be:", solve_1(5))

print("\nQuestion 2:")
print(f"If n ≡ 1 mod 6, n mod 5 can be:", solve_2(1))

print("\nQuestion 3:")
print(f"If n ≡ 2 mod 10, n mod 6 can be:", solve_3(2))

print("\nQuestion 4:")
print(f"Smallest n for n ≡ 3 mod 11 and n ≡ 7 mod 17:", solve_4())
