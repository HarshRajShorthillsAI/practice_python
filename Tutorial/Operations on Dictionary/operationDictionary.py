my_dict = {'name': 'Alice', 'age': 25}
my_dict.clear()
print(my_dict)  # Output: {}

my_dict = {'name': 'Alice', 'age': 25}
copy_dict = my_dict.copy()
print(copy_dict)  # Output: {'name': 'Alice', 'age': 25}

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.get('name'))  # Output: Alice
print(my_dict.get('city', 'Not found'))  # Output: Not found

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25)])

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

my_dict = {'name': 'Alice', 'age': 25}
print(my_dict.values())  # Output: dict_values(['Alice', 25])

my_dict = {'name': 'Alice', 'age': 25}
age = my_dict.pop('age')
print(age)  # Output: 25
print(my_dict)  # Output: {'name': 'Alice'}

my_dict = {'name': 'Alice', 'age': 25}
last_item = my_dict.popitem()
print(last_item)  # Output: ('age', 25)
print(my_dict)  # Output: {'name': 'Alice'}

my_dict = {'name': 'Alice'}
age = my_dict.setdefault('age', 30)  # Adds 'age' key with value 30 if not present
print(age)  # Output: 30
print(my_dict)  # Output: {'name': 'Alice', 'age': 30}

my_dict = {'name': 'Alice', 'age': 25}
my_dict.update({'age': 26, 'city': 'New York'})  # Updates 'age' and adds 'city'
print(my_dict)  # Output: {'name': 'Alice', 'age': 26, 'city': 'New York'}

keys = ['name', 'age', 'city']
default_dict = dict.fromkeys(keys, 'Unknown')
print(default_dict)  # Output: {'name': 'Unknown', 'age': 'Unknown', 'city': 'Unknown'}