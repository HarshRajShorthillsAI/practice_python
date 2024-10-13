my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}

print(my_dict['name'])  # Output: Alice
print(my_dict.get('age'))  # Output: 25

my_dict['age'] = 26  # Modifying value
my_dict['profession'] = 'Engineer'  # Adding new key-value pair

my_dict['email'] = 'alice@example.com'  # Adding a new key-value pair
my_dict['city'] = 'Boston'  # Updating an existing key's value

my_dict.pop('age')  # Removes 'age' key-value pair
del my_dict['name']  # Deletes 'name' key-value pair

for key, value in my_dict.items():
    print(f'{key}: {value}')

my_dict = {1: 'one', 2: 'two', 2: 'second two'}  # Overwrites key 2
print(my_dict)  # Output: {1: 'one', 2: 'second two'}

my_dict = {'name': 'Alice', 'scores': [90, 85, 88], 'details': {'age': 25, 'city': 'New York'}}

squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}


# Creating a dictionary
student = {'name': 'John', 'age': 21, 'grade': 'A'}

# Accessing values
print(student['name'])  # Output: John

# Modifying values
student['grade'] = 'A+'

# Adding new key-value pair
student['major'] = 'Computer Science'

# Deleting a key-value pair
del student['age']

# Iterating over keys and values
for key, value in student.items():
    print(key, value)

# Output:
# name John
# grade A+
# major Computer Science
