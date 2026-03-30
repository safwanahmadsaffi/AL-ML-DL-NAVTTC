# Can run any block of code by commenting other block of code or can be executed at the same time

# Print numbers from 1 to 5
i = 1
while i <= 5:
    print(i)
    i += 1  # Increment to avoid infinite loop

# Print even numbers from 2 to 10
i = 2
while i <= 10:
    print(i)
    i += 2  # Increase by 2 each time

# Loop runs until condition inside breaks it
i = 1
while True:
    print(i)
    if i == 5:
        break  # Exit loop when i is 5
    i += 1

# Print numbers from 1 to 10, skip multiples of 3
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue  # Skip current iteration
    print(i)

# Else executes when loop ends normally (no break)
i = 1
while i <= 3:
    print(i)
    i += 1
else:
    print("Loop finished without break")

# Keep asking user input until they type 'exit'
while True:
    user_input = input("Enter something (type 'exit' to quit): ")
    
    if user_input.lower() == "exit":
        print("Exiting loop...")
        break
    
    print("You entered:", user_input)