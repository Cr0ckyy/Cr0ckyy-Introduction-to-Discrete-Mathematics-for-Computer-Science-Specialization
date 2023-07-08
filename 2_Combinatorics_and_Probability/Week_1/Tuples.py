import itertools

# Number of letters in the alphabet
num_letters = 25

# Length of the combination
combo_length = 3

# Compute the number of combinations
num_combinations = num_letters ** combo_length

print(f'There are {num_combinations} different 3-letter combinations.')

# If you want to generate and print all combinations:
combinations = list(itertools.product(range(num_letters), repeat=combo_length))

# To view the combinations, uncomment the following line:
#print(combinations)
