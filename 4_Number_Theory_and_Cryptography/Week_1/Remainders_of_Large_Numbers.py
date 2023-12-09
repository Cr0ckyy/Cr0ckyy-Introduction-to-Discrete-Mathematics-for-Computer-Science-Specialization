# Question 1: What is the remainder of the number 762341 when divided by 3?
remainder_q1 = 762341 % 3

# Question 2: What is the remainder of the number 12^100 when divided by 11?
# For large exponents, we can use modular exponentiation to find the remainder.
# The pattern of remainders when base 12 is divided by 11 will repeat every 10 powers because 12^10 % 11 = 1
# Thus, 12^100 is (12^10)^10, and since 12^10 % 11 = 1, then (12^10)^10 % 11 = 1^10 % 11
remainder_q2 = (12**10 % 11)**(100//10) % 11

# Question 3: What is the remainder of the number 4632^10 when divided by 10?
# Any number raised to any power and then divided by 10 will have the same remainder as the last digit of the base
# raised to that power divided by 10. Since 4632 ends in 2, we need to find the remainder of 2^10 when divided by 10.
remainder_q3 = (2**10) % 10

# Print the results neatly on separate lines
print("Question 1: What is the remainder of the number 762341 when divided by 3?")
print(f"Remainder: {remainder_q1}\n")

print("Question 2: What is the remainder of the number 12^100 when divided by 11?")
print(f"Remainder: {remainder_q2}\n")

print("Question 3: What is the remainder of the number 4632^10 when divided by 10?")
print(f"Remainder: {remainder_q3}")
