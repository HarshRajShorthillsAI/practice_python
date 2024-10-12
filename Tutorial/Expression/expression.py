x = 10
y = 20
result = x < y  # Boolean expression, evaluates to True
is_valid = (x == 10 and y == 20)  # Logical expression combining conditions
print("is_valid", is_valid)

name = "Alice"
greeting = "Hello, " + name  # String concatenation
repeat = "ha" * 3  # String repetition, resulting in "hahaha"
print("name: ", name, "greeting: ", greeting, "repeat: ", repeat)

square = lambda x: x ** 2  # Lambda expression to compute square
result = square(5)  # Output: 25
print("result", result)

def add(a, b):
    return a + b

result = add(5, 10) * 2  # Function call `add(5, 10)` is part of the expression

expr = "5 + 2 * 3"
result = eval(expr)  # Evaluates the expression as if it were code
print(result)  # Output: 11
