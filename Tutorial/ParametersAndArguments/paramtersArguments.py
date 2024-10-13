def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

def multiply(x, y):
    return x * y

result = multiply(4, 5)  # 4 is assigned to x and 5 to y

result = multiply(y=5, x=4)  # Here, arguments are provided in a different order

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!

def summarize(*args):  # Non-keyword variable-length arguments
    return sum(args)

print(summarize(1, 2, 3, 4))  # Output: 10

def describe_pet(pet_name, **kwargs):  # Keyword variable-length arguments
    print(f"Pet Name: {pet_name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_pet("Buddy", species="Dog", age=5)
