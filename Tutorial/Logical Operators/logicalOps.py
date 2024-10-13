a = True
b = False
result = a and b
print(result)  # Output: False

x = 0
y = 10
result = x != 0 and y / x > 1  # y / x is not evaluated because x != 0 is False
print(result)  # Output: False

a = False
b = True
result = a or b
print(result)  # Output: True

x = 10
y = 0
result = x == 10 or y / x > 1  # y / x is not evaluated because x == 10 is True
print(result)  # Output: True

a = True
result = not a
print(result)  # Output: False

x = 10
if not x == 10:
    print("x is not 10")
else:
    print("x is 10")  # Output: x is 10

a = True
b = False
c = True
result = a or b and not c
print(result)  # Output: True (evaluated as: a or (b and (not c)))

result = (a or b) and not c
print(result)  # Output: False

x = 5
y = 10
if x > 0 and y > 5:
    print("Both conditions are True")  # Output: Both conditions are True
else:
    print("One or both conditions are False")