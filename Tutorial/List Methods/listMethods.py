my_list = [1, 2, 3]
my_list.append(4)
print("my_list: ", my_list)  # Output: [1, 2, 3, 4]

my_list = [1, 2, 3]
my_list.extend([4, 5])
print("my_list: ", my_list)  # Output: [1, 2, 3, 4, 5]

my_list = [1, 2, 4]
my_list.insert(2, 3)
print("my_list: ", my_list)  # Output: [1, 2, 3, 4]

my_list = [1, 2, 3, 2, 4]
my_list.remove(2)
print("my_list: ", my_list)  # Output: [1, 3, 2, 4]

my_list = [1, 2, 3]
element = my_list.pop(1)
print("element: ", element)  # Output: 2
print("my_list: ",my_list)  # Output: [1, 3]

my_list = [1, 2, 3]
my_list.clear()
print("my_list: ",my_list)  # Output: []

my_list = [1, 2, 3]
index = my_list.index(2)
print("index: ", index)  # Output: 1

my_list = [1, 2, 2, 3]
count = my_list.count(2)
print("count: ",count)  # Output: 2

my_list = [3, 1, 2]
my_list.sort()
print("my_list: ",my_list)  # Output: [1, 2, 3]

my_list = [1, 2, 3]
my_list.reverse()
print("my_list: ",my_list)  # Output: [3, 2, 1]

my_list = [1, 2, 3]
copy_list = my_list.copy()
print("copy_list: ",copy_list)  # Output: [1, 2, 3]

squares = [x**2 for x in range(5)]
print("squares: ", squares)  # Output: [0, 1, 4, 9, 16]
