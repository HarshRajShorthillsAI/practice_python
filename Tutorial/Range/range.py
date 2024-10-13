for i in range(5):
    print(i)

for i in range(2, 6):
    print(i)

for i in range(1, 10, 2):
    print(i)

for i in range(10, 0, -2):
    print(i)

my_range = range(1, 5)
print(list(my_range))

print(list(range(5, 5)))  # Output: []
print(list(range(5, 3)))  # Output: []

my_list = ['a', 'b', 'c']
for i in range(len(my_list)):
    print(i, my_list[i])