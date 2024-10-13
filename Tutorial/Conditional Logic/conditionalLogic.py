x = 10
if x > 5:
    print("x is greater than 5")

# Output: x is greater than 5

x = 10
if x < 5:
    print("x is less than 5")
elif x == 10:
    print("x is equal to 10")

# Output: x is equal to 10

x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is 5 or less")

# Output: x is 5 or less

x = 10
if x > 5:
    print("x is greater than 5")
    if x > 8:
        print("x is also greater than 8")

# Output:
# x is greater than 5
# x is also greater than 8

x = 10
result = "Positive" if x > 0 else "Negative or Zero"
print(result)  # Output: Positive

x = 10
y = 5
if x > 5 and y < 10:
    print("Both conditions are True")

if x < 5 or y < 10:
    print("At least one condition is True")

if not (x == 10):
    print("x is not equal to 10")