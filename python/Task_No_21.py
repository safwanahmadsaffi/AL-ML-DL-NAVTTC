# Create a list
fruits = ["apple", "banana", "cherry", "mango"]

# Access elements
print(fruits[0])     # First element
print(fruits[-1])    # Last element

# Slice list
print(fruits[1:3])   # From index 1 to 2

numbers = [10, 20, 30]

# Add elements
numbers.append(40)
numbers.insert(1, 15)

# Remove elements
numbers.remove(20)
popped = numbers.pop()

print(numbers)
print("Removed:", popped)

colors = ["red", "green", "blue"]

# Using for loop
for color in colors:
    print(color)

# Using index
for i in range(len(colors)):
    print(f"Index {i}: {colors[i]}")

# Create squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]

# Even numbers only
evens = [x for x in range(1, 21) if x % 2 == 0]

print(squares)
print(evens)

marks = [85, 72, 90, 60, 88]

# Sort ascending
marks.sort()

# Sort descending
marks.sort(reverse=True)

# Reverse list
marks.reverse()

print(marks)

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Access element
print(matrix[1][2])  # 6

# Print matrix
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()

# Find maximum and minimum without built-in functions
nums = [12, 45, 7, 23, 56]

max_val = nums[0]
min_val = nums[0]

for n in nums:
    if n > max_val:
        max_val = n
    if n < min_val:
        min_val = n

print("Max:", max_val)
print("Min:", min_val)