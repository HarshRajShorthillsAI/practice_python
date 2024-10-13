x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print("Inner x:", x)  # Prints local x

    inner()  # Calls inner function
    print("Outer x:", x)  # Prints enclosing x

outer()  # Calls outer function
print("Global x:", x)  # Prints global x

count = 0  # Global variable

def increment():
    global count  # Declare count as global
    count += 1  # Modify global variable

increment()
print("Count after increment:", count)  # Output: Count after increment: 1

def outer():
    x = "enclosing"

    def inner():
        nonlocal x  # Declare x as nonlocal
        x = "modified"
        print("Inner x:", x)  # Prints modified x

    inner()
    print("Outer x:", x)  # Prints modified x

outer()