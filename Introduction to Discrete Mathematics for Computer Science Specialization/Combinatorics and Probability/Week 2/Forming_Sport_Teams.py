import math

# Question 1
print("Question 1:")
total_students = 10
team_size = 5
ways_to_select_team = math.comb(total_students, team_size)
print("Number of ways to select a team of five students:", ways_to_select_team)

# Question 2
print("\nQuestion 2:")
ways_to_partition_teams = math.comb(total_students, team_size) // 2
print("Number of ways to partition ten students into two teams of size five:", ways_to_partition_teams)
