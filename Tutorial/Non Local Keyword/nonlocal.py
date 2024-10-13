def outer_function():
    variable = value  # Variable in the outer scope

    def inner_function():
        nonlocal variable  # Declare the variable as nonlocal
        variable += 1  # Modify the variable

    inner_function()
    return variable  # Return the modified variable

def outer_function():
    count = 0  # Variable in the outer scope

    def inner_function():
        nonlocal count  # Declare count as nonlocal
        count += 1  # Modify the variable in the outer scope

    inner_function()
    return count  # Return the modified count

result = outer_function()
print("Count after inner function:", result)  # Output: Count after inner function: 1