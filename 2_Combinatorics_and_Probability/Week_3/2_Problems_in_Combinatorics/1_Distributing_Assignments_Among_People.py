from math import factorial

# Question 1
print("\nQuestion 1: Suppose there are 4 people and 9 different assignments. "
      "\nEach person should receive one assignment. Assignments for different people should be different. "
      "\nHow many ways are there to do it?")
num_assignments_1 = factorial(9) // factorial(9 - 4)
print(f"Answer: There are {num_assignments_1} ways to do it.\n")

# Question 2
print("Question 2: There are 4 people and 9 different assignments. "
      "\nWe need to distribute all assignments among people. No assignment should be assigned to two people. "
      "\nEvery person can be given arbitrary number of assignments from 0 to 9. How many ways are there to do it?")
num_assignments_2 = 4 ** 9
print(f"Answer: There are {num_assignments_2} ways to do it.\n")
