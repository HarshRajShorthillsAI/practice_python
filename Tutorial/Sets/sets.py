my_set = {1, 2, 3, 4}
print(my_set)  # Output: {1, 2, 3, 4}

# Using set() constructor
my_set = set([1, 2, 3, 4])

empty_set = set()  # This is an empty set

my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # Output: {1, 2, 3, 4}

my_set = {1, 2, 3}
my_set.remove(2)
print(my_set)  # Output: {1, 3}

my_set = {1, 2, 3}
my_set.discard(4)  # No error even though 4 is not in the set
print(my_set)  # Output: {1, 2, 3}

my_set = {1, 2, 3}
element = my_set.pop()
print(element)  # Output: (Randomly selected element from the set)
print(my_set)  # Remaining elements in the set

my_set.clear()
print(my_set)  # Output: set()

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1 | set2)  # Output: {1, 2, 3, 4, 5}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 & set2)  # Output: {2, 3}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 - set2)  # Output: {1}

set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1 ^ set2)  # Output: {1, 4}

my_set = {1, 2, 3}
print(1 in my_set)  # Output: True
print(4 not in my_set)  # Output: True

set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True

set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True

set1 = {1, 2, 3}
set2 = {4, 5}
print(set1.isdisjoint(set2))  # Output: True

my_frozenset = frozenset([1, 2, 3, 4])
print(my_frozenset)  # Output: frozenset({1, 2, 3, 4})