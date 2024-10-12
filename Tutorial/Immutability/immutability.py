text = "hello"

print("text id: ", id(text))
# text[0] = "H"  # This would raise a TypeError
text = "Hello"  # This creates a new string, not modifying the original
print("text id: ", id(text))

my_tuple = (1, 2, 3)
try:
    my_tuple[0] = 10
except:
    print("error")

a = 5
print("id(a) = ", id(a))
a = a + 1  # A new integer object (6) is created, not modifying the original 5
print("id(a) = ", id(a))

x = 2.5
print("id(x) = ", id(x))
x = x + 0.5  # A new float object is created
print("id(x) = ", id(x))

flag = True
print("id(flag) = ", id(flag))

flag = False
print("id(flag) = ", id(flag))

my_frozenset = frozenset([1, 2, 3])
try:
    my_frozenset.add(4)  # Raises AttributeError as frozensets are immutable
except:
    print("error")