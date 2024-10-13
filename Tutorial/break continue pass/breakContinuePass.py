for number in range(10):
    if number == 5:
        print("Found 5, exiting loop")
        break
    print(number)

for number in range(5):
    if number == 2:
        print("Skipping 2")
        continue
    print(number)

for number in range(5):
    if number == 3:
        pass  # Placeholder for future code
    print(number)