print(True + True)  # Output: 2
print(True + False)  # Output: 1
print(False + False)  # Output: 0

x = 10
if x > 5:
    print("x is greater than 5")  # This block executes because the condition is True
else:
    print("x is less than or equal to 5")

a = True
b = False

print(a and b)  # Output: False
print(a or b)   # Output: True
print(not a)    # Output: False

if []:
    print("This won't print because the list is empty.")
else:
    print("An empty list is treated as False.")  # Output: This won't print because the list is empty.

if [1, 2, 3]:
    print("A non-empty list is treated as True.")  # Output: A non-empty list is treated as True.

x = 5
y = 10
print(x < y)   # Output: True
print(x == y)  # Output: False

print(bool(0))        # Output: False
print(bool(1))        # Output: True
print(bool(""))       # Output: False
print(bool("Hello"))  # Output: True