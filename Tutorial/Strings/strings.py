
# s = "hello"
# s[0] = "H"  # Raises an error because strings are immutable

s = "Python"
print(s[0])  # Output: 'P'
print(s[-1])  # Output: 'n'

s = "Python"
print(s[0:4])  # Output: 'Pyth'
print(s[::2])  # Output: 'Pto' (skips every second character)

s1 = "Hello"
s2 = "World"
s3 = s1 + " " + s2  # Output: 'Hello World'
print(s1, " + ", s2, " = ", s3)

s = "Ha"
print(s * 3)  # Output: 'HaHaHa'

s = "Python"
print("Py" in s)  # Output: True
print("Java" not in s)  # Output: True

s = "Python"
print(len(s))  # Output: 6


s = "hello"
print(s.upper())  # Output: 'HELLO'

s = "HELLO"
print(s.lower())  # Output: 'hello'

s = "python"
print(s.capitalize())  # Output: 'Python'

s = "hello world"
print(s.title())  # Output: 'Hello World'

s = "  hello  "
print(s.strip())  # Output: 'hello'

print(s.lstrip())  # Output: 'hello  '

print(s.rstrip())  # Output: '  hello'

s = "Python programming"
print(s.find("program"))  # Output: 7

s = "Python programming"
print(s.replace("Python", "Java"))  # Output: 'Java programming'

s = "apple,banana,cherry"
fruits = s.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

fruits = ['apple', 'banana', 'cherry']
result = ", ".join(fruits)
print(result)  # Output: 'apple, banana, cherry'

name = "Alice"
age = 25
print("My name is %s and I am %d years old" % (name, age))

print("My name is {} and I am {} years old".format(name, age))

print(f"My name is {name} and I am {age} years old")

multiline_str = '''This is a\n
multiline\tstring that spans\'
multiple\"\\ lines.'''
print(multiline_str)