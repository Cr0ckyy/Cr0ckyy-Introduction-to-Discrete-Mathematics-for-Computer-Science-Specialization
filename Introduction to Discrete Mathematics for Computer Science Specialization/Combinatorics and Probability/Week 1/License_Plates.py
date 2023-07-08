# Number of possible digits
num_digits = 10

# Number of possible letters
num_letters = 26

# Number of characters in each block
block_size = 2

# Compute the number of possible license plates
num_plates = (num_digits ** block_size) * (num_letters ** block_size) * (num_digits ** block_size)

print(f'There are {num_plates} different license plates.')
