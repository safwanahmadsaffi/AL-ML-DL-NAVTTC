# Skip number 3 and print the rest
for i in range(1, 6):
    if i == 3:
        continue  # Skip this iteration
    print(i)

# Print only odd numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(i)

# Skip multiples of 3
i = 0
while i < 10:
    i += 1
    if i % 3 == 0:
        continue  # Skip numbers divisible by 3
    print(i)

# Skip the word "banana"
fruits = ["apple", "banana", "cherry", "banana"]

for fruit in fruits:
    if fruit == "banana":
        continue  # Skip this item
    print(fruit)

# Skip inner loop when j equals 2
for i in range(1, 4):
    for j in range(1, 4):
        if j == 2:
            continue  # Skip this iteration of inner loop
        print(f"i={i}, j={j}")

# Only process numbers, skip invalid input
while True:
    value = input("Enter a number (or 'exit'): ")
    
    if value.lower() == "exit":
        break
    
    if not value.isdigit():
        print("Invalid input, try again")
        continue  # Skip rest and ask again
    
    print("Valid number:", int(value))