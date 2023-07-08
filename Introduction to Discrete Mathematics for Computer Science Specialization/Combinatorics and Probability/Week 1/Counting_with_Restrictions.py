import math

# Q1: How many 3-digit numbers are there that have digits 1, 2, and 3 (each of them exactly once)?
num_three_digit_numbers = math.perm(3, 3)
print(f'Q1: There are {num_three_digit_numbers} 3-digit numbers with digits 1, 2, and 3 each exactly once.')

# Q2: A board of 15 people has to pick a chairman, a vice-chairman, and a secretary.
num_ways_board = math.perm(15, 3)
print(f'Q2: There are {num_ways_board} ways to pick a chairman, a vice-chairman, and a secretary among 15 people.')

# Q3: How many ways for 5 students to sit in 5 different tables.
num_ways_sit = math.perm(5, 5)
if num_ways_sit > 200:
    print(f'Q3: There are {num_ways_sit} ways for the students to sit, so it is possible to sit in a new way every day of the year.')
else:
    print(f'Q3: There are {num_ways_sit} ways for the students to sit, so it is not possible to sit in a new way every day of the year.')

# Q4: How many integer numbers between 0 and 9999 are there that have exactly one digit 1 and exactly one digit 3?
ways_to_choose_positions = math.comb(4, 2)
ways_to_arrange_digits = math.perm(2, 2)
ways_to_fill_remaining = 8 * 8
num_numbers_1_3 = ways_to_choose_positions * ways_to_arrange_digits * ways_to_fill_remaining
print(f'Q4: There are {num_numbers_1_3} integer numbers between 0 and 9999 that have exactly one digit 1 and exactly one digit 3.')
