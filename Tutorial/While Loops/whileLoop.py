i = 1
while i <= 5:
    print(i)
    i += 1


i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)

i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop ended")

while True:
    user_input = input("Enter 'q' to quit: ")
    if user_input == 'q':
        break

choice = ''
while choice != 'exit':
    print("1. Start Game")
    print("2. Options")
    print("Type 'exit' to quit.")
    choice = input("Choose an option: ")