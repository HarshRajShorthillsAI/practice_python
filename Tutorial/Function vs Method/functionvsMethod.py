def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8


def calculate(x, y):
    sum_value = x + y
    product_value = x * y
    return sum_value, product_value

result = calculate(4, 5)
print(result)  # Output: (9, 20)

# Unpacking the returned values
sum_value, product_value = calculate(4, 5)
print(sum_value)  # Output: 9
print(product_value)  # Output: 20

def print_message(message):
    print(message)
    # No return statement

result = print_message("Hello, World!")  # Output: Hello, World!
print(result)  # Output: None

def find_item(item, collection):
    for i in collection:
        if i == item:
            return i
    return None  # Item not found

result = find_item("apple", ["banana", "orange", "grape"])
print(result)  # Output: None