result = 0 and (5 / 0)  # The division is not evaluated because the left operand is False
print(result)  # Output: 0

result = 1 or (5 / 0)  # The division is not evaluated because the left operand is True
print(result)  # Output: 1

value = None
result = value is not None and len(value) > 0  # The len() function is not called if value is None
print(result)  # Output: False

def expensive_operation():
    print("Expensive operation executed")
    return True

result = False and expensive_operation()  # The function is never called
print(result)  # Output: False

x = 0
y = 10
result = x != 0 and (y / x > 1)  # The second part is not evaluated because x is 0
print(result)  # Output: False

x = 10
y = 0
result = x == 10 or (y / x > 1)  # The second part is not evaluated because x is 10
print(result)  # Output: True