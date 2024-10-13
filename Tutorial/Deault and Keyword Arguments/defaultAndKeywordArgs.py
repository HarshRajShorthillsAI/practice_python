def greet(name="Guest"):
    print(f"Hello, {name}!")

# Calling the function without an argument
greet()  # Output: Hello, Guest!

# Calling the function with an argument
greet("Alice")  # Output: Hello, Alice!

def describe_pet(pet_name, pet_type="Dog"):
    print(f"Pet Name: {pet_name}")
    print(f"Pet Type: {pet_type}")

# Calling the function using positional arguments
describe_pet("Buddy")  # Output: 
# Pet Name: Buddy
# Pet Type: Dog

# Calling the function using keyword arguments
describe_pet(pet_type="Cat", pet_name="Whiskers")  # Output:
# Pet Name: Whiskers
# Pet Type: Cat

