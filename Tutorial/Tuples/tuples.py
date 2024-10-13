my_tuple = ()

my_tuple = (1, 2, 3, 'hello', 4.5)

single_element_tuple = (1,)

my_tuple = (10, 20, 30, 40)
print(my_tuple[1])  # Output: 20

print(my_tuple[2])  # Output: 30

print(my_tuple[1:3])  # Output: (20, 30)

print(len(my_tuple))  # Output: 4

new_tuple = my_tuple + (50, 60)
print(new_tuple)  # Output: (10, 20, 30, 40, 50, 60)

repeated_tuple = my_tuple * 2
print(repeated_tuple)  # Output: (10, 20, 30, 40, 10, 20, 30, 40)

my_tuple = (1, 2, 3, 2, 2, 4)
print(my_tuple.count(2))  # Output: 3

print(my_tuple.index(3))  # Output: 2

my_tuple = (1, 2, 3)
a, b, c = my_tuple
print(a)  # Output: 1
print(b)  # Output: 2
print(c)  # Output: 3

nested_tuple = (1, (2, 3), (4, (5, 6)))
print(nested_tuple[2][1][1])  # Output: 6

my_tuple = (1, 2, 3)
try:
    my_tuple[1] = 4  # This will raise a TypeError
except:
    print("error")

coordinates = (10.0, 20.0)  # A tuple to represent x and y coordinates

# Returning multiple values from a function
def min_max(data):
    return min(data), max(data)

result = min_max([1, 2, 3, 4, 5])
print(result)  # Output: (1, 5)