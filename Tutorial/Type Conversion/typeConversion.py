x = 10   # int
y = 3.5  # float
result = x + y  # x is implicitly converted to float
print("x + y =", result) # Output: 13.5
print(type(result))  # Output: <class 'float'>

# String to integer
num_str = "100"
num_int = int(num_str)
print("num_str = ",num_int)  # Output: 100

# Float to integer
num_float = 10.75
num_int = int(num_float)  # Output: 10
print("num_int = ", num_int)

# Integer to string
num_str = str(50)
print(num_str)  # Output: "50"

try:
    val = int("abc")  # This will raise ValueError
except ValueError:
    print("Invalid conversion!")
