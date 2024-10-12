x = 5
y = "John"
print(x)

print(type(x))

print(y)

print(type(y)) 

x = "Sally" # x is now of type str
print(x)

a, b, c = 1, 2, "Three"
print(a, b, c)

def my_function():
    global t
    t = 3
    u = 10  # Local variable
    print(u)

my_function()  # Output: 10

print(t)

del x
print(x)