age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult

x = 10
result = "Positive" if x > 0 else "Zero" if x == 0 else "Negative"
print(result)  # Output: Positive

if age >= 18:
    status = "Adult"
else:
    status = "Minor"