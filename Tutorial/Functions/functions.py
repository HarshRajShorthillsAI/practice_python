def greet(name):
    """Function to greet a person by name."""
    print(f"Hello, {name}!")

def greet(name):
    """Function to greet a person by name."""
    print(f"Hello, {name}!")

greet("Alice")

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()

def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

def summarize(*args):
    return sum(args)

print(summarize(1, 2, 3, 4))  # Output: 10

def describe_pet(pet_name, **kwargs):
    print(f"Pet Name: {pet_name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_pet("Buddy", species="Dog", age=5)