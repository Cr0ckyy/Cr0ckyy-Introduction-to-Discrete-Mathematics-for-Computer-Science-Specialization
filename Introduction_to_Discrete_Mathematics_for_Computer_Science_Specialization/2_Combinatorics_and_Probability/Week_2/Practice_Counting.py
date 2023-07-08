from math import comb

# Question 1
num_hands = comb(13, 3) * comb(13, 3)
print(f"Answer to Question 1: {num_hands}")

# Question 2
num_bit_strings = comb(6, 3)
print(f"Answer to Question 2: {num_bit_strings}")

# Question 3
num_digit_sequences = comb(6, 3) * 5**3 * 5**3
print(f"Answer to Question 3: {num_digit_sequences}")

# Question 4 and 5
def num_paths(n):
    grid = [[0]*n for _ in range(n)]
    grid[0][0] = 1
    for i in range(n):
        for j in range(n):
            if i - 2 >= 0:
                grid[i][j] += grid[i - 2][j]
            if j - 3 >= 0:
                grid[i][j] += grid[i][j - 3]
    return grid[-1][-1]

print(f"Answer to Question 4: {num_paths(9)}")
print(f"Answer to Question 5: {num_paths(13)}")
