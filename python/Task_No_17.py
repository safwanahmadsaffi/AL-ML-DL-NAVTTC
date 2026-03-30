# Stop loop when number reaches 5
for i in range(1, 10):
    if i == 5:
        break  # Exit the loop
    print(i)

# Stop loop when condition is met
i = 1
while i <= 10:
    if i == 6:
        break  # Exit loop when i is 6
    print(i)
    i += 1

# Exit loop when user types 'quit'
while True:
    text = input("Enter text (quit to stop): ")
    
    if text.lower() == "quit":
        print("Loop stopped by user")
        break
    
    print("You entered:", text)

# Break only exits the inner loop
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            break  # Break inner loop only
        print(f"i={i}, j={j}")

# Else runs only if loop does NOT break
for i in range(1, 6):
    if i == 3:
        break  # Loop stops here
    print(i)
else:
    print("Loop completed")  # This will NOT execute

# Stop searching once item is found
numbers = [10, 20, 30, 40, 50]

for num in numbers:
    if num == 30:
        print("Found:", num)
        break  # Exit loop once found