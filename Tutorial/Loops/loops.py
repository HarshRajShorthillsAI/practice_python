fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i in range(5):
    print(i)

x = 0
while x < 5:
    print(x)
    x += 1

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

for i in range(3):
    print(i)
else:
    print("Loop completed")

for i in range(3):
    for j in range(2):
        print(f"i: {i}, j: {j}")