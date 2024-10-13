a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # Output: True, because both lists have the same value

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b)  # Output: False, because they are different objects in memory

x = None
if x is None:
    print("x is None")  # This is the recommended way to check for None

a = 1000
b = 1000
print(a is b)  # Output: False (in most cases, as different memory locations)

c = 10
d = 10
print(c is d)  # Output: True (due to Python’s optimization of small integers)