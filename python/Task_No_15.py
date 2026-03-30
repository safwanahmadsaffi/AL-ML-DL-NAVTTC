# Can run any block of code by commenting other block of code or can be executed at the same time

# Print numbers from 1 to 5
for i in range(1, 6):
    print(i)

# Iterate over a list of fruits
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# The else block runs after the loop finishes
for i in range(3):
    print("Number:", i)
else:
    print("Loop completed successfully")

# Print a simple pattern using nested loops
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()  # Move to next line

# Stop loop when number equals 4
for i in range(1, 10):
    if i == 4:
        break
    print(i)

# Skip even numbers and print only odd numbers
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print(i)