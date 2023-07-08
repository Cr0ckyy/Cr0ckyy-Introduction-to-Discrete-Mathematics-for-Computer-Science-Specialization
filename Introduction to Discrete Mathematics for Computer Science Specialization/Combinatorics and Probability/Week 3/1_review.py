from itertools import product, permutations, combinations, combinations_with_replacement

# Tuples are ordered selections with repetitions
print("\nTuples:")
for t in product('abc', repeat=2):
    print(''.join(t), end=' ')
print("\n")

# Permutations are ordered selections without repetitions
print("Permutations:")
for t in permutations('abc', 2):
    print(''.join(t), end=' ')
print("\n")

# Combinations are unordered selections without repetitions
print("Combinations:")
for t in combinations('abc', 2):
    print(''.join(t), end=' ')
print("\n")

# Combinations with repetitions are unordered selections with repetitions
print("Combinations with repetitions:")
for t in combinations_with_replacement('abc', 2):
    print(''.join(t), end=' ')
print("\n")
