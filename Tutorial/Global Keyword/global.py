count = 0  # Global variable

def increment():
    global count  # Declare count as global
    count += 1  # Modify the global variable

increment()
print("Count after increment:", count)  # Output: Count after increment: 1

message = "Hello, World!"  # Global variable

def print_message():
    print(message)  # Accessing global variable without modifying

print_message()  # Output: Hello, World!