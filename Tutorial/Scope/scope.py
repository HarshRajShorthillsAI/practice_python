def my_function():
    x = 10  # Local variable
    print("Inside function:", x)

my_function()  # Output: Inside function: 10
# print(x)  # This would raise a NameError since x is not accessible here.

def outer_function():
    y = 20  # Enclosing variable

    def inner_function():
        print("Inside inner function:", y)

    inner_function()  # Output: Inside inner function: 20

outer_function()

z = 30  # Global variable

def another_function():
    global z  # Declaring z as global
    z += 10
    print("Inside function, modified global z:", z)

another_function()  # Output: Inside function, modified global z: 40
print("Global z after modification:", z)  # Output: Global z after modification: 40