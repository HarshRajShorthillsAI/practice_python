x = None
print(x)  # Output: None

x = None
print(x is None)  # Output: True

def my_func():
    pass

result = my_func()
print(result)  # Output: None

def greet(name=None):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hello, Guest!")

greet()  # Output: Hello, Guest!
greet("Alice")  # Output: Hello, Alice!

x = None
if not x:
    print("x is None or False")  # Output: x is None or False

x = 0
print(x is None)  # Output: False

y = None
print(y is None)  # Output: True