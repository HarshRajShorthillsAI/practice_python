my_list = [1, 2, 3]
a, b, c = my_list
print(a, b, c)  # Output: 1 2 3

my_list = [1, 2, 3, 4, 5]
a, *b, c = my_list
print(a)  # Output: 1
print(b)  # Output: [2, 3, 4]
print(c)  # Output: 5

def pack_elements(*args):
    print(args)

pack_elements(1, 2, 3, 4)  # Output: (1, 2, 3, 4)

x, y = 10, 20
x, y = y, x
print(x, y)  # Output: 20, 10

nested_list = [1, [2, 3], 4]
a, [b, c], d = nested_list
print(a, b, c, d)  # Output: 1 2 3 4

my_list = [1, 2, 3, 4, 5]
a, *middle, c = my_list
print(a, middle, c)  # Output: 1 [2, 3, 4] 5