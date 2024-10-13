def add_numbers(*args):
    """Returns the sum of all the numbers passed as arguments."""
    return sum(args)

result = add_numbers(1, 2, 3, 4, 5)  # result will be 15
print(result)  # Output: 15

def print_info(**kwargs):
    """Prints the information passed as keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

def combined_example(*args, **kwargs):
    """Prints positional and keyword arguments."""
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

combined_example(1, 2, 3, name="Alice", age=30)