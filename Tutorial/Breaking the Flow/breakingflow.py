for i in range(5):
    if i == 3:
        break  # Exits the loop when i is 3
    print(i)

# Output:
# 0
# 1
# 2

for i in range(5):
    if i == 3:
        continue  # Skips the iteration when i is 3
    print(i)

# Output:
# 0
# 1
# 2
# 4

for i in range(5):
    if i == 3:
        pass  # Placeholder for future implementation
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed successfully")

# Output:
# 0
# 1
# 2

def check_even(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"

result = check_even(4)
print(result)  # Output: Even
