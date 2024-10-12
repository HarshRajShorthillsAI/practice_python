numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:4])  # Output: [1, 2, 3]

print(numbers[:3])  # Output: [0, 1, 2]

print(numbers[2:])  # Output: [2, 3, 4, 5]

print(numbers[0:6:2])  # Output: [0, 2, 4]

print(numbers[-4:-1])  # Output: [2, 3, 4]

print(numbers[::-1])  # Output: [5, 4, 3, 2, 1, 0]

print(numbers[2:10])  # Output: [2, 3, 4, 5]

copy_list = numbers[:]
print(copy_list)  # Output: [0, 1, 2, 3, 4, 5]
