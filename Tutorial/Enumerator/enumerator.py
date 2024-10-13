my_list = ['apple', 'banana', 'cherry']
for index, value in enumerate(my_list):
    print(index, value)

for index, value in enumerate(my_list, start=1):
    print(index, value)

my_string = "hello"
for index, char in enumerate(my_string):
    print(index, char)

my_tuple = tuple(enumerate(['a', 'b', 'c']))
print(my_tuple)

fruits = ['apple', 'banana', 'cherry', 'date']
for index, fruit in enumerate(fruits):
    if fruit == 'cherry':
        print(f"'cherry' found at index {index}")