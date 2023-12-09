def check_divisibility_by_4(consecutive_numbers):
    # If there are four consecutive numbers, one of them has to be divisible by 4.
    return "Yes, there always is one"

def check_divisibility_by_5(consecutive_numbers):
    # If there are four consecutive numbers, they may not necessarily include a multiple of 5.
    for number in consecutive_numbers:
        if number % 5 == 0:
            return "Yes, there always is one"
    return "No, for some numbers this is not true"

# Generate a list of four consecutive numbers starting from an arbitrary number, say 1
consecutive_numbers = list(range(1, 5))

# Check divisibility by 4
answer_1 = check_divisibility_by_4(consecutive_numbers)

# Check divisibility by 5
answer_2 = check_divisibility_by_5(consecutive_numbers)

print(answer_1 )
print(answer_2)