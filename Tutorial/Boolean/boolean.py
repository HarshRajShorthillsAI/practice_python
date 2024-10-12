print(True + 1)   # Output: 2
print(False + 1)  # Output: 1

print(5 > 3)  # Output: True
print(2 == 3)  # Output: False

print(True and False)  # Output: False

print(True or False)  # Output: True

print(not True)  # Output: False

if []:
    print("This won't print")  # Empty list is falsy
else:
    print("Falsy value")  # Output: Falsy value

print(bool(0))       # Output: False
print(bool("hello")) # Output: True