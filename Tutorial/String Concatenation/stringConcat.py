str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: 'Hello World'

words = ["Hello", "world"]
result = " ".join(words)
print(result)  # Output: 'Hello World'

greeting = "Hello"
name = "Alice"
result = "{} {}".format(greeting, name)
print(result)  # Output: 'Hello Alice'

greeting = "hello"
name = "Alice"
result = f"{greeting} {name}"
print(result)  # Output: 'Hello Alice'

greeting = "Hello"
greeting += "-World"
print(greeting)  # Output: 'Hello World'
