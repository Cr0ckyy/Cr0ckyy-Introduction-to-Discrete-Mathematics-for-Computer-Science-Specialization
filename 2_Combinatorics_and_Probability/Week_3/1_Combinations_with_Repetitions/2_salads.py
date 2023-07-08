from itertools import combinations_with_replacement

# Define the ingredients
ingredients = ['tomato', 'bell pepper', 'lettuce']

# Generate all salads
salads = list(combinations_with_replacement(ingredients, 4))

# Print the total number of salads
print(f"\nTotal number of different salads: {len(salads)}")

# Print each salad
for salad in salads:
    print(salad)


