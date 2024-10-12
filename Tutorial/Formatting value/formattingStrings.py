name = "Alice"
age = 30
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)  # Output: My name is Alice and I am 30 years old.

name = "Bob"
age = 25
formatted_string = "My name is {0} and I am {1} years old. {0} is my nickname.".format(name, age)
print(formatted_string)  # Output: My name is Bob and I am 25 years old. Bob is my nickname.

formatted_string = "My name is {name} and I am {age} years old.".format(name="Charlie", age=40)
print(formatted_string)  # Output: My name is Charlie and I am 40 years old.

name = "Eve"
age = 22
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Eve and I am 22 years old.

x = 5
y = 10
formatted_string = f"The sum of {x} and {y} is {x + y}."
print(formatted_string)  # Output: The sum of 5 and 10 is 15.

pi = 3.14159
formatted_string = "Value of Pi: {:.2f}".format(pi)  # Formatting to 2 decimal places
print(formatted_string)  # Output: Value of Pi: 3.14

pi = 3.14159
formatted_string = f"Value of Pi: {pi:.2f}"  # Formatting to 2 decimal places
print(formatted_string)  # Output: Value of Pi: 3.14