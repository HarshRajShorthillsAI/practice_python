my_dict = {1: 'one', 2: 'two', 1: 'first'}
print(my_dict)  # Output: {1: 'first', 2: 'two'}

my_dict = {
    'name': 'Alice',
    42: 'Answer to life',
    (1, 2): 'tuple as key'
}
print(my_dict)

try:
    my_dict = {[1, 2]: 'list as key'}  # This raises a TypeError
except:
    print("error")

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict['name'])  # Output: Alice
print(my_dict.get('city'))  # Output: None
print(my_dict.get('city', 'Not Found'))  # Output: Not Found

# String as a key
person = {'name': 'John', 'age': 30}
print(person)

# Integer as a key
numbers = {1: 'one', 2: 'two'}
print(numbers)

# Tuple as a key
coordinates = {(0, 0): 'origin', (1, 2): 'point'}
print(coordinates)

my_dict = {'a': 1, 'b': 2, 'c': 3}
for key in my_dict:
    print(key, my_dict[key])  # Output: a 1, b 2, c 3 (in insertion order)

my_dict = {'name': 'Alice', 'age': 25}
print('name' in my_dict)  # Output: True
print('city' in my_dict)  # Output: False

del my_dict['age']  # Removes the 'age' key and its value

for key in my_dict:
    print(key, my_dict[key])