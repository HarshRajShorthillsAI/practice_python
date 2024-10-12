fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "apple", 3.14, True]

print(fruits[0])    # Output: apple
print(fruits[-1])   # Output: cherry

print(fruits[1:3])  # Output: ['banana', 'cherry']
print(fruits[::2])  # Output: ['apple', 'cherry'] (step of 2)

fruits[1] = "orange"  # ['apple', 'orange', 'cherry']
print(fruits)

fruits.append("grape")  # ['apple', 'orange', 'cherry', 'grape']
print(fruits)

fruits.remove("orange")  # ['apple', 'cherry', 'grape']
print(fruits)

fruits.append("mango")  # ['apple', 'cherry', 'grape', 'mango']
print(fruits)

fruits.insert(1, "pear")  # ['apple', 'pear', 'cherry', 'grape', 'mango']
print(fruits)

fruits.remove("pear")  # ['apple', 'cherry', 'grape', 'mango']
print(fruits)

fruits.pop()  # Removes and returns 'mango'
print(fruits)

numbers = [3, 1, 4, 2]
numbers.sort()  # [1, 2, 3, 4]
print(numbers)

squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
print(squares)

print("apple" in fruits)  # Output: True

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix[1][2])  # Output: 6